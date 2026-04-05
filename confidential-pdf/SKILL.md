---
name: confidential-pdf
description: >-
  Create send-out versions of PPTX presentations or watermark existing PDFs for
  confidential distribution. Two modes: (1) Full sendout -- removes unwanted slides
  (blanks, exercises, duplicates, videos, quotes), adds red "Do Not Share" banner,
  exports to PDF with diagonal watermark, compresses for email. (2) Quick watermark --
  stamps an existing PDF with confidential notice and compresses. Use when asked to
  create a send-out, participant version, do-not-share copy, shareable PDF, clean up
  slides for distribution, watermark a PDF, add confidential notice, or prepare a
  presentation for external sharing.
---

# Confidential PDF

Two modes: full sendout (PPTX) or quick watermark (PDF).

## Mode 1: Full Sendout (PPTX input)

Triggers: "create sendout", "participant version", "clean up for sharing", "do not share copy", "make PDF of workshop slides"

### Gather inputs

| Input | Required | Default |
|-------|----------|---------|
| source_path | Yes | -- |
| client_name | Yes | -- |
| programme_type | No | multi-session |
| output_dir | No | Same as source |
| banner_text | No | "[client] Team Only - Do Not Share" |

### Run the script

```bash
python3 scripts/create_sendout.py \
  --source "/path/to/deck.pptx" \
  --client "ClientName" \
  --programme-type multi-session
```

Dry run (analysis only):
```bash
python3 scripts/create_sendout.py --source "/path/to/deck.pptx" --client "ClientName" --dry-run
```

Options: `--no-watermark` (skip PDF watermark), `--no-compress` (skip Ghostscript), `--banner-text "Custom text"`

### What the script does

1. Analyses every slide against 9 removal rules (see `references/slide-removal-rules.md`)
2. Removes flagged slides (blanks, videos, duplicates, exercises, recaps, quotes, welcome, lesson series)
3. Adds red "Do Not Share" banner to every remaining slide (exact EMU dimensions from real files)
4. Saves cleaned PPTX as `[YYMMDD] [name] (Do Not Share).pptx`
5. Exports PDF via LibreOffice
6. Adds diagonal "CONFIDENTIAL" watermark + footer bar to every PDF page
7. Compresses with Ghostscript

Expected reduction: 25-35% for multi-session, 10-15% for single-workshop.

### Review output

Check the removal summary. If reduction seems off, run `--dry-run` first. See `references/slide-removal-rules.md` for calibration guidance.

## Mode 2: Quick Watermark (PDF input)

Triggers: "watermark this PDF", "add confidential notice", "stamp as confidential"

```bash
python3 scripts/watermark_pdf.py "<input>.pdf" "<output>.pdf"
```

Custom text:
```bash
python3 scripts/watermark_pdf.py input.pdf output.pdf \
  --watermark "INTERNAL USE ONLY" \
  --footer "Property of ACME Corp."
```

Skip compression: `--no-compress`

## Optional: Email Attachment

When the user wants to send the PDF via email and Outlook MCP is available:

1. `get_attachment_upload_urls` (fileName, mimeType: application/pdf)
2. `curl -X PUT` the file to the upload URL
3. `create_reply_draft` with `attachmentTempFileIds`

For files under 3MB, use `inlineAttachments` with base64 instead.

Email copy is a separate concern -- use the `/email` skill for tone and style.

## Dependencies

- **python-pptx**: slide analysis, removal, banner insertion
- **reportlab** + **pypdf**: PDF watermark overlay
- **LibreOffice**: PPTX to PDF export (`soffice --headless`)
- **Ghostscript**: PDF compression (`gs`)
- **Outlook MCP**: email attachment (optional)
