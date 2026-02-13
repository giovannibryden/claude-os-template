# Claude OS - System Guide

This is your personal operating system. Everything in this directory exists to help you be a world-class leader.

## Structure

### `/team`
Your people. This is your most important asset.

- **1-1s/**: Individual conversation notes with each team member. Name files by person and date (e.g., `sarah-2026-02-05.md`). Keep these informal—they're for you, not HR.
- **performance/**: Performance reviews, feedback prep, development plans.
- **org-chart.md**: Current team structure, who reports to whom, regional breakdown.
- **team-themes.md**: Running log of patterns you're seeing across the team—morale issues, skill gaps, repeated feedback, cultural trends.

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

- **drafts/**: Messages you're working on—team emails, exec updates, Slack announcements.
- **sent/**: Archive of important communications for future reference.
- **templates/**: Reusable message templates for common scenarios (new hire announcements, deal wins, etc.).

### `/meetings`
Where you process synchronous information.

- **transcripts/**: Meeting recordings or transcripts. Name by date and topic.
- **action-items.md**: Centralized list of follow-ups from meetings that need tracking.

### `/personal`
Your own development as a leader.

- **development/**: Books, articles, notes on leadership, courses you're taking.
- **priorities.md**: What you're focusing on right now. Update this weekly.
- **reflection.md**: Space for thinking about your own performance, lessons learned, what you want to improve.

### `/inbox`
Your dumping ground.

Drop anything here—meeting notes, transcripts, email threads, random thoughts, PDFs, screenshots. Tell Claude "process inbox" and it will:
- Read everything in there
- Determine what's relevant and where it belongs
- File it in the appropriate folder
- Update tracking documents
- Flag anything important
- Move processed files to `.processed` folder

This is the lowest-friction way to get information into the system. Don't think, just dump.

## How Claude Uses This System

When you give Claude information, it will:
1. Determine where it belongs in this structure
2. File it appropriately (creating new files as needed)
3. Update relevant tracking documents (team-themes, action-items, etc.)
4. Surface connections to other information you've shared

When you ask Claude for help, it will:
1. Pull context from relevant files automatically
2. Synthesize across multiple sources
3. Give you direct recommendations, not summaries
4. Update documents based on the conversation

## Working With This System

### Starting Out
You don't need to fill everything in at once. Start with what's immediately useful:
- Create your org-chart
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
- Commit at logical milestones (after processing inbox, updating strategy docs, etc.)
- Use clear commit messages describing what changed
- Push regularly to back up your work

**What to exclude** (add to .gitignore):
- PDF files (may contain sensitive information)
- System files (.DS_Store)
- Processed file archives (.processed/)
- Credentials files

**Manual git operations**: You can always run git commands yourself to review history, create branches, or manage versions.

## Privacy Note

This system contains sensitive information: employee feedback, candidate assessments, deal details, strategic plans. Keep this directory secure. Never commit it to a public repo. Consider encrypting it if you sync it anywhere.
