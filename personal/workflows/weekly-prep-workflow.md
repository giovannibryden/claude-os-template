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
- Cross-reference against `team/team-structure.md` - include direct reports and key stakeholders
- Sort by date/time (earliest first)

---

## Step 2: Decision Gate

Before drafting any agendas, identify open decisions that need resolution this week. Scan:
- `meetings/action-items.md` - items flagged as decisions or pending confirmation
- Person briefs (`team/briefs/[name].md`) - "What to Watch" sections with open choices
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

Ask decisions sequentially - one at a time. Only after all decisions are resolved, proceed to Step 3.

---

## Step 3: Run Meeting Prep for Each Person

For each 1:1, run the meeting-prep workflow. Present all agendas together for batch approval rather than one at a time.

---

## Key Principles

1. **Decisions first, agendas second** - walk into every 1:1 with a position, not a question
2. **Batch approval** - show all agendas at once, not one at a time
3. **Development over pipeline** - every agenda defaults development-first
