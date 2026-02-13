# Setup Guide

## Quick Start (5 minutes)

### 1. Clone this repository

```bash
cd ~
git clone [YOUR-TEMPLATE-REPO-URL] claude-os
cd claude-os
```

### 2. Run the setup script

```bash
chmod +x SETUP.sh
./SETUP.sh
```

This will prompt you for:
- Your name
- Your role/title
- Your team name
- Your git repository URL (optional)

### 3. Customize your config

The setup script creates a basic `config.md`. Review and adjust it to match your working style.

### 4. Start using it

**Option A: Process your first meeting**
```bash
# Drop a meeting transcript or notes into inbox/
cp ~/Downloads/meeting-notes.txt inbox/
```

Then tell Claude: "process inbox"

**Option B: Prep for your next 1:1**
```bash
cp team/1-1s/template.md team/1-1s/sarah-2026-02-13.md
```

Edit the file with your agenda, then ask Claude: "What should I cover with Sarah?"

## Next Steps

### Essential (Do these first)

- [ ] **Set your priorities** - Edit `personal/priorities.md` with your top 3 current focuses
- [ ] **Document your team** - Fill in `team/org-chart.md` with your direct reports
- [ ] **Create your first 1:1** - Copy `team/1-1s/template.md` for your next 1:1

### Recommended (This week)

- [ ] **Connect Notion** (if you use it) - Follow `.setup/notion-mcp-setup.md`
- [ ] **Set up git backup** - Push to your private GitHub repo
- [ ] **Process old meeting notes** - Drop 2-3 past meetings in inbox to build context

### Optional (As needed)

- [ ] **Google Calendar integration** - Follow `.setup/google-calendar-mcp-setup.md`
- [ ] **Customize templates** - Edit files in `communications/templates/`
- [ ] **Add hiring rubric** - Create `hiring/interview-rubric.md`

## Integration Setup

This system works standalone, but integrations make it more powerful:

### Notion (Recommended if you use Notion for 1:1s)
- **Time:** 15 minutes
- **Benefit:** Sync your Notion 1:1 docs with Claude
- **Instructions:** [.setup/notion-mcp-setup.md](.setup/notion-mcp-setup.md)

### Google Calendar (Optional)
- **Time:** 10 minutes
- **Benefit:** Auto-import meeting notes and transcripts
- **Instructions:** [.setup/google-calendar-mcp-setup.md](.setup/google-calendar-mcp-setup.md)

## Troubleshooting

### Claude doesn't see my files
Make sure you're in the claude-os directory when you start Claude:
```bash
cd ~/claude-os
claude
```

### Git push fails
Add your remote repository:
```bash
git remote add origin git@github.com:your-username/your-repo.git
git push -u origin main
```

### I want to start over
```bash
cd ~
rm -rf claude-os
# Then re-clone and run setup again
```

## Daily Usage Pattern

1. **Morning:** Ask Claude "What's on my plate today?"
2. **After meetings:** Drop notes/transcripts in `inbox/`, tell Claude to process
3. **Before 1:1s:** Ask Claude to prep you on the person
4. **End of day:** Quick brain dump to Claude or drop notes in inbox

## Getting Help

- Read [WORKFLOWS.md](WORKFLOWS.md) for advanced usage patterns
- Read [CLAUDE.md](CLAUDE.md) for system structure details
- Ask Claude - it's designed to help you use this system
- Open an issue on the template repo

---

**All set?** Head to [START-HERE.md](START-HERE.md) to learn the basics.
