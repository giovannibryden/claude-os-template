#!/usr/bin/env python3
"""List the only files a growth cycle review may draw on.

    bin/gc-sources.py Jane_Doe "H2 FY27"            # list sources
    bin/gc-sources.py Jane_Doe "H2 FY27" --check f  # fail if f cites a file outside the window

Window = after the most recent prior-cycle review file's date (Written, Submitted,
Converted, else git date) through today. Prior is decided by the Review Period
label, never by file date. Claude-written roll-ups (cert results, briefs, themes)
are never listed, so they can't be cited as evidence.
"""
import datetime, pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATE = re.compile(r"(\d{4}-\d{2}-\d{2})")


def cycle_key(label):
    m = re.search(r"H([12])[ _]FY(\d+)", label, re.I)
    if not m:
        sys.exit(f"Can't parse cycle from {label!r}; use e.g. 'H2 FY27'")
    return int(m[2]), int(m[1])


def front(path):
    text = path.read_text()
    fm = text.split("---")[1] if text.startswith("---") else ""
    return dict(re.findall(r"^([\w -]+):\s*(.+)$", fm, re.M)), text


def file_date(path, fm):
    for k in ("Written", "Submitted", "Converted"):
        if k in fm and DATE.search(fm[k]):
            return DATE.search(fm[k])[1]
    out = subprocess.run(["git", "log", "-1", "--format=%cs", "--", str(path)],
                         cwd=ROOT, capture_output=True, text=True).stdout.strip()
    return out or None


def sources(person, cycle):
    cur = cycle_key(cycle)
    first, last = person.lower().split("_", 1)
    slug = f"{first}-{last.replace('_', '-')}"
    prior, current_self = [], None
    for p in sorted((ROOT / "growth-cycle-reviews" / person).glob("*.md")):
        fm, text = front(p)
        key = cycle_key(fm.get("Review Period", p.name))
        if key < cur:
            prior.append((key, p, fm))
        elif key == cur and "## Self-Review" in text:
            current_self = p
    prior.sort()
    start = file_date(prior[-1][1], prior[-1][2]) if prior else None
    today = datetime.date.today().isoformat()

    def in_window(pattern):
        hits = []
        for p in sorted(ROOT.glob(pattern)):
            d = DATE.search(p.name)
            if d and (start is None or d[1] > start) and d[1] <= today:
                hits.append(p)
        return hits

    evidence = (in_window(f"team/1-1s/{slug}-20*.md") + in_window(f"team/1-1s/{first}-20*.md")
                + in_window(f"team/performance/{slug}-demo-*.md"))
    if current_self:
        evidence.append(current_self)
    return start, today, [p for _, p, _ in prior], evidence


def rel(p):
    return str(p.relative_to(ROOT))


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    person, cycle = sys.argv[1], sys.argv[2]
    start, today, prior, evidence = sources(person, cycle)
    allowed = {rel(p) for p in evidence}

    if "--check" in sys.argv:
        draft = pathlib.Path(sys.argv[sys.argv.index("--check") + 1]).read_text()
        cited = set(re.findall(r"((?:team|growth-cycle-reviews|meetings|strategy|deals|personal)/[\w./-]+\.md)", draft))
        bad = sorted(cited - allowed)
        for b in bad:
            print(f"OUT OF WINDOW OR NOT EVIDENCE: {b}")
        sys.exit(1 if bad else 0)

    print(f"Window: after {start or '(no prior review: all dates)'} through {today}")
    print("\nPrior reviews (prior-view subagent only, never evidence):")
    print("\n".join(f"  {rel(p)}" for p in prior) or "  none")
    print("\nEvidence (the only files the writer may read):")
    print("\n".join(f"  {p}" for p in sorted(allowed)) or "  none")
    if not any("## Self-Review" in p.read_text() for p in evidence):
        print("\nCurrent self-review: not on disk. Pull it from your review tool or the inbox, or write without alignment language.")


if __name__ == "__main__":
    main()
