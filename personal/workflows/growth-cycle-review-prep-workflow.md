# Growth Cycle Review Prep Workflow

When the user provides PDF files containing performance reviews (Growth Cycle reviews, annual reviews, etc.) for direct reports, follow these steps to extract, convert, and organize the content into structured markdown files.

---

## Input

The user will provide one or more PDF files. Each PDF contains:

- A **self-review** written by the direct report, including their self-assessed performance rating
- A **manager review** written by the user (the manager), including a manager rating

---

## Step 1: Identify the Direct Report

For each PDF, extract the name of the direct report the review belongs to. Use this name to:

- Determine the correct output directory (see Step 4)
- Populate the metadata block

---

## Step 2: Identify the Review Period

Determine which review period the document covers. Use a consistent format such as: **H1 FY26**, **H2 FY26**, **H1 FY27**, etc., where:

- **H1** = the first half of the fiscal year
- **H2** = the second half of the fiscal year

Look for the review period in the following places (in order of priority):

1. An explicit label in the document (e.g., "H2 FY26 Growth Cycle Review", "First Half FY2026")
2. Dates referenced in the review text — infer the half and fiscal year from those dates
3. File name of the PDF if it contains date information

If the fiscal year uses a calendar year reference (e.g., "2026"), map it to the correct FY label. If the period truly cannot be determined, mark it as **Unknown** and flag it in the summary.

---

## Step 3: Convert PDF Content to Markdown

Convert the full contents of each PDF to clean, well-formatted markdown. Follow these formatting rules:

### Metadata block

Add a YAML metadata block at the top of each file:

```yaml
---
Direct Report: [Name]
Review Period: [Period if available, otherwise "Unknown"]
Self-Assessment Rating: [Rating]
Manager Rating: [Rating]
Converted: [Today's Date]
---
```

### Content formatting

- Use `## Self-Review` and `## Manager Review` headers to clearly separate the two sections
- Include the identified review period prominently in the document header (e.g., `# H2 FY26 Growth Cycle Review — [Name]`)
- **Preserve all original text faithfully** — do not summarize or omit anything
- Format any ratings prominently using bold text (e.g., **Rating: Exceeds Expectations**)
- Preserve bullet points, numbered lists, and section headers from the original document

---

## Step 4: Save to the Correct Directory

Save each converted markdown file to the `growth-cycle-reviews/` directory at the project root using this structure:

```
growth-cycle-reviews/
  [Direct_Report_Name]/
    [ReviewPeriod]_growth_cycle_review.md
```

### Naming conventions

- Replace spaces in names with underscores (e.g., `Jane_Doe/`)
- Replace spaces in review periods with underscores (e.g., `H2_FY26_growth_cycle_review.md`)
- If the review period cannot be determined, name the file `review_[n].md` where `n` is a sequential number
- If a directory for a direct report does not already exist, create it
- If multiple reviews for the same person exist across different periods, save each as a separate file — **do not overwrite**

---

## Step 5: Confirm & Summarize

After processing all PDFs, output a summary table to the terminal:

| Direct Report | Review Period | Self-Rating | Manager Rating | File Saved |
|---|---|---|---|---|
| Jane Doe | H2 FY26 | Meets Expectations | Exceeds Expectations | `growth-cycle-reviews/Jane_Doe/H2_FY26_growth_cycle_review.md` |

Flag any PDFs that could not be fully processed or where information was missing.

---

## Error Handling

- If a PDF is **password protected or unreadable**, skip it and note the issue in the summary
- If any required field (name, rating, period) is missing, still process the file but flag the missing fields in the summary table and in the metadata block as "Unknown"

---

## Key Principles

1. **Preserve original voice:** Do not alter, interpret, or editorialize any review content — preserve the original wording exactly as written
2. **No summarization:** Convert the full content, not a summary
3. **Faithful formatting:** Maintain the document's structure (bullets, numbered lists, headers) as closely as possible in markdown
4. **Idempotent:** Running this on the same PDF twice should produce the same output without duplicating files (match on review period + person)

---

## Notes

- This workflow stores output in `growth-cycle-reviews/` at the project root, separate from `team/performance/` which is for feedback prep and development plans
- PDFs are excluded from git via `.gitignore` — the converted markdown files are the canonical record
- The converted markdown files may contain sensitive performance data — treat with the same privacy considerations as other personnel files
