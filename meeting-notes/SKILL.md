---
name: communications-meeting-notes
description: Creates standardized meeting notes with decisions, action items, and key outcomes. Use when documenting meetings, summarizing transcripts, or preparing follow-ups to ensure consistent capture of decisions and accountability.
---

# Meeting Notes Format

Standardized format for documenting meetings. Ensures consistent, actionable meeting notes across the organization.

## Why This Exists

Meeting notes are the source of truth for decisions and accountability. A standard format ensures nothing is lost between meetings, action items have clear owners, and follow-ups are traceable. This is critical for client relationships, internal coordination, and legal records on project scope changes.

## When to Use This Skill

**Triggers:**
- Creating meeting notes during or after meetings
- Summarizing meeting transcripts from Fireflies, Otter, or similar
- Documenting decisions and tracking accountability for action items
- Preparing meeting follow-up emails with structured context
- Extracting key decisions from client calls for CRM or project files

## Standard Meeting Notes Template

```markdown
# [Meeting Title]

**Date**: [YYYY-MM-DD]
**Time**: [HH:MM - HH:MM]
**Attendees**: [Name 1], [Name 2], [Name 3]
**Meeting Type**: [Discovery / Workshop / Project Sync / Internal / Other]

---

## Summary

[2-3 sentences capturing the essence of the meeting and main outcome]

---

## Key Decisions

| Decision | Rationale | Owner |
|----------|-----------|-------|
| [Decision 1] | [Why this was decided] | [Who owns it] |
| [Decision 2] | [Why this was decided] | [Who owns it] |

---

## Action Items

| Action | Owner | Deadline | Status |
|--------|-------|----------|--------|
| [Action 1] | [Name] | [Date] | [PENDING] |
| [Action 2] | [Name] | [Date] | [PENDING] |

---

## Discussion Notes

### Topic 1: [Topic Title]

[Key points discussed, insights shared, concerns raised]

### Topic 2: [Topic Title]

[Key points discussed, insights shared, concerns raised]

---

## Quotes Worth Capturing

> "[Verbatim quote from someone that's worth remembering]"
> — [Name], [Role]

---

## Next Meeting

**Date**: [If scheduled]
**Agenda preview**: [What will be covered]

---

## Parking Lot

Items raised but not addressed:
- [Item 1]
- [Item 2]
```

## Meeting Type Variations

### Discovery Call Notes

Focus on:
- Client pain points and challenges
- Current state / desired state
- Decision criteria and timeline
- Stakeholders and their roles
- Budget indicators
- Next steps

### Workshop Notes

Focus on:
- Session objectives and outcomes
- Exercises completed
- Key insights from participants
- Ideas generated (prioritized)
- Follow-up commitments

### Project Sync Notes

Focus on:
- Progress since last meeting
- Blockers and dependencies
- Scope changes or risks
- Timeline adjustments
- Action items with specific deadlines

### Internal Strategy Notes

Focus on:
- Strategic options considered
- Decision rationale
- Resource implications
- Timeline and milestones
- Owner assignments

## Action Item Rules

**Every action item MUST have:**
1. **Clear description** - What exactly needs to be done
2. **Single owner** - One person responsible (not "team" or "we")
3. **Specific deadline** - Date, not "soon" or "next week"
4. **Status tracking** - [PENDING] / [COMPLETE] / [BLOCKED]

**Good action items:**
- [GOOD] "[Name]: Send proposal by Friday Jan 10"
- [GOOD] "Client (Jan): Confirm budget approval by Jan 15"

**Bad action items:**
- [BAD] "Follow up on proposal" (who? when?)
- [BAD] "Team to discuss next steps" (no owner)

## Quote Extraction Guidelines

Capture quotes that are:
- **Insight-rich**: Reveal something important about needs or thinking
- **Decision-making**: Show how decisions were reached
- **Testimonial-worthy**: Could be used in case studies
- **Risk indicators**: Signal concerns or hesitation

Always attribute with name and role.

## Storage Locations

| Meeting Type | Save Location |
|--------------|---------------|
| Client meeting | `{projectFolder}/01. Internal/Meeting Notes/` |
| Internal meeting | `{baseDir}/projects/Internal/Meeting Notes/` |
| Sales discovery | CRM note |

## Integration with Other Skills

- **chief-of-staff-action-tracking**: Extract action items for tracking
- **communications-email-writer**: Convert notes to follow-up email
- **project-management-project-closing**: Use notes as evidence for project outcomes

## Testing & Validation

When validating meeting notes:
1. **Action items completeness**: Each item has owner (single name/role), specific date (not relative), and clear verb phrase
2. **Decision traceability**: Each decision includes rationale (the "why") to prevent revisiting closed issues
3. **Quote attribution**: All quotes include name and role to enable follow-up or case study usage
4. **Parking lot accuracy**: Items in parking lot are genuinely out-of-scope for this meeting, not forgotten action items
5. **Status consistency**: All action item statuses are in standard format ([PENDING], [COMPLETE], [BLOCKED]) for tracking integration

**Magic Numbers:**
- **2-3 sentences for Summary**: Enough detail to understand outcome without requiring full notes review
- **3 meeting type variations documented**: Discovery, Workshop, Project Sync, Internal Strategy—covers 95% of use cases
- **4 mandatory action item fields**: Description, owner, deadline, status—minimum viable for accountability

