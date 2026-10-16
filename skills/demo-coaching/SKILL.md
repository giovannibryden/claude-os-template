---
name: demo-coaching
description: Use when asked to coach someone on a demo, score a demo transcript, provide demo coaching, or fetch a demo transcript from Gong. Scores the demo against the SE Demo Scorecard, writes coaching feedback, and saves a coaching record.
---

# Demo Coaching

Score a sales engineering demo against the four-criterion scorecard, write balanced coaching feedback, and save a record. Run end to end, pausing only where this file says to confirm with the user.

**Files in this skill:**
- `references/se-demo-scorecard.md` - the rubric. Read it before scoring.
- `scripts/fetch-gong-transcripts.py` - pulls transcripts from Gong.
- `config.json` - team roster, output folders, optional 1:1 page mapping. Copy from `config.example.json`.

---

## Step 1: Get the transcript

**If the user pasted a transcript:** use it.

**If the user named a person:** resolve them with `config.json` (`team` maps names to emails) and run from the skill directory:

```
python3 scripts/fetch-gong-transcripts.py --se <name or email> --days 30
```

The script prints a numbered list of demo calls. Show the list and ask which call to coach (number, or "none" to paste manually). Then:

```
python3 scripts/fetch-gong-transcripts.py --id <call_id>
```

The transcript lands in the `transcripts_dir` from config as a `.txt` with a `.json` sidecar. Read the `.txt` and continue.

If nothing is found, widen to `--days 90` once before asking the user. The script filters on demo-like titles only, so a call titled differently can always be fetched by `--id` from its Gong URL.

**If the user says "coach the whole team":** run the script with no `--se` flag, take each person's most recent demo, and run Steps 2 to 6 per person. Still pause for confirmation per person before writing anything. Skip anyone with no calls and say so at the end.

---

## Step 2: Identify SE, AE, prospect, date

From the transcript, extract:
- The SE (running the product demo)
- The AE, if present (intro, context, value slides)
- The prospect company
- The date: filename first, then an explicit date in the transcript, then inference, then ask
- The SE's level, if `config.json` lists one under `team`

If it is unclear who the SE is, ask before scoring.

**Score only the SE's contribution.** If the AE did the research share or asked the value questions, the SE does not get credit for it. Note "(AE handled X)" in the evidence column.

---

## Step 3: Score

Read `references/se-demo-scorecard.md`. Score each criterion 1 to 5 with one short evidence sentence (under about 80 characters). Detailed evidence goes in Step 4, not the table.

Output this context block, then the table:

```
**Company:** [prospect] | **Stage:** [discovery / evaluation / POC] | **AE:** [name or "none"]
**SE:** [name] ([level if known]) | **Key topics:** [list] | **Outcome:** [next steps from the call]
**Date:** [date or "inferred from X"]
```

```
## Demo Scorecard - [SE] / [Prospect] - [Date]

| Criterion | Score | Evidence |
|---|---|---|
| Tailoring & Preparation | X/5 | ... |
| Narrative & Structure | X/5 | ... *(scored from transcript only - slides not visible)* |
| AI Narrative | X/5 | ... |
| Business Value | X/5 | ... |
| **Total** | **X/20** | [band from the scorecard] |
```

Two calibration notes:
- Narrative & Structure is scored from transcript only. Anchor slides are invisible, so if the SE used them the real score may be higher. Say so.
- Calibrate to level. A 3 from a senior SE is a coaching conversation. A 3 from a new hire may be fine. Say which applies.

---

## Step 4: Coaching feedback

Take the two highest-scoring criteria as strengths and the two lowest as development areas. Always two and two.

Write directly to the SE in second person, in the voice of their manager:
- Direct and warm. Not a performance review, not corporate filler.
- Short paragraphs. Every point cites a specific moment from the transcript.
- Single hyphens for clause breaks, no em dashes.
- No AI tells: no "Furthermore", no perfectly parallel sentences, no "not X but Y" reframes.
- Name the gap plainly, then ask an open question. Questions invite reflection, they do not lead.

```
## Coaching Feedback - [SE]

### What went well

1. **[Criterion]** - [What they did, where, and why it worked.]
2. **[Criterion]** - [Same.]

### Areas to develop

1. **[Criterion]** - [What was missing or inconsistent, grounded in the transcript.]
   - *Coaching question:* "[Open question for the 1:1]"
2. **[Criterion]** - [Same.]
   - *Coaching question:* "[Open question for the 1:1]"
```

Two questions that reliably open the right conversation:
- AI Narrative below 3: "Where did you plan for AI to show up - did it have a home, or did it depend on the prospect asking?"
- Business Value below 3: "After each section, what was the one sentence that named the business outcome?"

**Show the scorecard and feedback, then wait for confirmation before Step 4b.**

---

## Step 4b: Gong annotations (Gong transcripts only)

Only if a `.json` sidecar exists next to the `.txt`. For each of the four coaching moments:
1. Pick a distinctive phrase from the transcript that the feedback references.
2. Find it in the sidecar's `transcript` array.
3. Convert `start` to `MM:SS`. **`start` is milliseconds:** `s = start // 1000`, then `s // 60 : s % 60`. Never use the timestamps printed in the `.txt`.
4. No exact match: use the nearest segment on that topic.

Append:

```
---

## Gong Annotations - ready to paste

Call review: [call_review_page_url from sidecar]

⭐ [MM:SS] - [one-sentence positive, addressed to the SE]
⭐ [MM:SS] - [one-sentence positive]
🔧 [MM:SS] - [one-sentence coaching note, phrased as an observation]
🔧 [MM:SS] - [one-sentence coaching note]
```

Skip this step for pasted transcripts.

---

## Step 5: Add to the next 1:1

**Scores never leave this machine.** No totals, no per-criterion numbers in anything the SE can see: no 1:1 agendas, no Notion, no Slack. Scores live in the coaching record only. The agenda item carries observations and questions.

Agenda item format:

```
- **Demo coaching** - [Prospect], [demo date]
  - Went well: [two things, briefly]
  - To discuss: [the two coaching questions]
```

If `config.json` has a `one_on_one_pages` entry for the SE and you have a Notion (or equivalent) tool: fetch the page, find a meeting note dated **strictly after today**, and append the item to its agenda. Never write into a past meeting note. Never write to another person's page. If there is no mapping for the SE, ask where it should go; do not guess.

If there is no future page or no mapping: save the agenda item to `[coaching_dir]/agenda-[firstname-lastname]-[YYYY-MM-DD].md` and tell the user it is waiting for the next 1:1 prep.

Show the agenda text and get a yes before writing anywhere external.

---

## Step 6: Save the coaching record

Always, regardless of Step 5:

```
[coaching_dir]/[firstname-lastname]-demo-coaching-[YYYY-MM-DD].md
```

```markdown
# Demo Coaching - [SE]
**Date of demo:** [date]
**Prospect:** [company]
**Scored by:** [manager]

[scorecard table]

[coaching feedback]

[Gong annotations, if any]

## Notes
[anything else worth remembering]
```

The date in the filename is the demo date. This folder is the historical record for growth cycle reviews and promotion cases, and the input for spotting team-wide patterns.

---

## Team patterns

Review the coaching records quarterly. Average each criterion across the team, name the one or two lowest, and write the finding here so future sessions open with the right question. Replace this paragraph with the current findings and a date.

---

## Principles

1. **Evidence-based.** Every score and every line of feedback points at a moment in the transcript.
2. **Two and two.** Strengths before development areas, always.
3. **Questions, not verdicts.** Development areas end in an open question.
4. **Proportional to level.** Expectations scale with seniority.
5. **Confirm before writing externally.** Show the text, wait for yes.
6. **Scores stay private.** Internal measurement only.
