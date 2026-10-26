# Changelog

All notable changes to the Claude OS template will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.0] - 2026-10-26

### Added
- **Context Discipline** section in `CLAUDE.md`: source provenance, synthesized files as pointers, code over prompt rules, per-person isolation, deliberate forgetting
- **Write growth cycle review workflow** (`personal/workflows/write-growth-cycle-review-workflow.md`) with isolated prior-view and writer subagents
- **`bin/gc-sources.py`**: lists the only in-window files a review may cite (window set by Review Period label) and `--check` fails drafts citing anything else

### Changed
- **Meeting prep**: Source Contract - agenda topics need a source you were in; Slack, email, and synthesized files go to the internal summary only, with a "You may not have seen" section
- **Weekly prep**: one clean-context subagent per person; decision gate ignores Slack-only or `[synth]` decisions; directs always prepped even without a booked slot
- **Update briefs** and **brief template**: every bullet carries a source tag (`[1:1 date]`, `[review cycle]`, `[you]`, `[synth]`); prior reviews used for expectations only, never as recent wins

## [2.0.0] - 2026-09-24

### Added
- **Person briefs** (`team/briefs/`) - synthesized context files per person, the primary source for meeting prep
- **Team milestones** (`team/milestones.md`) - team-wide deadlines with expiry dates, surfaced in 1:1 prep
- **Team structure** (`team/team-structure.md`) - evolved from org-chart with Notion page mappings
- **Writing style guide** (`communications/writing-style-guide.md`) - template for Claude to match your voice
- **Workflows index** (`personal/workflows-index.md`) - maps triggers to files, shows dependency chain
- **Meeting prep workflow** (`personal/workflows/meeting-prep-workflow.md`) - brief-first, development-first agenda building
- **Update briefs workflow** (`personal/workflows/update-briefs-workflow.md`) - synthesize 1:1s/performance into briefs
- **Process week workflow** (`personal/workflows/process-week-workflow.md`) - batch-process a week's meetings
- **Weekly prep workflow** (`personal/workflows/weekly-prep-workflow.md`) - decision gate + batch meeting prep

### Changed
- **Action items** restructured: "Open Items by Person" section at top, dated log below, strategic items only
- **Team themes** simplified: removed unused category taxonomy, adopted organic format with update history
- **1:1 template** updated: "What They Said" + "Context for Next 1:1" sections replace generic notes format
- **CLAUDE.md** updated with workflow system documentation, briefs concept, milestones
- **WORKFLOWS.md** expanded with workflow dependency chain, Update Briefs, Weekly Prep (decision gate), Process Week
- **README.md** updated to reflect workflow system and briefs concept
- **.gitignore** expanded with `__pycache__/`, `.venv*/`, `*.wav`, `run.log`, `.claude/`

## [1.0.0]

### Added
- Initial release of Claude OS template
- Core directory structure for team, hiring, deals, strategy, meetings, communications, personal
- SETUP.sh automated configuration script
- Comprehensive documentation (README, SETUP, START-HERE, CLAUDE, WORKFLOWS)
- Template files for 1:1s, candidates, deals, action items, themes, decisions
- Communication templates (new hire, team update, feedback request)
- Integration setup guides (Notion, Google Calendar, Slack)
- Inbox processing workflow
- Growth cycle review processing workflow
- Git integration and .gitignore
