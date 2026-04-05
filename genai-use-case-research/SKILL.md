---
name: research-genai-use-case-research
description: Research orchestrator for Generative AI use cases using Agent Teams. Coordinates peer teammates to discover, validate, and document GenAI implementations in specific industries. Use when researching GenAI use cases for an industry or when preparing client proposals.
---

# GenAI Use Case Research Skill

Coordinates peer research teammates to discover, validate, and document Generative AI implementations in specific industries using Claude Code Agent Teams.

## Why This Exists

This skill accelerates client proposal preparation and market research by systematically discovering proven GenAI implementations across an industry. Rather than manual searching, it creates a research team where teammates collaborate peer-to-peer to validate use cases with multiple sources, ensuring proposals contain credible, specific examples that resonate with prospects.

---

## COST WARNING

**Agent Teams use 3-10x more tokens than traditional subagents** due to:
- Peer-to-peer messaging overhead
- Shared task list synchronization
- Collaborative discovery patterns

Only use for research requiring cross-pollination between topics. For isolated research tasks, use traditional subagent spawning.

---

## Output Requirements

**CRITICAL: Display in Chat AND Save to File**

After generating the research report:
1. **Save to file:** Write to `{baseDir}/logs/genai-use-cases-[industry]-report.md`
2. **Display in chat:** Output the COMPLETE report (not just summary)

The user must see the full report without opening the file.

---

## Progress Notifications

Show progress after each step:
```
[STARTING] GenAI Use Case Research...
[INFO] Industry: [industry name]
[TEAM_CREATE] Creating research team...
[GENERATING] [N] search topics...
[COMPLETE] Topics generated: [N] company-focused, [M] theme-focused
[TASKS_CREATED] Created [N] research tasks on shared board
[LAUNCHING] Research teammate 1 (topics 1-3)...
[LAUNCHING] Research teammate 2 (topics 4-6)...
[LAUNCHING] Research teammate 3 (topics 7-9)...
[WAITING] All teammates launched - awaiting results...
[TEAMMATE_MSG] Teammate 1 → Teammate 2: "Found McKinsey report covering your topic"
[TEAMMATE_MSG] Teammate 3 → ALL: "Deduplication check: Is anyone covering Nike personalization?"
[TASK_UPDATE] Teammate 1 completed task [ID]: 3 use cases discovered
[TASK_UPDATE] Teammate 2 completed task [ID]: 2 use cases discovered
[COMPLETE] All teammates complete
[PROCESSING] Deduplicating [N] use cases...
[COMPLETE] Deduplicated: [M] unique use cases
[FILTERING] Filtering by quality...
[COMPLETE] Validated: [X] use cases (HIGH/MEDIUM confidence, 2+ sources)
[GENERATING] Generating final report...
[TEAM_DELETE] Cleaning up team resources...
[COMPLETE] Report saved to {baseDir}/logs/genai-use-cases-[industry]-report.md
```

---

## Session State Persistence

Write to `{baseDir}/logs/genai-research-session.md` after EVERY significant action:

```markdown
# GenAI Research Session
**Started:** [timestamp]
**Last Updated:** [timestamp]
**Industry:** [industry]
**Team Name:** genai-research-[timestamp]

## Progress
- [x] Step 1: Team created
- [x] Step 2: Topics generated - [N] topics
- [x] Step 3: Tasks created on shared board - [N] tasks
- [x] Step 4: Teammates launched - [3/3] active
- [ ] Step 5: Research collaboration - [2/3] tasks complete
- [ ] Step 6: Deduplication - pending
- [ ] Step 7: Quality filter - pending
- [ ] Step 8: Report generation - pending
- [ ] Step 9: Team cleanup - pending

## Team Status
| Teammate | Status | Tasks Claimed | Tasks Complete | Messages Sent |
|----------|--------|---------------|----------------|---------------|
| researcher-1 | active | 3 | 2 | 4 |
| researcher-2 | active | 3 | 1 | 2 |
| researcher-3 | active | 3 | 0 | 1 |

## Use Cases Collected
[JSON array of validated use cases so far]

## Peer Collaboration Log
- [timestamp] researcher-1 → researcher-2: "Cross-check: Nike personalization use case"
- [timestamp] researcher-3 → ALL: "Found comprehensive Gartner report at [URL]"

## Next Steps
[What to do when resuming]
```

**On completion:** Delete the session state file.

---

## Input Requirements

Parse from user request:
- **Industry**: Required (e.g., "apparel and footwear", "financial services")
- **Target count**: Default 5-10 validated use cases
- **Companies**: Optional specific companies to focus on
- **Output path**: Optional location to save results

---

## Workflow

### Phase 1: Create Research Team

```
TeamCreate("genai-research-[timestamp]")
```

This creates a shared task list visible to all teammates.

### Phase 2: Generate Search Topics

Based on industry, create 8-12 search topics covering:

**Major companies** (5-8 companies):
- Research industry leaders and their GenAI initiatives

**Application themes** (3-4 themes):
- Customer experience / personalization
- Content / marketing
- Operations / productivity
- Product development

### Phase 3: Create Shared Tasks

For each search topic, create a task on the shared board:

```
TaskCreate(
  subject="Research [topic]",
  description="Search for GenAI use cases related to [topic]. Validate with 2+ sources. Before deep-diving, message peers to check for overlap."
)
```

**CRITICAL:** All tasks created BEFORE spawning teammates, so they can self-claim from the board.

### Phase 4: Launch Research Teammates

Spawn 3-4 research teammates in a SINGLE message with multiple Task tool calls:

```
For each teammate:
  Task(
    prompt="You are a GenAI research teammate. Review the shared TaskList, claim unassigned tasks, and collaborate with peers using SendMessage. Follow the Research Collaboration Protocol.",
    team_name="genai-research-[timestamp]",
    model="sonnet"
  )
```

Each teammate:
1. Reviews shared TaskList
2. Claims unassigned tasks using TaskUpdate
3. Conducts research following worker methodology
4. Messages peers for deduplication and source sharing
5. Updates task status on completion

### Phase 5: Research Collaboration Protocol

Teammates MUST use peer-to-peer messaging for:

**Real-time deduplication:**
- Before deep-diving a use case, SendMessage to peers: "Anyone already covering [Nike personalization]?"
- Peers respond with status to avoid duplicate work

**Cross-industry discovery:**
- Healthcare teammate finds scheduling AI → messages Manufacturing teammate: "This patient scheduling pattern could apply to production scheduling"
- Enables cross-pollination across research topics

**Source sharing:**
- Teammate finds high-quality source → broadcasts to all: "Found comprehensive McKinsey report on [topic] at [URL]"
- All teammates leverage shared sources to strengthen validation

**Confidence boosting:**
- Teammate finds use case in only 1 source → messages peers: "Anyone encountered [use case] in your research?"
- If 2+ teammates confirm → validated
- Single mention → flagged as LOW confidence

**Message format:**
```
SendMessage(
  type="message",
  recipient="researcher-2",
  content="Checking: Are you covering Nike's GenAI personalization engine? I found it in my retail search.",
  summary="Deduplication check: Nike personalization"
)
```

**Broadcast format:**
```
SendMessage(
  type="broadcast",
  content="Found comprehensive Gartner 2025 GenAI report covering retail, healthcare, finance. URL: [link]. Relevant for everyone's validation.",
  summary="Shared resource: Gartner GenAI report"
)
```

### Phase 6: Collect and Deduplicate

As teammates complete tasks:
1. Monitor TaskList for completed status
2. Collect all discovered use cases from teammate outputs
3. Deduplicate by company + initiative name
4. Merge sources for same use cases found by multiple teammates
5. Incorporate peer validation flags from collaboration messages

### Phase 7: Quality Filter

Filter results:
- **INCLUDE**: HIGH or MEDIUM confidence
- **EXCLUDE**: LOW confidence or single-source only
- **EXCLUDE**: Non-GenAI (traditional ML that slipped through)

**Target threshold:** 5-10 validated use cases (ensures sufficient proof points for proposals without overwhelming detail)

### Phase 8: Generate Final Report

Structure output with:
- Executive Summary
- Use Cases by Category (CX, Content, Operations)
- Key Themes
- Collaboration Insights (cross-industry patterns discovered through peer messaging)
- Methodology

### Phase 9: Team Cleanup

```
SendMessage(type="shutdown_request", recipient="researcher-1")
SendMessage(type="shutdown_request", recipient="researcher-2")
SendMessage(type="shutdown_request", recipient="researcher-3")
TeamDelete()
```

---

## Research Collaboration Protocol

This section defines how teammates interact peer-to-peer during research.

### Deduplication Check (MANDATORY before deep-dive)

Before investing time in a use case, teammate MUST broadcast:
```
"Deduplication check: Is anyone covering [company + use case]?"
```

Peers respond within their next action:
- "Yes, I'm researching that" → First teammate pivots to different topic
- "No" or silence → Proceed with research

### Cross-Industry Pattern Sharing (PROACTIVE)

When teammate discovers a pattern applicable to other industries:
```
SendMessage to relevant peer: "Pattern alert: [Use case] in [Industry A] could apply to [Industry B]. Check if [Company B] has similar initiative."
```

### Source Broadcasting (HIGH-QUALITY sources only)

When teammate finds comprehensive source (e.g., McKinsey report, Gartner analysis):
```
Broadcast: "Shared resource: [Source title] covers [topics]. URL: [link]. Relevant for [which teammates]."
```

**Threshold:** Only broadcast sources covering 3+ use cases or authoritative industry reports.

### Validation Boost Request (SINGLE-source use cases)

When teammate finds promising use case with only 1 source:
```
Broadcast: "Validation request: Did anyone encounter [company + use case] in your research? I have 1 source, need confirmation."
```

If another teammate confirms → 2-source validation achieved → upgrade to MEDIUM confidence.

### Contradiction Resolution (CONFLICTING information)

If teammates find conflicting information about same use case:
```
SendMessage to peer: "Contradiction alert: My source says [claim A], your source says [claim B]. Which is more recent?"
```

Resolve by:
1. Source recency (newer wins)
2. Source authority (company official > press release)
3. Flag as "disputed" if unresolved

---

## Quality Checks

Before returning final report:

1. **Count check**: 5-10 use cases included (threshold: ensures proposal has proof points without overwhelming decision-maker)
2. **Diversity check**: No single company > 30% of use cases (threshold: prevents single-company bias, ensures broad market applicability)
3. **Source check**: Each use case has 2+ sources (threshold: prevents single-mention claims, requires editorial validation)
4. **GenAI check**: Each explicitly mentions GenAI technology (threshold: excludes traditional ML, AI-washing)
5. **Recency check**: All sources < 24 months old (threshold: ensures relevance to current market trends, avoids outdated examples)
6. **Metric check**: Each has at least one quantitative result (threshold: ensures concrete proof of ROI, not anecdotal)
7. **Collaboration check**: At least 2 instances of peer validation or cross-industry discovery logged (threshold: ensures team actually collaborated, not siloed work)

---

## Error Handling

| Error | Action |
|-------|--------|
| Teammate returns no results | Log task, don't retry same topic |
| Too few validated use cases | Create additional tasks, spawn new teammate |
| Context running low | Save session state, shut down teammates, return partial results |
| Teammate unresponsive | Send shutdown_request, spawn replacement if needed |
| Duplicate work despite protocol | Merge results during deduplication phase |

---

## Testing & Validation

**Unit-level tests:**
1. Team creation: Verify TeamCreate returns team ID, shared TaskList accessible
2. Topic generation: Verify 8-12 topics created, split between company (5-8) and theme (3-4)
3. Task creation: Confirm all topics converted to tasks before teammate spawn
4. Teammate spawning: Verify all teammates join same team, can access TaskList
5. Collaboration messaging: Test SendMessage peer-to-peer and broadcast functionality
6. Task claiming: Verify teammates can claim unassigned tasks via TaskUpdate
7. Deduplication: Test merge logic with duplicate company + initiative names across teammates
8. Quality filter: Verify HIGH/MEDIUM confidence retained, LOW/single-source excluded
9. Team cleanup: Confirm TeamDelete removes shared resources, teammates shut down

**Integration tests:**
1. End-to-end with real industry: Run full workflow on test industry (e.g., "healthcare"), verify 5-10 use cases returned
2. Peer collaboration: Verify at least 2 peer messages logged in session state
3. Cross-validation: Test single-source use case upgraded to MEDIUM via peer confirmation
4. Session persistence: Interrupt mid-workflow, verify session state file created and resumable
5. File output: Confirm report saved to correct path with collaboration insights section
6. Empty results handling: Test workflow when topic yields no results (should not crash, log gracefully)

**Validation criteria:**
- No use case appears twice in final report
- All use cases pass quality checks (2+ sources, GenAI mention, quantitative metric)
- At least 2 collaboration events logged (deduplication, source sharing, or cross-validation)
- Report generates and saves within 10 minutes for standard industry research (longer than subagent version due to messaging overhead)
- Progress notifications display teammate messages correctly
- Team resources cleaned up on completion (no orphaned TaskList or teammates)

---

## Tools Used

- TeamCreate - Initialize research team with shared TaskList
- TaskCreate - Add research topics to shared board
- Task - Spawn research teammates that join the team
- SendMessage - Peer-to-peer collaboration during research
- TaskUpdate - Teammates claim and complete tasks
- TaskList - Monitor progress across all teammates
- TeamDelete - Clean up team resources on completion
- WebSearch - Topic generation and research validation
