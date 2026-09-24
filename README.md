# Claude OS

Your personal operating system for being a world-class manager.

## What This Is

Claude OS is a structured system for capturing, organizing, and retrieving everything you need to lead effectively. It turns Claude into your strategic thought partner with full context about your team, decisions, and priorities.

Instead of scattering information across tools, you capture it once in a simple file structure. Claude handles organization, synthesis, and retrieval.

## Quick Start

```bash
# Clone this repository
git clone [YOUR-TEMPLATE-REPO-URL] claude-os
cd claude-os

# Run setup (5 minutes)
chmod +x SETUP.sh
./SETUP.sh

# Start using it
# Drop a meeting transcript in inbox/ and tell Claude "process inbox"
```

## What You Get

- **Before 1:1s:** Claude preps you with person briefs, open items, and themes - development first, pipeline last
- **After meetings:** Claude files notes, extracts action items, and updates person briefs automatically
- **Weekly:** "Process this week" batch-files all meetings; "Prep for next week" creates all agendas with a decision gate
- **When hiring:** Claude evaluates candidates against your rubric
- **For decisions:** Claude synthesizes context from across all your documents
- **For communication:** Claude drafts in your voice using your writing style guide

## The Workflow System

Workflows chain together and share files as handoffs:

```
Process Week -> writes 1:1 files -> triggers Update Briefs -> refreshes briefs
Weekly Prep -> reads briefs -> runs Meeting Prep -> creates agendas
```

The **person brief** (`team/briefs/[name].md`) is the central node - it synthesizes 1:1 notes, performance records, themes, and action items into one file per person. Meeting prep reads the brief instead of re-scanning 6+ files.

## System Structure

```
claude-os/
├── team/           # Your people (1:1s, briefs, performance, themes, milestones)
├── hiring/         # Candidates and open roles
├── deals/          # Active opportunities
├── strategy/       # Long-term plans and decisions
├── meetings/       # Transcripts and action items
├── communications/ # Drafts, sent messages, templates, writing style guide
├── personal/       # Your priorities, workflows, and development
└── inbox/          # Drop anything here for processing
```

## Documentation

- **[PITCH.md](PITCH.md)** - Why use this system? (Read this first)
- **[SETUP.md](SETUP.md)** - Installation and configuration
- **[START-HERE.md](START-HERE.md)** - Getting started guide
- **[CLAUDE.md](CLAUDE.md)** - System structure and philosophy
- **[WORKFLOWS.md](WORKFLOWS.md)** - Advanced usage patterns

## Time Investment

- **Setup:** 20 minutes
- **Daily use:** 0 extra time (you're already taking notes)
- **Payoff:** Hours saved per week on context switching and decision prep

## Who This Is For

This works best if you:
- Manage a team (any size)
- Have recurring 1:1s you want to track
- Make hiring decisions
- Need to synthesize information across multiple sources
- Want a thought partner who remembers everything

## Privacy & Security

This system contains sensitive information. Keep it private:
- Use a private git repository
- Never commit to public repos
- Add sensitive files to `.gitignore`
- Consider encrypting if syncing across devices

## Contributing

If you develop useful patterns or improvements:
1. Document them in your own repo
2. Open an issue or PR to suggest additions to the template
3. Share workflows in [WORKFLOWS.md](WORKFLOWS.md)

## License

[Choose your license - MIT recommended for open templates]

---

**Ready?** Head to [SETUP.md](SETUP.md) to get started.
