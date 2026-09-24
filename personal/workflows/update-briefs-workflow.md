# Update Briefs Workflow

## Interface
**Inputs:** person name (optional - if omitted, updates all active direct reports)
**Outputs:** updated team/briefs/[name].md files
**Reads:** team/1-1s/, team/performance/, growth-cycle-reviews/, team-themes.md, action-items.md
**Writes:** team/briefs/[name].md

When asked to "update briefs" or after process-week completes, refresh person briefs. These are the primary context source for meeting prep - they replace the need to scan multiple files before each 1:1.

---

## Step 1: Determine Scope

- If a specific person was named, update only their brief
- If called after process-week, update briefs for all people whose 1:1 was processed
- If standalone with no arguments, update all active direct reports

---

## Step 2: Gather Sources

For each person, read in order:

1. **team/team-structure.md** - confirm role, level, region, tenure
2. **team/briefs/[name].md** - current brief (if exists), to diff against
3. **team/1-1s/[name]-*.md** - last 4 notes, sorted newest first
4. **team/performance/** - last 3 coaching or performance records
5. **growth-cycle-reviews/** - most recent review
6. **team/team-themes.md** - entries mentioning this person
7. **meetings/action-items.md** - items where this person is the named owner

---

## Step 3: Synthesize

Write a brief, not a summary. The value is analyst's judgment - what matters, what to watch, what's changed. Not a factual recap of what happened.

Use the brief template from `team/briefs/template.md`.

**"What to Watch" is the payoff** - this section requires holding multiple sources in mind and is what meeting prep can't easily derive without the brief. Be direct. Don't hedge.

---

## Step 4: Save

Write to `team/briefs/[name].md`. Overwrite the existing file - briefs are living documents, not logs. History lives in the source files.

After saving all briefs, report: "[N] briefs updated: [list of names]."

---

## Key Principles

1. **Judgment, not recaps** - anyone can read the 1:1 notes; the brief tells you what they mean
2. **Current Focus should reflect today** - stale briefs are worse than no briefs
3. **What to Watch is the payoff** - this requires synthesis across sources
4. **Overwrite, don't append** - briefs are refreshed state
5. **Run after every process-week** - keeps meeting prep fast (2 minutes instead of 10)
