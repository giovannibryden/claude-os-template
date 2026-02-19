# Advanced Workflows

Once you've used Claude OS for a few weeks, these patterns will help you get even more value.

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
   - Update tracking docs (action-items.md, team-themes.md, etc.)
   - Flag anything urgent
   - Move processed files to `.processed/`

### Pro tip
Don't overthink where things should go. Just dump everything in inbox and let Claude sort it out. You'll save mental energy.

## The "1:1 Prep" Workflow

Get the most out of your 1:1s with minimal prep time.

### Before the meeting
```
You: "Prep me for my 1:1 with [person] today"

Claude:
- Pulls last 2-3 meetings with them
- Surfaces open action items
- Highlights patterns or themes
- Suggests discussion topics
- Notes anything from team-themes.md relevant to them
```

### During the meeting
Take rough notes directly in the 1:1 file. Don't worry about formatting.

### After the meeting
```
You: "I just met with [person]. Here are my rough notes: [paste notes]"

Claude:
- Cleans up and organizes notes
- Extracts action items → meetings/action-items.md
- Updates team-themes.md if new patterns emerge
- Flags anything important
- Suggests follow-ups
```

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

## The "Weekly Review" Workflow

Stay on top of patterns and priorities.

### Friday end-of-week
```
You: "What patterns am I seeing across the team this week?"

Claude:
- Reviews this week's 1:1 notes
- Surfaces common themes (morale, blockers, skill gaps)
- Compares to previous weeks
- Suggests topics for team meeting
```

```
You: "What are my open action items?"

Claude:
- Shows meetings/action-items.md
- Highlights anything overdue
- Suggests priorities for next week
```

```
You: "Update my priorities for next week"

Claude:
- Reviews what you accomplished
- Updates personal/priorities.md
- Carries forward incomplete items
- Suggests new priorities based on recent context
```

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

### For routine messages
1. Create templates in `communications/templates/`
2. When needed: "Use the [template name] template for [situation]"
3. Claude customizes it with current context

### For custom messages
```
You: "Draft an email to the team about [topic]"

Claude:
- Pulls relevant context from strategy docs, recent 1:1s, etc.
- Writes in your voice (learns from communications/sent/)
- Anticipates questions
- Suggests tone adjustments
```

### After sending
Save important communications in `communications/sent/` so Claude learns your voice and can reference them later.

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

## The "Deal Context" Workflow

Stay sharp on your active opportunities.

### Before a customer call
```
You: "Prep me for [customer/deal name]"

Claude:
- Pulls from deals/active/[customer].md
- Summarizes current state
- Notes risks and blockers
- Reminds you of next steps
- Surfaces related 1:1 notes if team members are involved
```

### After a call
Drop notes in inbox, Claude updates the deal file automatically.

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

### Output format
Each review is saved as a markdown file with:
```yaml
---
Direct Report: Jane Doe
Review Period: H2 FY26
Self-Assessment Rating: Exceeding Expectations
Manager Rating: Meeting Expectations
Converted: 2026-02-19
---
```
Followed by the full review content under `## Self-Review` and `## Manager Review` headers.

### After processing
```
You: "Who is missing an H1 FY26 growth cycle review?"

Claude:
- Cross-references processed reviews against your org chart
- Identifies gaps by person and period
- Flags any reviews with missing ratings or incomplete content
```

### Pro tip
The detailed workflow definition lives in `personal/growth-cycle-review-prep-workflow.md`. You can customize the output format, metadata fields, and directory structure there.

## Integration Workflows

### Notion Integration
If you use Notion for 1:1s (recommended for teams already on Notion):
- Claude can read and update your Notion 1:1 docs directly
- Keeps filesystem and Notion in sync
- See `.setup/notion-mcp-setup.md` for configuration

### Google Calendar Integration
If you have meeting transcripts:
- Auto-import from Calendar → `meetings/transcripts/`
- Claude processes and files them
- See `.setup/google-calendar-mcp-setup.md` for configuration

## Power User Tips

### 1. Name files consistently
- 1:1s: `person-name-YYYY-MM-DD.md`
- Candidates: `firstname-lastname.md`
- Meetings: `YYYY-MM-DD-topic.md`

Claude can find things faster with consistent naming.

### 2. Use descriptive file names
Instead of `notes.md`, use `2026-02-13-leadership-offsite-notes.md`. Claude can search by filename.

### 3. Keep priorities.md current
Update this weekly. Claude references it constantly when helping you make decisions.

### 4. Don't over-organize
The inbox workflow exists so you DON'T have to think about organization. Use it liberally.

### 5. Trust the system
It's okay to have messy notes. Claude can parse rough notes better than you think. Focus on capturing information, not formatting it.

## Advanced Queries

Once Claude has enough context, try:

```
"What are the biggest risks to my team right now?"
"Who on my team needs the most attention this month?"
"What am I spending time on that I should delegate?"
"Compare my Q1 priorities to what I'm actually working on"
"What decisions am I avoiding?"
```

Claude will synthesize across all your docs to answer these.

## Customizing the System

### Add new folders as needed
If you find yourself creating files that don't fit anywhere, make a new directory. For example:
- `/projects` - Cross-functional initiatives
- `/customers` - Key account relationship notes
- `/industry` - Market research and competitive intel

Tell Claude about new directories and what they're for.

### Adjust the structure
Don't like the default layout? Change it. Just update CLAUDE.md so Claude knows the new structure.

### Create your own templates
Copy any file to `[directory]/template.md` and Claude will use it as the default for new files in that directory.

## Maintenance

### Monthly
- Review and archive old files from inbox/.processed/
- Check team-themes.md for outdated themes
- Update org-chart.md if team structure changed
- Commit and push to git

### Quarterly
- Archive completed deals to deals/archive/
- Move old strategy docs to strategy/archive/
- Review decision-log.md and note outcomes
- Update hiring/interview-rubric.md based on learnings

### Annually
- Review the whole system structure
- Archive old performance reviews
- Clean up communications/sent/ (keep only important ones)
- Reflect on what worked and what didn't

## Questions or Ideas?

This system evolves based on how you use it. If you develop new patterns or workflows, document them here and share with the community (if using the blessed template repo).
