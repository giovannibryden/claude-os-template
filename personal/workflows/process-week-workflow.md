# Process Week Workflow

## Interface
**Inputs:** date range (optional - defaults to current week)
**Outputs:** week summary, updated action-items.md, updated team-themes.md, new 1:1/meeting files
**Reads:** team/team-structure.md, team-themes.md, action-items.md (from Notion or local sources)
**Writes:** team/1-1s/, meetings/, action-items.md, team-themes.md, milestones.md, week-summary.md
**Triggers:** update-briefs after Step 7 for any person whose 1:1 was processed

When asked to "process my meetings for the week", "process this week", or similar, pull meeting notes, file them in the right places, and generate a week summary.

---

## Step 1: Pull Meeting Notes

Search for meeting notes from the target week. If using Notion, search for AI-generated meeting notes. If working locally, scan inbox/ or meetings/ for new files.

Cross-reference against the calendar. Any calendar event with no matching notes gets flagged as "No notes available" - not silently dropped.

Present a summary table:

| # | Title | Date | Status |
|---|---|---|---|
| 1 | 1:1 with [Name] | [Date] | Notes found |
| 2 | Team sync | [Date] | No notes |

If no meeting notes are found, flag this before proceeding.

---

## Step 2: Fetch Full Content

For each meeting with notes, retrieve the full content:
- AI summary or meeting notes
- Action items
- Key topics discussed
- Attendee list

Skip meetings with no substantive content (blocked calendar holds, brief touch-points with no notes).

---

## Step 3: Categorize

Read `team/team-structure.md`. Match each meeting to a category based on attendees and title:

| Category | Routing |
|----------|---------|
| Direct report 1:1 | `team/1-1s/[name]-[date].md` |
| Stakeholder 1:1 | `meetings/[name]-[date].md` |
| Hiring interview | `hiring/candidates/[name].md` (append) |
| Group / team meeting | `meetings/[topic]-[date].md` |
| Cross-functional | `meetings/[name]-[date].md` |

Present the categorized list and **wait for confirmation before writing anything.**

---

## Step 4: Create Files

After confirmation, create files for each meeting using the appropriate template. **Never overwrite an existing file - skip if one already exists for this person + date.**

### Direct report 1:1s → `team/1-1s/[name]-[date].md`
### Stakeholder / cross-functional → `meetings/[name-or-topic]-[date].md`
### Hiring interviews → `hiring/candidates/[name].md` (append if exists)

---

## Step 5: Extract Action Items

From all meeting notes, extract action items and add to `meetings/action-items.md`:

1. **Update the "Open Items by Person" section** - add new items under the relevant person's name
2. **Append to the dated log** - under a new "### Added [date]" heading

Rules:
- Deduplicate: don't add items that already exist
- Mark owner clearly: "You" for your items, person's name for theirs
- Flag urgent items with **URGENT** or **CRITICAL**
- Items without a clear due date get "This week" as default

---

## Step 6: Update Team Themes

Read `team/team-themes.md`. For each active theme, check if this week's meetings added new signal.

For new patterns that appear across 2+ separate meetings, add a new theme entry.

**Only update if there is genuine new signal.** Don't restate what's already documented.

---

## Step 6b: Update Milestones

Read `team/milestones.md`:
- Update status if this week's meetings provided new signal
- Move expired milestones (expiry date < today) to Archived section
- Add new milestones surfaced this week (default expiry: 30 days)

---

## Step 7: Generate Week Summary

Create `meetings/week-summary-[date].md`:

```markdown
# Week Summary: [Date Range]

**Meetings processed:** [N]

## By Category
- Direct report 1:1s: [N]
- Stakeholder 1:1s: [N]
- Hiring: [N]
- Group / project syncs: [N]

## Key Insights

### People & Team
[Patterns across 1:1s - morale, performance signals, development milestones]

### Deals & Pipeline
[Deal updates, pipeline signals surfaced in meetings]

### Projects & Priorities
[Project status updates, priority shifts]

### Hiring
[Candidate pipeline, decisions pending]

## Action Items Added
[Count added to action-items.md, plus any CRITICAL or URGENT items]

## Team Themes Updated
[Which entries were touched and why]

## Files Created This Run
[Bulleted list of every file created or modified]

## What Downstream Workflows Should Know
[Specific notes for meeting-prep and weekly-prep workflows]
```

---

## Phase 2: Post-Processing

Run update-briefs for each direct report whose 1:1 was processed. If no direct report 1:1s were processed, skip this step.

---

## Key Principles

1. **Show before writing** - always present categorization and wait for "proceed"
2. **Additive only** - never overwrite existing files
3. **Source every action item** - every item traces back to its meeting
4. **Flag what's missing** - meetings without notes get called out explicitly
5. **The week summary is the handoff** - it's the connective tissue for every other workflow
6. **Briefs stay current** - update-briefs at the end ensures meeting prep has fresh context
