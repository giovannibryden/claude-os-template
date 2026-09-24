# Advanced Workflows

Once you've used Claude OS for a few weeks, these patterns will help you get even more value.

## Workflow Dependency Chain

The workflows in `personal/workflows/` form a connected system. Understanding how they chain together helps you get the most out of them:

```
Process Week
  ├── Pulls meeting notes (Notion or local)
  ├── Files them as 1:1s, meetings, hiring notes
  ├── Updates action-items.md, team-themes.md, milestones.md
  ├── Generates week-summary.md
  └── Triggers Update Briefs (refreshes person briefs)

Weekly Prep
  ├── Scans next week's calendar for 1:1s
  ├── Runs Decision Gate (resolve open decisions first)
  └── Runs Meeting Prep for each person
        ├── Reads person brief (primary context)
        ├── Reads last 3 meeting notes
        ├── Reads milestones.md
        └── Creates agenda (Notion or local)
```

The **person brief** (`team/briefs/[name].md`) is the central node. It synthesizes 1:1 notes, performance records, themes, and action items into one file. Meeting prep reads the brief instead of re-scanning 6+ files.

Full details: `personal/workflows-index.md`

---

## The "Process Inbox" Workflow

This is your most powerful tool for staying organized.

### When to use it
- After any meeting with notes/transcript
- End of day brain dump
- When you have a batch of emails or documents to file
- Weekly cleanup

### How it works
1. Drop files into `inbox/` (any format: .txt, .md, .pdf, .docx, screenshots)
2. Tell Claude: "process inbox"
3. Claude will:
   - Read everything
   - Identify what's important
   - File items in appropriate directories
   - Update tracking docs (action-items.md, team-themes.md, milestones.md, etc.)
   - Flag anything urgent
   - Move processed files to `.processed/`

### Pro tip
Don't overthink where things should go. Just dump everything in inbox and let Claude sort it out. You'll save mental energy.

## The "Process Week" Workflow

Batch-process an entire week's meetings at once.

### When to use it
- Mid-week or end of week, once most meetings have happened
- When you've fallen behind on filing meeting notes

### How it works
```
You: "Process this week's meetings"

Claude:
- Pulls all meeting notes from the week (Notion AI notes or local files)
- Cross-references against your calendar
- Categorizes each meeting (1:1, stakeholder, hiring, group)
- Shows you the categorization and waits for approval
- Creates files in the right directories
- Extracts and files action items
- Updates team themes and milestones
- Generates a week summary
- Updates person briefs for each direct report discussed
```

### Pro tip
The week summary (`meetings/week-summary-[date].md`) is what downstream workflows reference. Keep it actionable.

Detailed workflow: `personal/workflows/process-week-workflow.md`

## The "1:1 Prep" Workflow

Get the most out of your 1:1s with minimal prep time.

### Before the meeting
```
You: "Prep me for my 1:1 with [person] today"

Claude:
- Loads their person brief (primary context source)
- Checks last 3 meeting notes for anything since the brief was updated
- Checks milestones.md for relevant team-wide deadlines
- Suggests top 5 agenda topics (development first, pipeline last)
- Produces an internal-only summary with sensitive context
- Creates the meeting note (Notion or local) after you approve
```

### Key design choice: development first
Structured 1:1s naturally default to deal/pipeline reviews. This workflow fights that by ordering topics development-first. Pipeline only appears when there's something to escalate.

### During the meeting
Take rough notes directly in the 1:1 file. Don't worry about formatting.

### After the meeting
```
You: "I just met with [person]. Here are my rough notes: [paste notes]"

Claude:
- Cleans up and organizes notes
- Extracts action items -> meetings/action-items.md
- Updates team-themes.md if new patterns emerge
- Flags anything important
- Suggests follow-ups
```

Detailed workflow: `personal/workflows/meeting-prep-workflow.md`

## The "Update Briefs" Workflow

Keep person briefs current so meeting prep stays fast.

### When to use it
- After processing a week's meetings
- Before a performance review cycle
- Anytime you want a refreshed picture of someone

### How it works
```
You: "Update briefs" or "Update [name]'s brief"

Claude:
- Reads last 4 1:1 notes, last 3 coaching/performance records, latest review
- Cross-references team-themes.md and action-items.md
- Synthesizes into judgment (not recap) - what matters, what to watch
- Overwrites the existing brief (briefs are living state, not logs)
```

### Key insight: "What to Watch" is the payoff
The brief's most important section requires holding multiple sources in mind at once. It names the risk, opportunity, or open thread for the next 1:1. Meeting prep can't derive this without the brief.

Detailed workflow: `personal/workflows/update-briefs-workflow.md`

## The "Weekly Prep" Workflow

Batch-prep all next week's 1:1s with a decision gate.

### When to use it
- End of week, to walk into Monday ready
- Before a heavy week of meetings

### How it works
```
You: "Prep for next week"

Claude:
1. Loads next week's 1:1s from your calendar
2. Decision Gate: identifies open decisions from action items,
   briefs, and milestones. Presents each one with a recommendation.
   You resolve each before agendas get drafted.
3. Runs meeting prep for each person
4. Presents all agendas together for batch approval
```

### Key design choice: decisions first, agendas second
The Decision Gate ensures you walk into every 1:1 with a position, not a question. Resolved decisions become agenda items framed as positions ("Here's where I'm landing") rather than open questions ("Where do we land on this?").

Detailed workflow: `personal/workflows/weekly-prep-workflow.md`

## The "Candidate Evaluation" Workflow

Make faster, better hiring decisions.

### After each interview
1. Drop interview notes or transcript in `inbox/`
2. Tell Claude to process it
3. Claude creates/updates the candidate file in `hiring/candidates/`

### When making the decision
```
You: "Should we move forward with [candidate name]?"

Claude:
- Reviews all interview feedback
- Compares against your hiring rubric
- Flags strengths and concerns
- Compares to other candidates for the role
- Gives you a clear recommendation
```

### Pro tip
Create `hiring/interview-rubric.md` with your evaluation criteria. Claude will reference it automatically when assessing candidates.

## The "Decision Logging" Workflow

Learn from your choices over time.

### When making a significant decision
```
You: "I decided to [decision]. Here's my reasoning: [context]"

Claude:
- Adds entry to strategy/decision-log.md
- Captures: decision, reasoning, tradeoffs, expected outcome
- Links to relevant documents
```

### Months later
```
You: "What was my reasoning for [past decision]?"

Claude:
- Pulls from decision-log.md
- Shows original context
- Notes actual outcome vs. expected
- Helps you learn from the pattern
```

### Pro tip
This is especially valuable for hiring decisions, org changes, and strategy pivots. Your future self will thank you.

## The "Communication Drafting" Workflow

Write faster in your voice.

### Setup
Fill in `communications/writing-style-guide.md` with your preferences and examples. Claude will reference this for all drafting.

### For routine messages
1. Check `communications/templates/` for starting points
2. When needed: "Use the [template name] template for [situation]"
3. Claude customizes it with current context

### For custom messages
```
You: "Draft an email to the team about [topic]"

Claude:
- Pulls relevant context from strategy docs, recent 1:1s, etc.
- Writes in your voice (references writing-style-guide.md)
- Anticipates questions
- Suggests tone adjustments
```

### After sending
Save important communications in `communications/sent/` so Claude can reference them later.

## The "Theme Tracking" Workflow

Spot patterns before they become problems.

### As you take notes
Don't worry about identifying themes yourself. Just capture raw information.

### Let Claude surface patterns
```
You: "What themes am I seeing in 1:1s this month?"

Claude:
- Reviews all recent 1:1s
- Identifies common topics (technical debt, unclear priorities, workload, etc.)
- Shows which team members mentioned each theme
- Updates team/team-themes.md
- Suggests actions
```

### Act on themes
When a theme appears 3+ times, it's worth addressing:
- In a team meeting
- In strategy docs
- With individual coaching

## The "Performance Review Processing" Workflow

Convert performance review PDFs into structured, searchable markdown.

### When to use it
- At the start of a review cycle, to have past reviews on hand
- When you inherit a new team and receive historical reviews
- After reviews are finalized, to archive them in a structured format

### How it works
1. Drop performance review PDFs into `inbox/`
2. Tell Claude: "process inbox and prep growth cycle reviews"
3. Claude will:
   - Read each PDF and identify the direct report and review period
   - Extract self-assessment and manager ratings
   - Convert the full content to markdown with YAML metadata
   - Save to `growth-cycle-reviews/[Name]/[Period]_growth_cycle_review.md`
   - Output a summary table with all ratings

### Pro tip
The detailed workflow definition lives in `personal/workflows/growth-cycle-review-prep-workflow.md`. You can customize the output format, metadata fields, and directory structure there.

## Integration Workflows

### Notion Integration
If you use Notion for 1:1s (recommended for teams already on Notion):
- Claude can read and update your Notion 1:1 docs directly
- Keeps filesystem and Notion in sync
- See `.setup/notion-mcp-setup.md` for configuration

### Google Calendar Integration
If you have meeting transcripts:
- Auto-import from Calendar
- Claude processes and files them
- See `.setup/google-calendar-mcp-setup.md` for configuration

## Power User Tips

### 1. Name files consistently
- 1:1s: `person-name-YYYY-MM-DD.md`
- Candidates: `firstname-lastname.md`
- Meetings: `topic-YYYY-MM-DD.md`

Claude can find things faster with consistent naming.

### 2. Keep priorities.md current
Update this weekly. Claude references it constantly when helping you make decisions.

### 3. Don't over-organize
The inbox workflow exists so you DON'T have to think about organization. Use it liberally.

### 4. Trust the system
It's okay to have messy notes. Claude can parse rough notes better than you think. Focus on capturing information, not formatting it.

## Advanced Queries

Once Claude has enough context, try:

```
"What are the biggest risks to my team right now?"
"Who on my team needs the most attention this month?"
"What am I spending time on that I should delegate?"
"Compare my Q1 priorities to what I'm actually working on"
"What decisions am I avoiding?"
"What am I missing this week that's important?"
```

Claude will synthesize across all your docs to answer these.

## Maintenance

### Monthly
- Prune action-items.md (keep it under ~120 lines)
- Check team-themes.md for outdated themes
- Archive expired milestones
- Update team-structure.md if team changed
- Commit and push to git

### Quarterly
- Archive completed deals to deals/archive/
- Move old strategy docs to strategy/archive/
- Review decision-log.md and note outcomes
- Update hiring/interview-rubric.md based on learnings

### Annually
- Review the whole system structure
- Archive old performance reviews
- Clean up communications/sent/
- Reflect on what worked and what didn't
