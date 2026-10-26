# Meeting Prep Workflow

## Interface
**Inputs:** person name (required)
**Outputs:** meeting note with agenda, internal summary for you
**Reads:** see Source Contract
**Writes:** meeting note (Notion page or local file)

When asked to "prep for a 1:1" with someone, follow these steps.

---

## Source Contract

The agenda is what you say to this person, so it may only contain what you have actually seen. The usual failure is an agenda item lifted from a Slack thread, an email, or a Claude-written summary you never read. The other person notices.

**Agenda-eligible (you were in it or decided it):**
- This person's last 3 1:1 notes (Notion or `team/1-1s/`)
- Brief bullets tagged `[1:1 ...]`, `[review ...]`, or `[you]` in `team/briefs/[name].md`
- Decisions you made: `strategy/decision-log.md` and Decision Gate answers from weekly prep
- `team/milestones.md` entries whose `1:1 prompt` applies to this person
- Anything you say in this conversation

**Internal-summary-only (context, not agenda):** `meetings/action-items.md`, `team/team-themes.md`, strategy docs, deal trackers, and brief bullets tagged `[synth]` or untagged. Use them to sharpen a question on an eligible topic. Never let one create a topic. If one looks important enough to raise, put it under "You may not have seen" in the internal summary and let the user decide.

**Never read for prep:** Slack, email, daily-brief output, or anything left in the session from an earlier task. If those are in context, ignore them for this person.

Every agenda topic carries a `Source:` line in the internal summary naming its eligible source. No eligible source, no agenda slot.

---

## Step 1: Gather Context

1. **Brief:** `team/briefs/[name].md`. Primary synthesis. Note each bullet's source tag.
2. **Recent meetings:** the last 3 1:1 notes (Notion or local), for anything since the brief was updated.
3. **Milestones:** active, unexpired entries in `team/milestones.md` relevant to this person.

If the person has no 1:1 page or file mapping in `team/team-structure.md`, ask where to create it. Never put it under another person's page: managers can see everything under theirs.

---

## Step 2: Find Next Meeting Date

Check the calendar for the next scheduled 1:1 with this person (14-day window). If none, say so in the draft and ask for the date.

---

## Step 3: Draft Agenda and Internal Summary

Up to **5 topics**, development first, pipeline last. Structured 1:1s drift toward deal reviews, so pipeline only appears when there's something to escalate.

**For ICs:**
1. Development and coaching follow-ups
2. Open action items from previous 1:1s
3. Relevant milestones (use the milestone's `1:1 prompt`)
4. Projects raised in the last 3 1:1s
5. Deals or projects only if they need your input

**For managers:**
1. Their team's development: who they're coaching, gaps they see
2. Open action items from previous 1:1s
3. Relevant milestones
4. Org and strategic topics they raised or you decided
5. Escalations they brought to you
6. Their own development, quarterly

**Gate:** if a topic is about someone who reports through this manager, skip it unless the manager raised it or it's a skip-level concern.

**Tone:**
- Conversation starters, not directives
- Decisions you already made are stated as positions, not reopened as questions
- Sensitive topics framed as check-ins ("How are you feeling about X?")
- Never in the agenda: scores, ratings, manager assessments, or confidential information about other people or deals

**Internal summary (you only, never shared):**
- Per topic: `Source:` line, context behind it, what to probe
- Sensitive observations to keep in mind
- **You may not have seen:** at most 3 items from internal-summary-only sources that bear on this person, each with its source. Omit if empty.

**Wait for the user to confirm or edit before writing anything.**

---

## Step 4: Create Meeting Note

Create the note (Notion child page under this person's 1:1 page, or `team/1-1s/[name]-[date].md`) with the approved agenda, space for their topics, and an action items section. If the person already added topics, put yours above and never overwrite theirs.

---

## Step 5: Verify

Confirm the note was created under the right parent. If Notion creation failed, write a local backup.

---

## Action items vs agenda topics

Action items are concrete tasks with an owner, a deliverable, and a timeframe ("Sam to send the hiring plan by Wednesday"). Agenda topics are conversation starters ("Discuss career development"). Never convert one into the other. Only carry over action items still open from previous 1:1s.
