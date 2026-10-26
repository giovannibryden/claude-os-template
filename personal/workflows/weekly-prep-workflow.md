# Weekly Prep Workflow

## Interface
**Inputs:** none (reads next week's calendar automatically)
**Outputs:** meeting notes/agendas for all next week's 1:1s
**Reads:** Calendar (next week), team/team-structure.md, meetings/action-items.md, team/milestones.md
**Writes:** Meeting notes (via meeting-prep workflow)

When asked to "prep for next week" or "weekly prep", run meeting prep for every 1:1 scheduled next week, with a decision gate first.

---

## Step 1: Load Next Week's 1:1s

Query calendar for next Monday through Sunday.
- Exclude all-day events and events marked "Free" or "Out of Office"
- Include only 1:1 meetings (2 attendees max, or title contains "1:1")
- Build the list from `team/team-structure.md` first, then overlay the calendar for times. Direct reports are always prepped, even if a slot was declined or isn't booked; note the status and prep anyway
- Sort by date/time (earliest first)

---

## Step 2: Decision Gate

Before drafting any agendas, identify open decisions that need resolution this week. Only raise decisions that came out of a meeting you were in or that you asked for:
- `meetings/action-items.md` - items flagged as decisions or pending confirmation
- Person briefs (`team/briefs/[name].md`) - open choices in "What to Watch" tagged `[1:1 ...]` or `[you]`
- `team/milestones.md` - milestones with status 🔴 Blocked or 📅 Upcoming with dates in the coming week

For each decision, present it and **wait for a response before presenting the next one**:

```
**Decision [N of N]: [Short title]**

**Context:** [Why this is on the table now - 1-2 sentences]

**My recommendation:** [Specific, opinionated call]

**Rationale:** [Why this is the right call]

**Pros:** [Upside of the recommendation]
**Cons / risks:** [What we give up or risk]

Confirm this recommendation, or tell me your call.
```

Do not raise a decision whose only source is Slack, email, or a `[synth]` bullet. If one looks real, list it in one line after the gate as "Possible, unverified."

Ask decisions sequentially - one at a time. Only after all decisions are resolved, proceed to Step 3.

---

## Step 3: Run Meeting Prep for Each Person

Spawn **one subagent per person, all in a single message so they run in parallel**. Each starts with a clean context, so one person's material can't bleed into another's agenda and nothing from earlier in the session (a daily brief, Slack reads) leaks in.

Give each subagent the person's name, meeting date/status, and the Decision Gate answers that concern them, with this instruction: "Run `personal/workflows/meeting-prep-workflow.md` Steps 1-3 for [name], following its Source Contract exactly. Don't create the note. Return the agenda and the internal summary with a Source line per topic."

Drop any returned topic without an eligible Source line. Present all agendas together for batch approval, then create the notes (Step 4 of meeting prep) in the main session.

---

## Key Principles

1. **Decisions first, agendas second** - walk into every 1:1 with a position, not a question
2. **Batch approval** - show all agendas at once, not one at a time
3. **Development over pipeline** - every agenda defaults development-first
4. **One clean context per person** - isolation stops cross-person bleed and stale session context
