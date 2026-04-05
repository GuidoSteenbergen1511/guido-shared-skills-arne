# Demo Type Asset Matrix

Use this matrix to determine the minimum required assets per demo type.

| Demo Type | Required Files | Required Folders | Notes |
|----------|----------------|------------------|-------|
| Custom GPT | `GPT_Configuration.md`, prompt(s) | `Prompts/`, `Demo_Docs/`, `Custom_GPT_Knowledge_Docs/`, `Backup_Outputs/` | Demo_Docs must be input-only; outputs go to Knowledge or Backup |
| Agent Swarm | `Agentic_Swarm_Architecture.md` | `Prompts/`, `Demo_Docs/`, `Backup_Outputs/` | Demo_Docs must be input-only; outputs go to Backup |
| Prompt-only | prompt file(s) | `Prompts/`, `Demo_Docs/`, `Backup_Outputs/` | Demo_Docs must be input-only; outputs go to Backup |
| Hybrid | GPT config + swarm prompt | `Prompts/`, `Demo_Docs/`, `Custom_GPT_Knowledge_Docs/`, `Backup_Outputs/` | Document which parts are GPT vs swarm |

Checklist:
- [ ] Demo folder matches repo naming convention
- [ ] Demo_Instructions.md exists
- [ ] Demo_Docs contains only inputs (client or approved synthetic)
- [ ] Output examples are in Custom_GPT_Knowledge_Docs or Backup_Outputs
- [ ] Backup outputs exist and match current prompts
- [ ] QA checklist completed
