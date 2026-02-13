# Inbox

This is your dumping ground. Drop anything here and tell Claude "process inbox."

## What to Put Here

- Meeting notes or transcripts
- Email threads you want to save
- Screenshots
- PDFs (articles, reports, documents)
- Random thoughts you want to capture
- Anything you're not sure where to file

## How It Works

1. Drop files here (any format)
2. Tell Claude: "process inbox"
3. Claude will:
   - Read everything
   - Extract key information
   - File items in the appropriate directories
   - Update tracking documents (action-items.md, team-themes.md, etc.)
   - Flag anything important
   - Move processed files to `.processed/`

## Pro Tips

- **Don't overthink it** - If you're not sure where something goes, throw it in inbox
- **Batch processing** - Let items accumulate and process them all at once (end of day/week)
- **Any format works** - .txt, .md, .pdf, .docx, screenshots, etc.
- **No organization needed** - Claude figures out what's important and where it belongs
- **Quick capture** - The faster you can dump info here, the more you'll use the system

## Examples

### Meeting Notes
```
Subject: 1:1 with Sarah - 2026-02-13

- Discussed Q1 goals
- Sarah feeling overwhelmed with projects
- Needs help prioritizing
- Action: I'll work with her on focus areas next week
```

Claude will:
- Create/update `team/1-1s/sarah-2026-02-13.md`
- Add action item to `meetings/action-items.md`
- Note "overwhelm" theme in `team/team-themes.md`

### Candidate Feedback
```
Subject: Interview with Marcus Chen

Strong technical skills, good culture fit, slight concern about experience
with enterprise customers. Recommend moving to final round.
```

Claude will:
- Create/update `hiring/candidates/marcus-chen.md`
- Summarize feedback
- Flag for decision

### Random Thought
```
Thinking we need to revisit our demo strategy. Seeing feedback from
3 different deals that our standard demo isn't resonating. Need to
make it more vertical-specific.
```

Claude will:
- File in `strategy/` or create a new note
- Cross-reference with deal files
- Suggest next steps

## What Happens to Processed Files

After processing, Claude moves files to `.processed/` (which is git-ignored). This keeps your inbox clean while preserving originals if you need them.

You can safely delete files from `.processed/` once you're confident they've been properly filed.

## Start Using It

Try it now:
1. Create a file called `test.md` in this directory
2. Write a few sentences about something on your mind
3. Tell Claude "process inbox"
4. See where it ends up

Once you see how it works, you'll use it constantly.
