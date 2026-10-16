# Demo Coaching Skill

A Claude Code skill that scores SE demos against a four-criterion scorecard, writes coaching feedback in your voice, produces Gong annotations, and keeps a coaching record per person over time.

## What's in the box

```
demo-coaching/
  SKILL.md                      the workflow Claude follows
  config.example.json           team roster and folder settings
  references/se-demo-scorecard.md   the rubric (edit to match your demo standard)
  scripts/fetch-gong-transcripts.py pulls transcripts from Gong
```

## Install

1. Copy the folder into your skills directory:
   ```
   cp -r demo-coaching ~/.claude/skills/demo-coaching
   ```
2. Create your config:
   ```
   cd ~/.claude/skills/demo-coaching
   cp config.example.json config.json
   ```
   Fill in `team` (name to email, must match Gong user emails). `levels` and `one_on_one_pages` are optional. `transcripts_dir` and `coaching_dir` are relative to wherever you run Claude Code, so point them somewhere you keep notes.
3. Gong API key. In Gong go to Company Settings > Ecosystem > API and create a key. Then either export
   ```
   export GONG_ACCESS_KEY=...
   export GONG_ACCESS_KEY_SECRET=...
   ```
   or run the script once and it will prompt and save `gong_credentials.json` in the skill folder with owner-only permissions. Keep that file out of any repo.

## Use

In Claude Code:

```
/demo-coaching jane
/demo-coaching coach Sam on the Acme demo
/demo-coaching coach the whole team
```

Or paste a transcript and say "score this demo."

Claude lists recent demo calls, you pick one, it scores, writes feedback, and pauses for your confirmation before writing anything to a 1:1 page. The coaching record is always saved locally.

## Fetch transcripts by hand

```
python3 scripts/fetch-gong-transcripts.py --se jane --days 30
python3 scripts/fetch-gong-transcripts.py --id 1234567890   # from the Gong URL
```

The script only lists calls whose title contains a demo-like word (demo, walkthrough, evaluation, solution overview, platform overview). Edit `DEMO_TITLE_TERMS` at the top of the script if your team names calls differently. Any call can be fetched by `--id`.

EU Gong tenants: pass `--base-url https://<your-subdomain>.api.gong.io`.

## Adapting it

- **Scorecard.** `references/se-demo-scorecard.md` encodes one demo standard (research share, Tell-Show-Tell, AI narrative, business value). Rewrite the criteria to match yours. Keep the 1 to 5 scale and the evidence table per criterion so scoring stays consistent across reviewers.
- **Voice.** Step 4 of SKILL.md describes how feedback should read. Add a line or two about your own style if you want it closer to how you write.
- **Team patterns.** Every quarter, average each criterion across your coaching records and write the lowest one or two into the Team Patterns section of SKILL.md. Future sessions then open with the right coaching question.

## Privacy

Scores are for the manager only. The skill never writes numbers into anything the SE can see. Coaching records contain employee feedback, so keep `coaching_dir` and `transcripts_dir` out of shared repos.
