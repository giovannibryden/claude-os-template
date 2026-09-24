# Meeting Prep Workflow

## Interface
**Inputs:** person name (required)
**Outputs:** meeting note with agenda
**Reads:** team/briefs/[name].md (primary), team/team-structure.md, recent 1:1 notes, calendar
**Writes:** meeting note (Notion page or local file)

When asked to "prep for a 1:1" with someone, follow these steps.

---

## Step 1: Gather Context

**Load the person brief first.** Check `team/briefs/[name].md` - this is your primary context source for themes, development areas, coaching history, open action items, and what to watch. You do not need to re-derive what the brief already tells you.

**Then check recent meetings.** Fetch the last 3 meeting notes (from Notion or local files) to catch anything since the brief was last updated.

**Then check team milestones.** Read `team/milestones.md` for any active milestones relevant to this person's role or current work.

---

## Step 2: Find Next Meeting Date

Check the calendar for the next scheduled 1:1 with this person (14-day window).

If no 1:1 is found, note it in the agenda draft and ask the user for the date.

---

## Step 3: Suggest Agenda & Confirm

Present the **top 5 discussion topics** to the user. The agenda is a conversation guide for a direct report - keep it high-level, warm, and non-directive. Sensitive context (performance concerns, manager assessments, confidential information) must never appear in the agenda or anything shared with the direct report.

### Priority Order - Development First

Agenda topics are ordered development-first, pipeline-last. Structured 1:1s naturally default to deal/pipeline reviews rather than development conversations. The fix is structural - pipeline only appears when there's something to escalate.

**For ICs:**
1. **Development and coaching follow-ups** (highest priority) - skill gaps, growth goals, career trajectory
2. **Open action items from previous meetings**
3. **Active team milestones** relevant to this person (use the milestone's `1:1 prompt`)
4. **Themes from `team-themes.md`** related to this person
5. **Recent project mentions** in last 3 meetings
6. **Deal/project updates - only if escalation-worthy** - do not default to pipeline review

**For managers:**
1. **Their team's development** (highest priority) - who they're coaching, gaps they're seeing
2. **Open action items from previous meetings**
3. **Active team milestones** relevant to their region/team
4. **Org/strategic topics** - coverage model, hiring, cross-functional alignment
5. **Escalations from their team** - deals or situations needing your input
6. **Their own development** - quarterly cadence

### Agenda tone rules
- Topics should read as conversation starters, not directives
- No specific performance ratings, manager assessments, or sensitive observations
- No confidential information about other team members or deals
- Sensitive topics framed as check-ins ("How are you feeling about X?")
- Decisions from the weekly prep decision gate become positions, not questions

### Before presenting

Produce a **separate internal summary** for the user only (not shared with the direct report) that includes:
- Detailed context behind each agenda topic
- Sensitive observations or themes to keep in mind
- Specific things to watch for or probe on

**Wait for the user to confirm or modify the agenda before proceeding.**

---

## Step 4: Create Meeting Note

Create the meeting note (Notion child page or local markdown file at `team/1-1s/[name]-[date].md`) with:
- Approved agenda items
- Space for their topics
- Action items section
- Follow-up section

---

## Step 5: Verify

Confirm the meeting note was created. If Notion creation failed, create a local markdown backup to ensure prep work isn't lost.

---

## Key Principles

1. **Briefs are primary context** - don't re-derive what the brief already tells you
2. **Agenda stays high-level** - the direct report sees this; keep it warm and open-ended
3. **Internal summary stays internal** - sensitive themes never go in the shared note
4. **Development first, pipeline last** - structured 1:1s default to deal reviews; fight that
5. **Approval before writing** - always present topics before creating the note
6. **Action items ≠ agenda topics** - action items are concrete tasks; agenda topics are conversation starters
