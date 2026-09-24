# Claude OS - System Guide

This is your personal operating system. Everything in this directory exists to help you be a world-class leader.

## Structure

### `/team`
Your people. This is your most important asset.

- **1-1s/**: Individual conversation notes with each team member. Name files by person and date (e.g., `sarah-2026-02-05.md`). Keep these informal - they're for you, not HR.
- **briefs/**: Person briefs - the **primary context source** for meeting prep. Each brief synthesizes 1:1 notes, performance records, themes, and action items into a single file per person. Updated after every process-week run. See `team/briefs/template.md` for the format.
- **performance/**: Performance reviews, coaching records, feedback prep, development plans.
- **team-structure.md**: Current team structure - who reports to whom, regional breakdown, and Notion 1:1 page mappings (if using Notion). This is the source of truth for all workflows.
- **team-themes.md**: Running log of patterns you're seeing across the team - morale issues, skill gaps, repeated feedback, cultural trends.
- **milestones.md**: Team-wide events and deadlines with expiry dates. These get surfaced automatically in 1:1 prep. Different from action items (which are individual tasks) and themes (which are ongoing patterns).

### `/hiring`
Building the team you need.

- **candidates/**: One file per candidate. Include interview notes, assessments, references.
- **open-roles/**: Job descriptions, hiring plans, ideal candidate profiles.
- **interview-rubric.md**: Your framework for evaluating candidates consistently.

### `/deals`
The opportunities you're directly involved in.

- **active/**: Deals you're currently working. Include customer context, technical requirements, team assignments, risks.
- **pipeline/**: Opportunities you're tracking but not yet fully engaged with.
- **deal-template.md**: Standard structure for tracking deal information.

### `/strategy`
Where you think long-term.

- **quarterly/**: OKRs, quarterly plans, review documents.
- **annual/**: Year-long strategy, headcount planning, budget.
- **decision-log.md**: Record of major decisions you've made, the reasoning, and outcomes. Critical for learning from your choices.

### `/communications`
Your external interface.

- **drafts/**: Messages you're working on - team emails, exec updates, Slack announcements.
- **sent/**: Archive of important communications for future reference.
- **templates/**: Reusable message templates for common scenarios (new hire announcements, deal wins, etc.).
- **writing-style-guide.md**: Your voice and tone preferences. Claude references this when drafting on your behalf. Fill it in with examples of your actual writing.

### `/meetings`
Where you process synchronous information.

- **transcripts/**: Meeting recordings or transcripts. Name by date and topic.
- **action-items.md**: Centralized list of strategic follow-ups from meetings. Organized by person at the top, with a dated log below. Tactical follow-ups stay in individual 1:1 files.

### `/growth-cycle-reviews`
Performance review archive. When you provide performance review PDFs, Claude will process them using the workflow defined in `personal/workflows/growth-cycle-review-prep-workflow.md`:

- Extracts and converts each PDF to structured markdown
- Organizes by person and review period (e.g., `Jane_Doe/H2_FY26_growth_cycle_review.md`)
- Preserves all original text faithfully with YAML metadata (ratings, period, conversion date)
- Outputs a summary table showing all ratings and files

To use: drop review PDFs into `inbox/` and say "process inbox and prep growth cycle reviews."

### `/personal`
Your own development as a leader.

- **priorities.md**: What you're focusing on right now. Update this weekly. Include your strategic bets, what you're delegating, and what you're saying no to.
- **reflection.md**: Space for thinking about your own performance, lessons learned, what you want to improve.
- **workflows-index.md**: Maps all workflow triggers to their files and shows the dependency chain between them.
- **workflows/**: Claude workflow definitions that automate recurring tasks (meeting prep, week processing, brief updates, etc.). These are instructions Claude follows when triggered by specific commands.

### `/inbox`
Your dumping ground.

Drop anything here - meeting notes, transcripts, email threads, random thoughts, PDFs, screenshots. Tell Claude "process inbox" and it will:
- Read everything in there
- Determine what's relevant and where it belongs
- File it in the appropriate folder
- Update tracking documents (action-items, team-themes, milestones, etc.)
- Flag anything important
- Move processed files to `.processed` folder

This is the lowest-friction way to get information into the system. Don't think, just dump.

## Workflow System

The workflows in `personal/workflows/` form a connected system. The key insight is that **workflows chain together** and share files as handoffs:

```
Process Week -> writes 1:1 files -> triggers Update Briefs -> refreshes briefs
Weekly Prep -> reads briefs -> runs Meeting Prep -> creates agendas
```

The **person brief** (`team/briefs/[name].md`) is the central node. It synthesizes 1:1 notes, performance records, themes, and action items into one file per person. Meeting prep reads the brief instead of re-scanning 6+ files.

See `personal/workflows-index.md` for the full dependency chain.

## How Claude Uses This System

When you give Claude information, it will:
1. Determine where it belongs in this structure
2. File it appropriately (creating new files as needed)
3. Update relevant tracking documents (team-themes, action-items, milestones, etc.)
4. Surface connections to other information you've shared

When you ask Claude for help, it will:
1. Pull context from relevant files automatically
2. Synthesize across multiple sources
3. Give you direct recommendations, not summaries
4. Update documents based on the conversation

## Working With This System

### Starting Out
You don't need to fill everything in at once. Start with what's immediately useful:
- Fill in your team structure (`team/team-structure.md`)
- Set up files for your next few 1:1s
- Document your current priorities
- Add any active deals you're working

Build the habit of dumping information into Claude after meetings, calls, or when you have thoughts to capture. Claude will organize it.

### Daily Use
- Before a 1:1: "Pull up my notes on [person]" or "What should I cover with [person] today?"
- After a meeting: Share the transcript or your notes. Claude will file them and flag anything important.
- When evaluating a candidate: "Here's the interview debrief, should we move forward?"
- When drafting communication: "Write an email to the team about [topic]"

### Weekly Rhythm
- **Mid-week:** "Process this week's meetings" - files notes, extracts action items, updates briefs
- **End of week:** "Prep for next week" - decision gate + agendas for all upcoming 1:1s
- Update priorities.md with your focus areas
- Review team-themes.md to spot patterns
- Check action-items.md for follow-ups

### What You Don't Need to Do
- Don't manually organize things. That's Claude's job.
- Don't worry about perfect formatting. Rough notes are fine.
- Don't overthink where something goes. Claude will handle it.

## Evolution

This system will evolve as you use it. Claude will:
- Create new folders when needed
- Suggest structural changes when patterns emerge
- Archive old information to keep things clean
- Adapt templates based on how you actually use them

The system serves you, not the other way around. If something isn't working, change it.

## Version Control

This system should be backed up to a private GitHub repository.

**Recommended git workflow:**
- Commit at logical milestones (after processing meetings, updating strategy docs, processing performance reviews, etc.)
- Use clear commit messages describing what changed
- Push regularly to back up your work

**What to exclude** (add to .gitignore):
- PDF files (may contain sensitive information)
- System files (.DS_Store)
- Processed file archives (.processed/)
- Credentials files
- Virtual environments

**Manual git operations**: You can always run git commands yourself to review history, create branches, or manage versions.

## Privacy Note

This system contains sensitive information: employee feedback, candidate assessments, deal details, strategic plans. Keep this directory secure. Never commit it to a public repo. Consider encrypting it if you sync it anywhere.
