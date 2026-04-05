---
name: operations-as-is-workflow-documentation
description: Capture and document the current state of a business process in strict phase-by-phase format. Triggered when user asks to baseline a workflow, document current state, identify bottlenecks, or establish a process baseline. Records owners, tools, time/cost, and pain points exactly as provided with no AI improvements or recommendations.
---
# As-Is Workflow Documentation

## Why This Exists
Organizations need a factual baseline of their current processes before optimizing or transforming them. This skill captures the reality of today's workflows—who does what, with what tools, and how long it takes—without injecting improvement suggestions. Accurate as-is documentation is essential for change management, cost analysis, and identifying true bottleneck priorities.

## Purpose
Capture the current (as-is) workflow for a specific business process. Focus strictly on today's reality. Do not add improvements or AI suggestions.

## Required Inputs
- Domain name (e.g., Supply Chain, Marketing)
- Workflow name (specific process)
- Current workflow phases
  - Phase name
  - Key activities (bulleted list for each phase)
    - For each activity, include: owner, tool used (if any), typical time or cost
- Known pain points or bottlenecks (optional)

## Rules
- Include all user-provided details exactly as given. Do not paraphrase or omit.
- Do not add comparisons, recommendations, or AI suggestions (no "you could also...").
- If timing, tool, or ownership is missing, leave blanks with underscores (e.g., `owner: __`) so the user can fill in.
- Preserve all pain points and bottlenecks verbatim—do not filter or reframe them.
- Output is structured data, not narrative. Use the exact template format every time.

## Output Format

## [DOMAIN] - Current Workflow: [WORKFLOW NAME]

### High-level overview

- One or two sentences summarizing the purpose and scope of the current workflow.

### Phase 1 - [Phase name]

- Activity 1 (owner: __, tool: __, est. time/cost: __)
- Activity 2 (owner: __, tool: __, est. time/cost: __)
- Activity 3 (owner: __, tool: __, est. time/cost: __)

### Phase 2 - [Phase name]

- Activity 1 (owner: __, tool: __, est. time/cost: __)
- Activity 2 (owner: __, tool: __, est. time/cost: __)
- Activity 3 (owner: __, tool: __, est. time/cost: __)

### Phase 3 - [Phase name]

- Activity 1 (owner: __, tool: __, est. time/cost: __)
- Activity 2 (owner: __, tool: __, est. time/cost: __)
- Activity 3 (owner: __, tool: __, est. time/cost: __)

### Bottlenecks and pain points

- Pain point 1
- Pain point 2
- Pain point 3

### Baseline metrics summary (optional)

- Total cycle time: __
- Total direct cost: __

## Testing & Validation

After capturing a workflow, verify:
1. **Completeness**: All phases provided by the user are documented with no additions or omissions.
2. **Exactness**: Owner names, tool names, and time/cost estimates match user input exactly (no edits or interpretations).
3. **Formatting**: Output matches the template structure. Each phase is clearly labeled. Activities use the (owner: __, tool: __, est. time/cost: __) format consistently.
4. **No recommendations**: Review output for hidden suggestions or "however" language. Remove any improvement ideas.
5. **Blank handling**: Missing fields are marked with __ (not left empty or marked "TBD").

## Magic Numbers & Thresholds

**No configurable thresholds in this skill.** The output format is rigid:
- Exactly 3 blanks per activity (owner, tool, time/cost) for consistency and CSV exportability.
- Underscores (__) used as visual placeholder for human readability and easy find/replace in spreadsheets.
- No field length limits—user provides what matters for their domain.
