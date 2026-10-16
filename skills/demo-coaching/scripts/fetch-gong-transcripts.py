#!/usr/bin/env python3
"""
Fetch demo call transcripts from Gong for the demo-coaching skill.

Usage (run from the skill directory):
  python3 scripts/fetch-gong-transcripts.py                       # whole team, last 14 days
  python3 scripts/fetch-gong-transcripts.py --se jane             # one person (name or email from config.json)
  python3 scripts/fetch-gong-transcripts.py --se jane@acme.com --days 30
  python3 scripts/fetch-gong-transcripts.py --id <call_id>        # one specific call

Credentials: GONG_ACCESS_KEY and GONG_ACCESS_KEY_SECRET env vars, or
gong_credentials.json in the skill directory (prompted and saved on first run).

Config: config.json in the skill directory (see config.example.json).
"""

import argparse
import base64
import getpass
import json
import os
import pathlib
import re
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone

# -- Config -------------------------------------------------------------------

SKILL_DIR = pathlib.Path(__file__).resolve().parent.parent
CONFIG_FILE = SKILL_DIR / "config.json"
CREDENTIALS_FILE = SKILL_DIR / "gong_credentials.json"
DEFAULT_BASE_URL = "https://api.gong.io"
DEMO_TITLE_TERMS = ["demo", "solution overview", "walkthrough", "evaluation", "platform overview"]


def load_config():
    if not CONFIG_FILE.exists():
        print(f"Missing {CONFIG_FILE}. Copy config.example.json to config.json and fill in your team.",
              file=sys.stderr)
        sys.exit(1)
    with open(CONFIG_FILE) as f:
        return json.load(f)


def resolve_se_arg(se_arg, team):
    """Accept an email or any name from config.json's team map (case-insensitive)."""
    if not se_arg:
        return list(team.values())
    if "@" in se_arg:
        return [se_arg]
    needle = se_arg.lower()
    for name, email in team.items():
        if needle == name.lower() or needle in name.lower():
            return [email]
    print(f"'{se_arg}' is not in config.json team list and is not an email.", file=sys.stderr)
    sys.exit(1)

# -- Credentials --------------------------------------------------------------

def load_credentials():
    key, secret = os.environ.get("GONG_ACCESS_KEY"), os.environ.get("GONG_ACCESS_KEY_SECRET")
    if key and secret:
        return key, secret

    if CREDENTIALS_FILE.exists():
        with open(CREDENTIALS_FILE) as f:
            creds = json.load(f)
        return creds["access_key"], creds["access_key_secret"]

    print("Gong credentials not found. Create an API key under Gong Settings > API, then enter:")
    key = getpass.getpass("Access Key: ")
    secret = getpass.getpass("Access Key Secret: ")
    with open(CREDENTIALS_FILE, "w") as f:
        json.dump({"access_key": key, "access_key_secret": secret}, f, indent=2)
    os.chmod(CREDENTIALS_FILE, 0o600)
    print(f"Saved to {CREDENTIALS_FILE}\n")
    return key, secret


def auth_header(access_key, access_key_secret):
    token = base64.b64encode(f"{access_key}:{access_key_secret}".encode()).decode()
    return f"Basic {token}"

# -- API ----------------------------------------------------------------------

def api_request(method, base_url, path, access_key, access_key_secret, body=None, params=None):
    url = f"{base_url}{path}"
    if params:
        url += "?" + urllib.parse.urlencode(params, doseq=True)

    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(url, data=data, method=method, headers={
        "Authorization": auth_header(access_key, access_key_secret),
        "Content-Type": "application/json",
        "Accept": "application/json",
    })
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f"API error {e.code}: {e.read().decode()}", file=sys.stderr)
        sys.exit(1)


def api_get(base_url, path, access_key, access_key_secret, params=None):
    return api_request("GET", base_url, path, access_key, access_key_secret, params=params)


def api_post(base_url, path, access_key, access_key_secret, body=None):
    return api_request("POST", base_url, path, access_key, access_key_secret, body=body)

# -- Users --------------------------------------------------------------------

def resolve_users(base_url, access_key, access_key_secret, target_emails):
    """Resolve emails to Gong user IDs. Returns {email: {id, name}}."""
    target_set = {e.lower() for e in target_emails}
    mapping = {}
    cursor = None

    while True:
        params = {"cursor": cursor} if cursor else {}
        data = api_get(base_url, "/v2/users", access_key, access_key_secret, params=params)

        for user in data.get("users", []):
            email = (user.get("emailAddress") or "").lower()
            if email in target_set:
                name = f"{user.get('firstName', '')} {user.get('lastName', '')}".strip() or email.split("@")[0]
                mapping[email] = {"id": user["id"], "name": name}

        cursor = data.get("records", {}).get("cursor")
        if not cursor:
            break

    return mapping

# -- Formatting ---------------------------------------------------------------

def format_seconds(ms):
    """Gong sentence `start` values are milliseconds."""
    s = int(ms or 0) // 1000
    return f"{s // 60:02d}:{s % 60:02d}"


def format_duration(seconds):
    if not seconds:
        return "-"
    m, s = divmod(int(seconds), 60)
    return f"{m}m {s:02d}s"


def sanitize_filename(s):
    s = re.sub(r'[/\\:*?"<>|]', '_', s or "Unknown")
    return re.sub(r'\s+', ' ', s).strip()[:80]


def call_date(call):
    started = call.get("started")
    if not started:
        return ""
    try:
        return datetime.fromisoformat(started.replace("Z", "+00:00")).strftime("%Y-%m-%d")
    except ValueError:
        return "unknown-date"


def format_transcript(monologues, speaker_map):
    """Gong monologues -> '>>Speaker\\tMM:SS\\ntext\\n' blocks."""
    lines = []
    for monologue in monologues:
        speaker = speaker_map.get(monologue.get("speakerId"), f"Speaker {monologue.get('speakerId')}")
        sentences = monologue.get("sentences", [])
        if not sentences:
            continue
        text = " ".join((s.get("text") or "").strip() for s in sentences).strip()
        if text:
            lines += [f">>{speaker}\t{format_seconds(sentences[0].get('start', 0))}", text, ""]
    return "\n".join(lines) if lines else None


def make_filename(call):
    title = sanitize_filename(call.get("title") or call.get("purpose") or "Untitled")
    account = "Unknown"
    for ctx in call.get("context") or []:
        if ctx.get("system") == "Salesforce":
            for obj in ctx.get("objects", []):
                if obj.get("objectType") == "Account":
                    account = sanitize_filename(obj.get("name", "Unknown"))
                    break
    return f"{account}__{title}__{call_date(call)}.txt"

# -- Display ------------------------------------------------------------------

def display_calls(calls, user_map_by_id):
    print(f"\nFound {len(calls)} demo call(s):\n")
    print(f"{'#':>3}  {'Date':<12}  {'SE':<22}  {'Duration':>8}  Title")
    print("-" * 90)
    for i, c in enumerate(calls, 1):
        se = next((user_map_by_id[pid] for pid in c.get("participantsIds", []) if pid in user_map_by_id), "")
        title = (c.get("title") or c.get("purpose") or "")[:50]
        print(f"{i:>3}  {call_date(c):<12}  {se:<22}  {format_duration(c.get('duration')):>8}  {title}")
    print()

# -- Fetch & Save -------------------------------------------------------------

def fetch_transcript(base_url, call_id, access_key, access_key_secret):
    data = api_post(base_url, "/v2/calls/transcript", access_key, access_key_secret,
                    body={"filter": {"callIds": [call_id]}})
    transcripts = data.get("callTranscripts", [])
    return transcripts[0].get("transcript", []) if transcripts else []


def build_speaker_map(call, user_map_by_id):
    """speakerId -> display name, preferring the Gong user name for internal participants."""
    speaker_map = {}
    for party in call.get("parties", []):
        sid = party.get("speakerId")
        if sid is None:
            continue
        name = party.get("name") or party.get("emailAddress", "").split("@")[0].replace(".", " ").title()
        speaker_map[sid] = user_map_by_id.get(party.get("userId"), name)
    return speaker_map


def fetch_and_save(base_url, call_id, call_meta, access_key, access_key_secret, user_map_by_id, output_dir):
    """Save transcript .txt plus .json sidecar (per-sentence ms timestamps for annotations)."""
    print(f"  Fetching transcript for call {call_id}...")
    monologues = fetch_transcript(base_url, call_id, access_key, access_key_secret)
    if not monologues:
        print(f"  Warning: no transcript for call {call_id}")
        return None

    speaker_map = build_speaker_map(call_meta, user_map_by_id)
    text = format_transcript(monologues, speaker_map)
    if not text:
        print(f"  Warning: empty transcript for call {call_id}")
        return None

    dest_dir = pathlib.Path(output_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)
    output_path = dest_dir / make_filename(call_meta)
    output_path.write_text(text, encoding="utf-8")
    print(f"  Saved: {output_path}")

    flat = [
        {"speaker": speaker_map.get(m.get("speakerId"), f"Speaker {m.get('speakerId')}"),
         "start": s.get("start", 0), "text": (s.get("text") or "").strip()}
        for m in monologues for s in m.get("sentences", []) if (s.get("text") or "").strip()
    ]
    sidecar = {
        "call_id": call_id,
        "call_review_page_url": f"https://app.gong.io/call?id={call_id}",
        "title": call_meta.get("title") or call_meta.get("purpose") or "",
        "date": call_date(call_meta),
        "transcript": flat,
    }
    sidecar_path = output_path.with_suffix(".json")
    sidecar_path.write_text(json.dumps(sidecar, indent=2), encoding="utf-8")
    print(f"  Saved: {sidecar_path} (timestamps)")
    return output_path

# -- Main ---------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Fetch Gong demo transcripts for coaching")
    parser.add_argument("--se", help="Person to filter by: a name from config.json or an email (default: whole team)")
    parser.add_argument("--days", type=int, default=14, help="Lookback window in days (default: 14)")
    parser.add_argument("--id", dest="call_id", help="Download one specific call by Gong ID")
    parser.add_argument("--all", action="store_true", help="Download every match without prompting")
    parser.add_argument("--output-dir", help="Override transcripts_dir from config.json")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL, help="Gong API base URL (EU tenants use a different host)")
    args = parser.parse_args()

    config = load_config()
    team = config.get("team", {})
    output_dir = args.output_dir or config.get("transcripts_dir", "transcripts")
    access_key, access_key_secret = load_credentials()
    base_url = args.base_url.rstrip("/")

    se_emails = resolve_se_arg(args.se, team)
    if not se_emails:
        print("No team members in config.json and no --se given.", file=sys.stderr)
        sys.exit(1)

    print("Resolving Gong user IDs...")
    user_map = resolve_users(base_url, access_key, access_key_secret, se_emails)
    if not user_map:
        print("No Gong users matched those emails. Check config.json against Gong user accounts.", file=sys.stderr)
        sys.exit(1)
    user_map_by_id = {v["id"]: v["name"] for v in user_map.values()}
    print(f"  Found {len(user_map)} person(s) in Gong")

    if args.call_id:
        data = api_post(base_url, "/v2/calls/extensive", access_key, access_key_secret,
                        body={"filter": {"callIds": [args.call_id]},
                              "contentSelector": {"exposedFields": {"parties": True}}})
        calls = data.get("calls", [])
        if not calls:
            print(f"Call {args.call_id} not found.", file=sys.stderr)
            sys.exit(1)
        meta = calls[0].get("metaData", calls[0])
        meta["parties"] = calls[0].get("parties", [])
        fetch_and_save(base_url, args.call_id, meta, access_key, access_key_secret, user_map_by_id, output_dir)
        return

    now = datetime.now(timezone.utc)
    print(f"Searching Gong for demo calls in the last {args.days} day(s)...")
    if args.se:
        print(f"  Filter: {', '.join(se_emails)}")

    all_calls, cursor = [], None
    while True:
        body = {
            "filter": {"fromDateTime": (now - timedelta(days=args.days)).isoformat(),
                       "toDateTime": now.isoformat()},
            "contentSelector": {"exposedFields": {"parties": True, "content": {"structure": True}}},
        }
        if cursor:
            body["cursor"] = cursor
        data = api_post(base_url, "/v2/calls/extensive", access_key, access_key_secret, body=body)
        for call_data in data.get("calls", []):
            meta = call_data.get("metaData", {})
            meta["parties"] = call_data.get("parties", [])
            meta["participantsIds"] = [p.get("userId") for p in meta["parties"] if p.get("userId")]
            all_calls.append(meta)
        cursor = data.get("records", {}).get("cursor")
        if not cursor:
            break

    user_id_set = set(user_map_by_id)
    calls = [c for c in all_calls
             if any(t in (c.get("title") or c.get("purpose") or "").lower() for t in DEMO_TITLE_TERMS)
             and set(c.get("participantsIds", [])) & user_id_set]
    calls.sort(key=lambda c: c.get("started", ""), reverse=True)

    if not calls:
        print("No demo calls found. Try --days 30 or a different --se filter.")
        print("Only calls whose title contains a demo-like term are listed. Use --id <call_id> for anything else.")
        return

    display_calls(calls, user_map_by_id)

    if args.all:
        selected = calls
    else:
        print("Enter call number(s) to download (e.g. 1  or  1 3 5), 'a' for all, 'q' to quit:")
        choice = input("> ").strip().lower()
        if choice in ("q", ""):
            print("Cancelled.")
            return
        if choice == "a":
            selected = calls
        else:
            try:
                selected = [calls[int(x) - 1] for x in choice.split() if 0 < int(x) <= len(calls)]
            except ValueError:
                print("Invalid selection.")
                return
        if not selected:
            print("No valid calls selected.")
            return

    print(f"\nDownloading {len(selected)} transcript(s)...\n")
    saved = [p for call in selected if call.get("id")
             for p in [fetch_and_save(base_url, call["id"], call, access_key, access_key_secret,
                                      user_map_by_id, output_dir)] if p]
    print(f"\nDone. {len(saved)} transcript(s) saved to {output_dir}/")
    print("Run /demo-coaching to score and generate feedback.")


if __name__ == "__main__":
    main()
