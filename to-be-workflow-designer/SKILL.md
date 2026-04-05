---
name: operations-to-be-workflow-designer
description: Designs an AI-augmented (to-be) version of an existing workflow with new time estimates, tool mapping, and efficiency gains. Use when asked for to-be workflow design, AI-augmented workflow transformation, or process optimization with GenAI tools.
---
# To-Be Workflow Designer

## Why This Exists

Customers need concrete evidence that GenAI tooling reduces cycle time, improves quality, and lowers costs. This skill transforms as-is workflows into actionable to-be designs with specific tools, time estimates, and efficiency metrics—enabling clients to prioritize automation investments and justify resource allocation.

## Purpose
Create the AI-augmented (to-be) version of a workflow that has an existing as-is baseline. Show how GenAI improves speed, cost, and quality.

## When to Use This Skill

Invoke this skill when:
- A customer has mapped their current (as-is) workflow and baseline time estimates
- They request a GenAI-optimized redesign with tool mapping
- You need to demonstrate time/cost/quality improvements from specific AI tools
- Clients are evaluating workflow automation ROI

## Required Inputs
- Current (as-is) workflow with time estimates (from earlier in the session or provided document)
- Workflow name
- Tool list to use for mapping (if provided)

## Rules
- Do not repeat the full as-is workflow; only use it for time baselines.
- Every step in the to-be workflow must include:
  - Numbered label (e.g., 1.1, 1.2, 1.3)
  - Time estimate
  - Tool name(s)
  - Connection note: "-> Connects to: X.X"
- If tool list is not provided, ask for it before finalizing tool mapping.

## Output Structure

# [TITLE: Workflow Name] Transformation - AI-Augmented Workflow

## Overview
Describe how GenAI transforms the workflow and the expected impact.

## [WORKFLOW NAME]: Use Case Description
Provide a 2-3 paragraph summary of business purpose, strategic value, and pain points addressed.

## AI-Augmented Workflow

**New Timeline:** [X days/hours]
**Estimated Monthly AI Cost:** [-]

### Phase 1: [Phase Name]

- **1.1 [New AI-powered activity]** (Time estimate: X minutes/hours, Tool: [Tool]) -> Connects to: 1.2
- **1.2 [New AI-powered activity]** (Time estimate: X minutes/hours, Tool: [Tool]) -> Connects to: 1.3
- **1.3 [New AI-powered activity]** (Time estimate: X minutes/hours, Tool: [Tool]) -> Connects to: 2.1

### Phase 2: [Phase Name]

- **2.1 [New AI-powered activity]** (Time estimate: X minutes/hours, Tool: [Tool]) -> Connects to: 2.2
- **2.2 [New AI-powered activity]** (Time estimate: X minutes/hours, Tool: [Tool]) -> Connects to: 2.3
- **2.3 [New AI-powered activity]** (Time estimate: X minutes/hours, Tool: [Tool]) -> Connects to: 3.1

### Phase 3: [Phase Name]

- **3.1 [New AI-powered activity]** (Time estimate: X minutes/hours, Tool: [Tool]) -> Connects to: 3.2
- **3.2 [New AI-powered activity]** (Time estimate: X minutes/hours, Tool: [Tool]) -> Connects to: 3.3
- **3.3 [New AI-powered activity]** (Time estimate: X minutes/hours, Tool: [Tool]) -> Connects to: 4.1

### Phase 4: [Phase Name]

- **4.1 [New AI-powered activity]** (Time estimate: X minutes/hours, Tool: [Tool]) -> Connects to: 4.2
- **4.2 [New AI-powered activity]** (Time estimate: X minutes/hours, Tool: [Tool]) -> Connects to: 4.3
- **4.3 [New AI-powered activity]** (Time estimate: X minutes/hours, Tool: [Tool]) -> Connects to: end

### New Efficiencies Gained

- Efficiency 1
- Efficiency 2
- Efficiency 3

## Tool Selection Instructions
When a tool list is provided, map each workflow step to the most appropriate tool. For each step:
- Explain how GenAI creates efficiency
- Name the specific tool(s)
- Add a short italic description of how the tool is used
- If multiple tools apply, separate with a slash ("Tool A / Tool B")

## Testing & Validation

Verify the to-be design by:
1. **Time validation**: Total time is 30-70% of original as-is workflow (document rationale for outliers)
2. **Tool coverage**: Every step is mapped to a named, available tool (no generic "AI" references)
3. **Efficiency claim accuracy**: Each efficiency gained is tied to specific steps and measurable (e.g., "3.2 reduces manual review by 80% via AI screening")
4. **Connection integrity**: All numbered steps connect forward with no orphaned phases
5. **Cost realism**: Monthly AI costs are estimated based on actual tool pricing or stated assumptions
6. **Business alignment**: Efficiency gains address the original as-is pain points identified by the customer

## Magic Numbers & Rationale

| Value | Rationale |
|-------|-----------|
| 30-70% of as-is time | Realistic GenAI acceleration—full automation is rare; most workflows benefit from hybrid human-AI. Conservative ranges build credibility. |
| 2-3 phases (typical) | Most workflows decompose into discovery, execution, review/refinement—avoid >4 phases unless workflow is inherently complex |
| 1-3 tools per step | More tools per step increases cognitive load; sequence steps into phases instead |
| Monthly AI cost line | Required for ROI calculation; if unknown, state "To be determined pending tool selection" |
