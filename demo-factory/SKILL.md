---
name: demo-factory
description: Transforms customer interviews and document repositories into workshop-ready AI demo packages. Triggered when preparing discovery workshops, executive sessions, or compiling demo portfolios. Includes MANDATORY validation phase with terminal visualizations and Demo_Plan.md before building. Outputs prioritized use cases, Demo_XX_* demo folders, prompts/GPT configs, QA checklists, and validation reports.
---

# Agentic Use Case Demo Factory

## Why This Exists

Preparing AI workshops manually takes weeks and risks demo misalignment with real customer needs. This skill automates the pipeline from raw interviews and documents to production-ready demo packages, ensuring consistency, completeness, and business fit. It accelerates time-to-workshop and reduces the risk of irrelevant or incomplete demos.

**CRITICAL:** Phase 0 validation with terminal visualizations and Demo_Plan.md creates a visual approval gate before any demo building begins, ensuring stakeholder alignment and evidence-based demo selection.

## Purpose

- Validate demo portfolio with visual evidence mapping BEFORE building (Phase 0)
- Produce a workshop-ready package from real company inputs
- Convert interviews and documents into prioritized AI use cases
- Build a diverse demo portfolio with full assets and instructions
- Package prompts and GPT configurations with proper structure and validation

## Trigger

- **When:** Interviews and document repositories are available and a tailored AI demo plan is needed
- **When:** Preparing executive or departmental workshops with live AI demo components
- **When:** Compiling use case portfolios with full demo instructions and production assets

## Inputs (Required)

- Collect interview transcripts or meeting notes
- Collect access to document repositories or exported folders
- Collect company context and industry information
- Collect workshop audience profile and constraints (time, tools, format)

## Inputs (Optional)

- Collect priority departments or functions
- Collect existing templates or SOPs
- Collect sample outputs (reports, emails, dashboards)
- Collect compliance or legal constraints

## Tools and Conventions

- Use markitdown MCP for PDF, DOCX, PPTX, XLSX conversion
- Use rg to locate content in large repositories
- Use ASCII trees for folder structures
- Respect existing repo naming conventions; default to Demo_XX_* when present

### Language Conventions

| Document Type | Language | Rationale |
|---------------|----------|-----------|
| Demo_Instructions.md | English | For facilitators, international teams |
| Demo_Plan.md | English | Strategic document |
| Master_Demo_Sequence_Guide.md | English | Facilitator reference |
| AI_Use_Cases_Overview.md | English | Business stakeholder document |
| GPT System Prompts | English | GPT API standard |
| Participant-facing prompts | Target language (e.g., Dutch) | Natural interaction |
| GPT conversation starters | Target language | Participant-facing |
| Interview quotes | Original language | Authenticity |

### Document Types Supported

| Type | Formats | Use Cases |
|------|---------|-----------|
| Structured data | Excel (.xlsx), CSV | Data analysis, forecasting, QA demos |
| Documents | PDF, DOCX, PPTX | Contract analysis, compliance, reports |
| Images | JPG, PNG, TIFF | Label translation, visual validation, packaging artwork |
| Text | Markdown, TXT | Meeting notes, transcripts |
| Web | Live search | Trend research, market analysis |

## Primary Workflow

### Phase 0: Demo Validation & Visualization (MANDATORY)

**Purpose:** Create visual validation artifacts before building demos to ensure alignment and get user approval.

**Steps:**

1. **Terminal Graph Visualization** - Create a comprehensive ASCII visualization showing:
   - Demo name and description
   - Client documents used (with file paths)
   - Evidence from interviews/surveys that justify the demo (direct quotes with speaker and date)
   - Delivery format with icon: 💬 Simple Prompt / 🤖 Custom GPT / 📋 Claude Project / ⚙️ Skill / 🔄 Agent Swarm
   - Maturity level (see legend below)
   - Architecture diagram for agent swarms (if applicable)

2. **Maturity Level Legend:**
   ```
   ★☆☆☆☆ - Simple Prompt (copy-paste execution)
   ★★☆☆☆ - Custom GPT (conversational interface with knowledge)
   ★★★☆☆ - Claude Project (multi-turn with knowledge base)
   ★★★★☆ - Skill (procedural automation)
   ★★★★★ - Agent Swarm (multi-agent orchestration)
   ```

3. **Architecture Diagrams** - For any agent swarm demos, create ASCII flow diagrams showing:
   - Orchestrator → Worker relationships
   - Data flow between agents
   - Integration points with external systems
   - Model selection per agent (haiku/sonnet/opus)

4. **Create Demo_Plan.md** - Comprehensive markdown plan containing:
   - Full demo portfolio table with columns: Demo #, Name, Format, Maturity, Evidence Strength (⭐⭐⭐), Documents Used
   - Evidence mapping section linking each demo to specific interview quotes or document findings
   - Maturity levels explained with use case examples
   - ASCII architecture diagrams for all agent swarms
   - Build checklist with estimated effort per demo
   - Risk flags (missing inputs, synthetic data needed, complex integrations)
   - Strategic theme mapping (link demos to business priorities like Speed, Quality, Cost)
   - Changelog section for tracking updates

5. **User Approval Gate** - Display the terminal visualization and Demo_Plan.md location
   - Wait for explicit user approval before proceeding
   - Allow user to request changes to demo selection, formats, or priorities
   - Document approval in Demo_Plan.md with date

**Demo_Plan.md is a Living Document:**
- Initial approval: Required to proceed with build
- Updates allowed: New demos can be added based on new evidence
- Changelog: Document all changes with date and reason
- Re-approval: Major changes (>2 demos added/removed) require new approval confirmation
- Final approval: Required 48 hours before workshop

**Terminal Visualization Template:**
```
╔══════════════════════════════════════════════════════════════════════════════╗
║                         DEMO PORTFOLIO VALIDATION                            ║
╚══════════════════════════════════════════════════════════════════════════════╝

┌──────────────────────────────────────────────────────────────────────────────┐
│ Demo 01: Contract Review Automation                           Format: 🤖 GPT │
├──────────────────────────────────────────────────────────────────────────────┤
│ Maturity: ★★☆☆☆ (Custom GPT)                                                 │
│ Evidence: ⭐⭐⭐ (Strong - 3 stakeholder mentions)                            │
├──────────────────────────────────────────────────────────────────────────────┤
│ Documents Used:                                                              │
│   • contracts/NDA_Template_2025.docx                                         │
│   • contracts/MSA_Standard_Terms.pdf                                         │
├──────────────────────────────────────────────────────────────────────────────┤
│ Justification:                                                               │
│   "We spend 2-3 hours per contract doing manual checks against our          │
│    standard terms." - Legal Operations Lead (Interview 2024-12-10)          │
└──────────────────────────────────────────────────────────────────────────────┘

Total Demos: 8 | Formats: 2 GPT, 1 Swarm, 3 Prompt, 2 Project | Avg Maturity: ★★★
```

**Outputs:**
- Terminal visualization (displayed in console)
- Demo_Plan.md (saved to project root)
- User approval confirmation (recorded in Demo_Plan.md)

### Phase 1: Intake and Setup

- Confirm scope: organization, audience, and workshop duration
- Create a working folder for the demo package
- Inventory inputs: transcripts, documents, templates, datasets
- Normalize filenames and convert binary documents to markdown
- Apply repository convention gate (see {baseDir}/skills/operations-agentic-use-case-demo-factory/references/repo-conventions.md)

### Phase 2: Interview Analysis

- Extract pain points, manual steps, time estimates, and quality issues
- Identify stakeholder roles and owner teams
- Capture integration touchpoints and systems mentioned
- Pull direct quotes with speaker name and date to anchor findings
- Calculate potential time savings for CFO alignment

### Phase 3: Document Repository Analysis

- Identify input documents, output documents, and templates
- Map document types to processes and workflows
- Extract formatting and style patterns
- Capture boilerplate language and legal clauses
- For template-driven demos, extract section headers and layout ordering

**Document Types to Identify:**
- **Structured data:** Excel, CSV files for analysis demos
- **PDF documents:** Contracts, reports, certifications, compliance docs
- **Image documents:** Product photos, packaging artwork, labels, diagrams
  - Formats: JPG, PNG, TIFF
  - Use cases: Visual validation (label translation, compliance checks, design review)
  - Placement: Demo_Docs if being analyzed, Custom_GPT_Knowledge_Docs if reference examples

### Phase 4: Opportunity Mapping

- Map pain points to universal automation patterns
- Classify by function (operations, communication, research, decision support)
- Convert patterns into candidate use cases
- Rate by impact, effort, and demo suitability
- Map to strategic themes (Speed, Quality, Cost) for executive alignment

### Phase 5: Demo Portfolio Design

- Enforce diversity across AI capability categories using the checklist (see {baseDir}/skills/operations-agentic-use-case-demo-factory/references/demo-diversity-checklist.md)
- Use the demo catalog to confirm tier coverage, frequency, and platforms (see {baseDir}/skills/operations-agentic-use-case-demo-factory/references/Demo Types & AI Capability Categories d78e32cbdeff427482ccd673ddbcd7de.md)
- Use facilitation guidance to plan sequencing, tool switching, and delivery mix (see {baseDir}/skills/operations-agentic-use-case-demo-factory/references/AI Workshop Facilitation Guide 2ebb165a85e58092bddbe067145a0bcd.md)
- Balance quick wins with strategic demos
- Document the planned tool switches and 3-phase flow in Master_Demo_Sequence_Guide.md

### Phase 6: Solution Architecture Selection

- Choose solution type per use case
- Align complexity with workshop goals and readiness
- Determine which demos need Custom GPT vs simple prompts (see decision tree below)

**Demo Type Decision Tree:**

```
Does the demo need pre-loaded knowledge/reference docs?
├── YES → Custom GPT
│   └── Create: [Name]_GPT_Configuration.md + Custom_GPT_Knowledge_Docs/
└── NO → Prompt-only demo
    └── Create: Prompts/ folder with individual prompt files
```

### Phase 7: Demo Package Creation

Create a folder per demo with required assets based on demo type.

**Folder Structure by Demo Type:**

**Prompt-Only Demos:**
```
Demo_XX_[Name]/
├── Demo_Instructions.md
├── Prompts/
│   ├── 01_[first_prompt].md
│   ├── 02_[second_prompt].md
│   └── 03_[third_prompt].md
├── Demo_Docs/
└── Backup_Outputs/
```

**Custom GPT Demos:**
```
Demo_XX_[Name]/
├── Demo_Instructions.md
├── [Name]_GPT_Configuration.md
├── Prompts/
│   └── usage_prompts.md
├── Demo_Docs/
├── Custom_GPT_Knowledge_Docs/
└── Backup_Outputs/
```

**Key Rules:**
- Demo_Docs = Runtime inputs (the thing being analyzed/processed)
- Custom_GPT_Knowledge_Docs = Reference knowledge (examples, checklists, standards the GPT should know)
- Backup_Outputs = Captured outputs for fallback (populated in Phase 10)
- Synthetic input docs are allowed only with explicit user approval

**Demo Tags Schema (Required in Demo_Instructions.md):**

| Tag | Values | Purpose |
|-----|--------|---------|
| type | excel-data, custom-gpt, document-analysis, deep-research, communication | Capability category |
| platform | chatgpt, claude, perplexity, chatgpt-custom-gpt | Tool to use |
| audience | operations, finance, legal, executive, quality, category-management | Target participants |
| data-type | structured, unstructured, multi-document, live-web | Input format |
| delivery-mode | live-build, prepared-hybrid, pre-built-walkthrough | Execution style |
| duration | Xmin | Time allocation |

### Phase 8: Prompt Creation

**Prompt Simplicity Decision Tree:**

```
Is this a Custom GPT demo with knowledge base?
├── YES → Create structured GPT Configuration
│   └── Use [Name]_GPT_Configuration.md format
│   └── System prompt in English
│   └── Conversation starters in target language
│   └── Include character count validation
│   └── Include data anonymization notes if needed
│
└── NO → Create simple conversational prompts
    └── Write prompts directly in target language
    └── Start with "Je bent..." / "You are..."
    └── Keep each prompt <1000 characters
    └── No Prompt Wizard needed for simple prompts
```

**Simple Prompts (Prompt-only demos):**
- Format: Individual .md files per prompt in Prompts/ folder
- Language: Target language (e.g., Dutch)
- Start with: "Je bent een [role] die [task]..."
- Keep conversational and direct
- Typical length: 400-800 characters per prompt

**GPT System Prompts (Custom GPT demos):**
- Format: [Name]_GPT_Configuration.md
- Language: English for system prompt, target language for conversation starters
- Must include:
  - GPT Name and Description
  - System Prompt (with character count - must be <8000)
  - Conversation Starters (4 recommended, in target language)
  - Knowledge Files to Upload
  - Capabilities to Enable (Code Interpreter, Web Browsing, etc.)
  - Data anonymization notes (if real supplier names, codes, etc. were removed)
  - Prompt validation checklist

**GPT Configuration Template:**

```markdown
# [Name] - Custom GPT Configuration

## GPT Settings

| Setting | Value |
|---------|-------|
| Name | [Display name] |
| Description | [One sentence] |

## System Prompt

```
[System prompt content - MUST be under 8000 characters]
```

## Character Count

System prompt: X characters (limit: 8000)

## Conversation Starters

1. "[First question in target language]"
2. "[Second question]"
3. "[Third question]"
4. "[Fourth question]"

## Knowledge Files

Upload these files from Custom_GPT_Knowledge_Docs/:
- [file1.pdf] - [purpose]
- [file2.xlsx] - [purpose]

## Capabilities

| Capability | Enabled |
|------------|---------|
| Web Browsing | Yes/No |
| DALL-E Image Generation | No |
| Code Interpreter | Yes/No |

## Data Anonymization Applied

| Original | Anonymized To | Reason |
|----------|---------------|--------|
| [Real supplier name] | [Generic placeholder] | Confidentiality |

## Validation Checklist

- [ ] System prompt starts with "You are..."
- [ ] No bold formatting (** or __)
- [ ] Character count under 8000
- [ ] Includes output format section
- [ ] Includes output example
- [ ] Conversation starters in target language
- [ ] Knowledge files listed and present
```

### Phase 9: Demo Instructions Creation

Create Demo_Instructions.md using this template:

```markdown
# Demo XX: [Name]

> **STATUS** - LEAD DEMO | SUPPORTING DEMO

---

## Quick Demo Card

**30-Second Pitch:** "[One sentence value prop from stakeholder perspective]"

| What to Say | What to Show |
|-------------|--------------|
| [Talking point 1] | [Action/screen] |
| [Talking point 2] | [Action/screen] |

**Input files:** `Demo_Docs/[filename]`
**Backup output:** `Backup_Outputs/`

---

## Overview

| Field | Value |
|-------|-------|
| Duration | X minutes |
| Type | Prompt / Custom GPT |
| Complexity | Low / Medium / High |
| Platform | ChatGPT / Claude |
| Theme | Speed / Quality / Cost |
| Differentiator | [What makes this demo special] |

---

## Demo Tags

- type: [value]
- platform: [value]
- audience: [value]
- data-type: [value]
- delivery-mode: [value]
- duration: [X]min

---

## Business Context

[2-3 sentences on why this matters to the client]

**Pain Point:** "[Direct quote from interview]" - [Speaker, Date]

---

## Demo Flow

### Setup (X min)
1. [Step]
2. [Step]

### Execution (X min)
1. [Step with expected output]
2. [Step with expected output]

### Wrap-up (X min)
1. [Key message]
2. [Transition to next demo]

---

## Key Messages

- [Business impact point 1]
- [Business impact point 2]
- [Time savings estimate if applicable]

---

## Transition

"[Bridge sentence to next demo...]"

---

## Prompts / GPT Configuration

[Reference to Prompts/ folder or GPT Configuration file]

---

## Backup Plan

If live demo fails:
1. Open Backup_Outputs/[file]
2. Walk through pre-captured output
3. Explain what would have happened live

---

## Files in This Demo

```
Demo_XX_[Name]/
├── Demo_Instructions.md (this file)
├── [GPT_Configuration.md if Custom GPT]
├── Prompts/
├── Demo_Docs/
├── Custom_GPT_Knowledge_Docs/ [if Custom GPT]
└── Backup_Outputs/
```
```

### Phase 10: QA and Readiness

- Validate demo timing and success metrics
- Confirm each demo has realistic inputs and expected outputs
- Verify style fidelity and template adherence
- Produce a character count report for each GPT prompt
- Run validation script and record results
- Confirm demo diversity checklist is completed
- Verify each Demo_Instructions.md includes all demo tags
- Cross-reference against Demo_Plan.md to ensure all approved demos were built
- Update _Analysis/Prompt_QA_Checklist.md

**Backup_Outputs Population (2-3 days before workshop):**
1. Run each demo end-to-end with actual inputs
2. Capture all outputs (screenshots, text, tables, visualizations)
3. Save to Backup_Outputs/ with descriptive filenames:
   - `output_01_initial_analysis.png`
   - `output_02_recommendations.md`
4. Verify backup outputs can substitute for live demo
5. Test backup flow with facilitator

### Phase 11: Deliverables Assembly

- Compile workshop agenda and demo sequence guide
- Generate executive summary and key messages
- Produce slide-ready use case summaries
- Create AI_Use_Cases_Overview.md (see template below)
- Deliver the full demo package tree
- Include Demo_Plan.md as the strategic overview document

**AI_Use_Cases_Overview.md Template:**

```markdown
# [Client] AI Workshop - Use Cases Overview

## Workshop Context

| Item | Details |
|------|---------|
| Company | [Name, revenue, industry] |
| Date | [Workshop date] |
| Location | [Venue] |
| Goal | [Primary objective] |
| Themes | [Speed, Quality, Cost - or client-specific] |

---

## Demo Portfolio Summary

| # | Use Case | Format | Theme | Time |
|---|----------|--------|-------|------|
| 01 | [Name] | Prompt/GPT | [Theme] | X min |
| ... | ... | ... | ... | ... |

---

## Demo 01: [Name]

### What It Does
[2-3 sentences]

### Why It's Valuable

| Current State | With AI |
|---------------|---------|
| [Pain point] | [Benefit] |

### Business Impact
- [Impact 1]
- [Impact 2]

### Documents Used

| Document | Type | Purpose |
|----------|------|---------|
| [filename] | Demo input / Knowledge | [Why needed] |

### Sample Output
[Brief description of what AI produces]

---

[Repeat for each demo...]

---

## Technology Summary

### Platforms Used

| Platform | Demos | Why |
|----------|-------|-----|
| ChatGPT (Prompt) | XX, XX | Quick, no setup |
| ChatGPT (Custom GPT) | XX, XX | Pre-loaded knowledge |

### Data Types

| Type | Demos |
|------|-------|
| Excel/CSV | XX, XX |
| PDF | XX, XX |
| Images | XX, XX |

---

## Key Messages

1. **Speed**: [Message]
2. **Quality**: [Message]
3. **Scale**: [Message]

---

## Executive Alignment

[Link demos to executive priorities with time savings estimates]

| Demo | Time Saved | Frequency | Annual Impact |
|------|------------|-----------|---------------|
| [Name] | Xh → Ymin | [Frequency] | Z hours |
```

## Output Checklist

**Phase 0 Outputs (MANDATORY):**
- [ ] Demo_Plan.md with user approval confirmation
- [ ] Terminal visualization of demo portfolio displayed
- [ ] Architecture diagrams for all agent swarms (if applicable)

**Package Structure:**
- [ ] _Analysis/ folder with Prompt_QA_Checklist.md
- [ ] AI_Use_Cases_Overview.md in project root
- [ ] Master_Demo_Sequence_Guide.md
- [ ] All Demo_XX_* folders with complete structure

**Per-Demo Outputs:**
- [ ] Demo_Instructions.md with all demo tags
- [ ] Prompts/ folder with clean prompts (start with "Je bent..." or "You are...")
- [ ] Demo_Docs/ with runtime inputs only
- [ ] Custom_GPT_Knowledge_Docs/ for GPT demos (original files, not markdown)
- [ ] [Name]_GPT_Configuration.md for Custom GPT demos
- [ ] Backup_Outputs/ populated 2-3 days before workshop

**Documentation:**
- [ ] Demo diversity checklist completed (or exceptions documented)
- [ ] Tool switching plan in Master_Demo_Sequence_Guide.md
- [ ] Character counts validated for all GPT prompts (<8000)
- [ ] Data anonymization documented where applied
- [ ] Cross-doc references updated

## Folder Structure Template (ASCII)

```
Demo_Package/
├── _Analysis/                         # Validation artifacts
│   └── Prompt_QA_Checklist.md
├── AI_Use_Cases_Overview.md           # Business-friendly summary
├── Demo_Plan.md                       # Phase 0 output - strategic overview
├── Demo_01_[Use_Case_Name]/           # Prompt-only demo
│   ├── Demo_Instructions.md
│   ├── Prompts/
│   │   ├── 01_[first_prompt].md
│   │   └── 02_[second_prompt].md
│   ├── Demo_Docs/
│   └── Backup_Outputs/
├── Demo_02_[Use_Case_Name]/           # Custom GPT demo
│   ├── Demo_Instructions.md
│   ├── [Name]_GPT_Configuration.md
│   ├── Prompts/
│   ├── Demo_Docs/
│   ├── Custom_GPT_Knowledge_Docs/     # Original files (PDFs, images)
│   └── Backup_Outputs/
└── Master_Demo_Sequence_Guide.md
```

## References and Assets

- {baseDir}/skills/operations-agentic-use-case-demo-factory/references/demo-diversity-checklist.md
- {baseDir}/skills/operations-agentic-use-case-demo-factory/references/Demo Types & AI Capability Categories d78e32cbdeff427482ccd673ddbcd7de.md
- {baseDir}/skills/operations-agentic-use-case-demo-factory/references/AI Workshop Facilitation Guide 2ebb165a85e58092bddbe067145a0bcd.md
- {baseDir}/skills/operations-agentic-use-case-demo-factory/references/demo-type-asset-matrix.md
- {baseDir}/skills/operations-agentic-use-case-demo-factory/references/template-alignment-checklist.md
- {baseDir}/skills/operations-agentic-use-case-demo-factory/references/qa-checklist-template.md
- {baseDir}/skills/operations-agentic-use-case-demo-factory/references/repo-conventions.md
- {baseDir}/skills/operations-agentic-use-case-demo-factory/assets/demo-instructions-template.md
- {baseDir}/skills/operations-agentic-use-case-demo-factory/assets/prompt-qa-checklist-template.md
- {baseDir}/skills/operations-agentic-use-case-demo-factory/assets/gpt-configuration-template.md

## Testing & Validation

### Validation Approach

- Use {baseDir}/skills/operations-agentic-use-case-demo-factory/scripts/validate_demo_package.py to verify folder structure and completeness
- Automate checks for common structural errors before manual QA

### Test Cases

| Test Case | Purpose | Pass Criteria |
|-----------|---------|---------------|
| Missing Demo_Plan.md | Ensures Phase 0 validation occurred | Validation fails if Demo_Plan.md not found |
| Missing AI_Use_Cases_Overview.md | Ensures business summary created | Warning if not found |
| Missing _Analysis folder | Ensures QA artifacts created | Warning if not found |
| Demo built not in Demo_Plan.md | Ensures adherence to approved plan | Cross-reference check flags demos built without approval |
| Agent swarm without architecture | Ensures swarm complexity documented | Validation fails if swarm lacks ASCII diagram |
| User approval not documented | Ensures explicit sign-off | Demo_Plan.md must contain approval section |
| Missing Demo_Docs | Catches incomplete demos | Script exits with error |
| GPT demo without Knowledge_Docs | Checks GPT demos have knowledge | Warning for GPT demos without knowledge |
| Prompt-only demo with Knowledge_Docs | Checks unnecessary folders | Warning for prompt demos with knowledge folder |
| Knowledge docs are .md files | Should be original files | Warning if only .md files in Knowledge_Docs |
| Prompt doesn't start with role | Checks prompt format | Warning if prompt doesn't start with "Je bent" or "You are" |
| Prompt character count > 8000 | Ensures GPT compatibility | Error; re-invoke condensing |
| Demo folder naming | Validates convention | Regex: Demo_\d{2}_ prefix required |
| Missing demo tags | Ensures categorization | Warning if Demo_Instructions.md lacks tags |
| Empty Backup_Outputs | Checks readiness | Warning 2 days before workshop |

### Magic Numbers & Thresholds

- **8000 character limit per GPT prompt** - GPT API hard limit for system prompt field
- **1000 character threshold** - Prompts under this are "simple" (no Prompt Wizard needed)
- **Demo numbering:** Demo_01_ through Demo_99_
- **Evidence strength rating:**
  - ⭐⭐⭐ Strong: 3+ stakeholder mentions OR direct quote + supporting document evidence
  - ⭐⭐ Moderate: 1-2 stakeholder mentions OR clear document evidence without direct quotes
  - ⭐ Weak: Inferred from context, no explicit validation
- **Maturity level star ratings:** 1-5 stars mapping to Simple Prompt through Agent Swarm
- **Backup population timing:** 2-3 days before workshop (allows fixes, close to event)
- **Re-approval threshold:** >2 demos added/removed requires new approval

## Notes on Prompt Creation

**For Simple Prompts:**
- Write directly in target language
- No Prompt Wizard invocation needed
- Keep conversational and task-focused

**For GPT System Prompts:**
- Use Prompt Wizard conventions but create manually
- Always include character count
- Document any data anonymization
- Include validation checklist in configuration file

**Data Anonymization Guidance:**
When to anonymize:
- Real supplier/manufacturer names
- Real item codes, SKUs, barcodes
- Real customer names
- Real employee names
- Pricing data
- Any data marked confidential by client

How to document:
- Include anonymization table in GPT configuration
- Map original → anonymized values
- Note reason for each anonymization

## Script Usage

1. Scaffold a new demo:
   ```
   python {baseDir}/scripts/scaffold_demo.py --name "Demo_09_[Name]" --type gpt --root "<project_root>/Demo_Package"
   ```

2. Validate the demo package:
   ```
   python {baseDir}/scripts/validate_demo_package.py --root "<project_root>/Demo_Package" --project-root "<project_root>"
   ```
