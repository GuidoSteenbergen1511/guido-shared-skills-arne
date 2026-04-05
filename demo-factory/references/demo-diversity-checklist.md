# Demo Diversity Checklist

Purpose: turn "ensure diversity" into explicit, checkable coverage rules.

## 1) Core coverage (always required)
- [ ] Simple Prompts demo included.
- [ ] AI Assistants demo included (Custom GPTs / Claude Projects / Gemini Gems).

## 2) Capability coverage (minimum mix)
- [ ] At least 1 Standard demo (Deep Research OR Agentic Workflows OR Excel/Data OR Automation OR Coding Tools OR Interactive Artifacts).
- [ ] At least 1 Business Context demo (Cost/ROI OR Security/Governance OR Communication Assistants).
- [ ] Specialized demo included only if audience fit is clear (Image/Video OR MCPs OR Voice OR Multi-Model Comparison OR Enterprise Agents).

## 3) Audience-fit requirements
Choose the closest audience profile and ensure these appear:
- Executive: Simple Prompts + Deep Research + Cost/ROI + Multi-Model Comparison.
- Technical/IT: Simple Prompts + AI Assistants + Automation + MCPs or Coding Tools.
- Operations: Simple Prompts + AI Assistants + Communication Assistants + Excel/Data.
- Marketing/Creative: Simple Prompts + AI Assistants + Image/Video + Interactive Artifacts.
- Mixed/General: Simple Prompts + AI Assistants + Deep Research + Agentic Workflows.

## 4) Platform mix rule
- [ ] Use at least 2 LLM platforms when audience is mixed or executive (e.g., ChatGPT + Claude).
- [ ] Include ecosystem-native platform when relevant (M365 -> Copilot, Google Workspace -> Gemini).

## 5) Format diversity (delivery mode)
- [ ] At least one live build.
- [ ] At least one prepared-live hybrid (paste pre-written content, then run live).
- [ ] At least one pre-built walkthrough for higher-risk or longer demos.
- [ ] Apply 80/20 rule: ~80% pre-built, ~20% live build time.

## 6) Data-type diversity
- [ ] Unstructured text/doc demo included.
- [ ] Structured data demo included (spreadsheet/CSV/BI).
- [ ] Optional: voice or image data only if audience fit is clear.

## 7) Complexity mix
- [ ] One quick-win demo (5-10 min).
- [ ] One deeper demo (15-30+ min) with clear business or automation payoff.

## 8) Tool switching plan
- [ ] 3-phase flow documented: LLM comparison -> Specialized tools -> Automation.
- [ ] Demo depth ratio: ~70% time on 3-4 core tools, ~30% on breadth awareness.

## 9) Documentation tags (per demo)
Add to each Demo_Instructions.md:
- Demo Type(s)
- Platform(s)
- Audience fit
- Data type(s)
- Delivery mode (live / prepared-live / pre-built)
- Estimated duration

## 10) Exceptions
- Any skipped checklist item must include a short rationale in Master_Demo_Sequence_Guide.md.
