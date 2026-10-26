# Write Growth Cycle Review Workflow

## Interface
**Inputs:** review input sheet (CSV) + review template (PDF with the cycle's questions) in `inbox/`
**Outputs:** `growth-cycle-reviews/[First_Last]/[Cycle]_growth_cycle_review.md` per person
**Reads:** inbox inputs, the files `bin/gc-sources.py` lists, the current self-review, `communications/writing-style-guide.md`
**Writes:** `growth-cycle-reviews/[First_Last]/[Cycle]_growth_cycle_review.md`

The same rules apply to growth-conversation prep and handoff docs built from a review.

---

## How evidence is controlled

The two classic review errors both come from evidence the writer should never see:
- **Stale wins:** last cycle's self-review (often filed with the manager section still pending) gets read as this cycle's input, and old projects and awards get credited again.
- **Inflated facts:** a Claude-written roll-up upgrades a loose note ("attempted") into a fact ("second attempt"), and the review trusts the roll-up.

Rules alone don't stop either, so the writer never sees those files:
- `bin/gc-sources.py [First_Last] "[Cycle]"` is the only source list. It sets the window by Review Period label (after the last prior review's date, through today) and lists in-window 1:1s and the person's own `demo-*` coaching records. Prior reviews, briefs, team-themes, action items, and roll-ups are never on it.
- Prior reviews go to a separate subagent that returns only your prior view. No examples, projects, awards, or numbers come back.
- Each writer subagent reads only its person's evidence list, the current self-review, the input row, and the style guide.
- `bin/gc-sources.py ... --check [draft]` fails if the claims table cites any file outside the list.

Adjust the glob patterns in `bin/gc-sources.py` if your 1:1 or coaching files are named differently.

---

## Step 1: Inputs

From `inbox/`:
1. **Input sheet:** per person - name, level, rating, 2 strengths with examples, 2 growth areas with suggested actions. If a field is empty, stop and say which. Never invent a strength or growth area.
2. **Review template:** the questions and the cycle label.

For each person:
- Run `bin/gc-sources.py [First_Last] "[Cycle]"`. Flag anyone with no prior review or an empty evidence list.
- Get the **current cycle's** self-review (review tool or inbox) and check its period label matches. If none, skip alignment language.
- If you use 1:1 notes from Notion, save them to `team/1-1s/` first so `--check` can see them.

---

## Step 2: Prior View (one subagent per person with prior reviews)

Prompt: "Read only these files: [prior review paths]. From the manager review sections, return: (1) the growth areas named in the most recent review, verbatim; (2) what was expected in the next 6 months; (3) strengths or weaknesses recurring across two or more reviews, with their cycles. Return no examples, projects, awards, numbers, or self-review content."

---

## Step 3: Write (one subagent per person, all launched in one message)

Give each: their input row, the review questions, the Step 2 output, the current self-review (or "none"), and their evidence list. Instruct: "Read only the files on your evidence list and `communications/writing-style-guide.md`. Follow the Questions, Factual claims, and Voice rules in `personal/workflows/write-growth-cycle-review-workflow.md`. Return the draft and a claims table: claim | source file:line | Verified (source states it outright) or Inferred. Inferred rows first."

### Questions (adapt to your template)

- **Strengths:** exactly the ones from the input sheet. Per strength: what they did (behavioral, from evidence), the impact, and self-review alignment where it's real. This half only.
- **Growth areas:** exactly the ones from the sheet. The gap in one sentence, what closing it unlocks, then the suggested action. No hedging.
- **Values/culture:** 1-2 company values, each with an in-window example.
- **Summary:** rating signal, the most important thing this half, what you'll watch next half. Check your prior expectations against this half. Name cross-cycle patterns as patterns, with this cycle's evidence in-window.
- **Rating:** map from the input sheet to your review tool's labels.

### Factual claims

- Every score, date, count, rank, or sequence ("second attempt", "improved between X and Y") must be stated outright in a source line. Quote numbers exactly.
- No inferred sequences. An ungraded practice run is called a practice run.
- Loose wording stays loose. If ambiguous, mark it Inferred.
- A claim with no source gets cut, not softened.

### Voice

Per the style guide. Keep it generic: no customer, prospect, or partner names. Describe the behavior and the pattern. Never reveal sources: no tags, no file names, and no "in a meeting with X" or "others have raised". Every observation reads as your own. The claims table is for you only and never goes in the review file or your review tool.

---

## Step 4: Verify, Present, Save (main session, one person at a time)

1. Save the draft with its claims table to a scratch file and run `bin/gc-sources.py [First_Last] "[Cycle]" --check [file]`. If it fails, send the draft back with the failing paths or cut those claims.
2. Show the draft and claims table. Every Inferred row needs your confirmation or gets cut.
3. Before saving, write the review text alone (no claims table) to a scratch file and run `grep -nE '\[(1:1|mtg|review|you|synth)[ \]]|Source:|\.md' <file>`. Any hit blocks the save.
4. On approval, save with frontmatter `Direct Report`, `Review Period`, `Manager Rating`, and `Written: [today]`. The `Written` date opens next cycle's window.
5. When everyone is done, move inbox files to `inbox/.processed/`.
