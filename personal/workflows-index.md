# Workflows Index

Maps workflow triggers to files, what each reads and writes, and how they chain together.

---

## Skills and Triggers

| Skill | Trigger phrases | Workflow file |
|-------|----------------|---------------|
| Process Week | "process my meetings", "process this week" | `personal/workflows/process-week-workflow.md` |
| Weekly Prep | "prep for next week", "weekly prep" | `personal/workflows/weekly-prep-workflow.md` |
| Meeting Prep | "prep for my 1:1 with [name]" | `personal/workflows/meeting-prep-workflow.md` |
| Update Briefs | "update briefs", "update [name]'s brief" | `personal/workflows/update-briefs-workflow.md` |

---

## Dependency Chain

```
Process Week
  ├── Reads: Notion (AI meeting notes), Calendar, team/team-structure.md
  ├── Writes: team/1-1s/, meetings/, action-items.md, team-themes.md, milestones.md
  └── Calls: Update Briefs (for each person whose 1:1 was processed)

Weekly Prep
  ├── Reads: Calendar (next week), team/team-structure.md
  └── Calls: Meeting Prep for each person

Meeting Prep
  ├── Reads: team/briefs/[name].md (primary context)
  ├── Reads: Notion or local 1:1 pages (last 3 meetings)
  ├── Reads: team/milestones.md
  └── Writes: Meeting note (Notion or local)

Update Briefs
  ├── Reads: team/1-1s/, team/performance/, growth-cycle-reviews/
  ├── Reads: team-themes.md, action-items.md
  └── Writes: team/briefs/[name].md
```

---

## Key Files and What Reads Them

| File | Read by |
|------|---------|
| `team/team-structure.md` | meeting-prep, process-week, update-briefs |
| `team/briefs/[name].md` | meeting-prep (primary source), update-briefs (to diff) |
| `meetings/action-items.md` | meeting-prep (open items), process-week |
| `team/milestones.md` | meeting-prep (milestone prompts), process-week |
| `team/team-themes.md` | meeting-prep (theme context), process-week |
| `personal/priorities.md` | strategic review, weekly-prep |
| `strategy/decision-log.md` | weekly-prep (quarterly retrospective) |

---

## Notes

- Always update `meetings/action-items.md` before running update-briefs - briefs read action items
- `team/team-structure.md` must stay current or meeting-prep will silently fail Notion fetches
- Confidentiality: never create 1:1 pages under the wrong person's parent page. If no mapping exists, ask.
