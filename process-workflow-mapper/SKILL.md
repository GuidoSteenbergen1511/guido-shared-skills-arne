---
name: process-workflow-mapper
description: Creates a high-level, company-wide workflow map from an interview transcript. Use when asked to map an entire company workflow, build a process workflow map from a transcript, or summarize major functional phases with substeps and supporting functions.
---
# Process Workflow Mapper

## Purpose
Generate a comprehensive, high-level workflow for the entire company based on an interview transcript. Cover all major functional areas with 4-6 action-oriented phases and 3-4 substeps each.

## Inputs
- Context about the company (if available)
- Interview transcript
- Description of process to map (if provided)
- Optional: "Example Workflow Phases and Subphases.docx" for phase naming guidance

## Steps
1. Identify the company name and type from the transcript. If unclear, ask the user.
2. If needed, use web search to confirm industry/type (use current sources).
3. Analyze the transcript for departments, systems, and unique process details.
4. Build 4-6 phases that cover the company end-to-end. Each phase must start with a verb.
5. Add 3-4 substeps under each phase. Include tools, systems, and stakeholders mentioned.
6. Add a Supporting Functions section for cross-functional activities.
7. Ask clarification questions if details are missing or ambiguous.

## Style Rules
- Use parallel, action-driven phrasing.
- Be concise but specific; include contextual details from the transcript.
- Use bolded phase headings and bullet points for substeps.

## Output Format

### Workflow

**[Company Name Comprehensive Workflow]**

1. **[Phase 1: High-Level Title]**
   - Sub-step 1
   - Sub-step 2
   - Sub-step 3

2. **[Phase 2: High-Level Title]**
   - Sub-step 1
   - Sub-step 2
   - Sub-step 3

3. **[Phase 3: High-Level Title]**
   - Sub-step 1
   - Sub-step 2
   - Sub-step 3

[Continue for all phases]

### Supporting Functions

- Cross-departmental task 1
- Cross-departmental task 2

## Clarifying Prompts (use as needed)
- "Can you confirm the company name and type if not clear from the transcript?"
- "Do you have specific departments or phases you want prioritized in the workflow?"
