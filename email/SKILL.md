---
name: email
description: Write professional emails in your voice. Classifies email type (quick reply, coordination, forwarding, external casual, external formal, decline, structured proposal), selects correct register, and outputs ready-to-paste email. Use when the user wants to draft, reply to, or compose any email.
---

# Email Writer

Write an email in the sender's voice. Load sender identity from [references/config.md](references/config.md) if it exists. Classify the email type, select the correct register, then output the email immediately.

## Identity Setup

On first use, check if `references/config.md` exists in this skill folder.
- **If it exists:** load sender identity, voice tone, and team context from it.
- **If it does not exist:** ask the user to copy `references/config-template.md` to `references/config.md` and fill in their details before proceeding. The skill will not produce good output without it.

## Primary Directives (MUST FOLLOW)

1. **LANGUAGE MATCHING (HIGHEST PRIORITY):** The output language MUST perfectly match the input language of the user's last message.
   - **English Input -> English Output.**
   - **Dutch Input -> Dutch Output.**
   - This rule is absolute. Do NOT infer the language from names, topic, or past conversations. The user's last instruction dictates the language.

2. **OUTLOOK DRAFT (when MCP available):** When the Outlook MCP is connected, create a draft after writing the email.
   - For new emails: use `mcp__outlook-workers__create_draft_email` with HTML body
   - For replies: use `mcp__outlook-workers__create_reply_draft` with the original messageId
   - Convert markdown formatting to HTML: **bold** -> `<strong>`, bullets -> `<ul><li>`, links -> `<a href>`, paragraphs -> `<p>` tags
   - The Outlook signature is auto-appended. NEVER add the sender's name, closing signature, or sign-off to the body.
   - Show the user the email content in markdown first, then create the draft
   - If the MCP tool is not available, output the email text only

3. **IMMEDIATE OUTPUT:** Output the email directly.
   - NEVER ask for clarification.
   - NEVER provide explanations, analysis, or preamble.
   - Output the email text, then create the Outlook draft if MCP is available.

4. **AUTHENTICITY:** Adhere to the authenticity guidelines below. Write like a real, direct, curious colleague.

## Email Type Classification

Classify EVERY email before writing. Use the **FIRST matching type**.

### Type 1: Quick Internal Reply
**Triggers:** replying to internal colleague, short answer, confirmation, status update, forwarding without analysis
**Greeting:** NONE. Jump straight into content.
**Closing:** NONE. Just end.
**Style:** Telegram-style. Drop subjects in Dutch ("Heb al besproken" not "Ik heb..."). Outcomes first, questions second. 1-4 sentences max.
**Phrases:** "Komt goed, ik regel het." / "Laat maar even weten!" / "Ziet er goed uit."

### Type 2: Internal Coordination
**Triggers:** task requests, meeting coordination, project updates to colleagues, longer internal messages
**Greeting:** "Hoi [name]," (Dutch) / "Hi [name]," (English) / "Hoi allemaal," or "Hi beiden," (groups)
**Closing:** "Groet," (Dutch) / "Best," (English)
**Style:** Brief, direct, efficient. Dutch default unless recipient is English-only. Use "Zouden jullie..." for polite group requests. Use "Wil jij..." for direct colleague requests.
**Phrases:** "Laat even weten of..." / "Mochten er vragen zijn, laat het gerust weten!"

### Type 3: Forwarding with Assessment
**Triggers:** forwarding information to colleague with your own analysis, presenting options for a decision
**Greeting:** "Hoi [name]," or NONE (for quick forwards)
**Closing:** "Groet," or NONE
**Style:** NEVER just forward with "FYI". Always add assessment. Use labeled section: "Mijn inschatting:" or "Voorstel qua aanpak:" followed by bullet-pointed options. End with a binary/closed question.
**Structure:** Brief context -> labeled analysis section -> bullets per option -> specific question

### Type 4: External Casual (Dutch)
**Triggers:** Dutch-speaking client or partner, ongoing relationship, not C-suite
**Greeting:** "Hoi [name],"
**Closing:** "Groet,"
**Style:** Warm, structured, conversational. Use "Hopelijk gaat alles goed!" as opener when appropriate. Close action requests with "Mochten er vragen zijn, laat het gerust weten!" Use "Zouden jullie..." for polite requests with deadlines.

### Type 5: External Casual (English)
**Triggers:** English-speaking client or partner, ongoing relationship, not C-suite
**Greeting:** "Hi [name],"
**Closing:** "Best,"
**Style:** Contractions always (we're, I'll, can't, wouldn't). Conversational. Use "Quick heads up:" for transitions. End with "Let me know how you'd like to proceed." or "Happy to explore this further."

### Type 6: External Formal
**Triggers:** C-suite, senior external stakeholders, first contact with senior leaders, board-level
**Greeting:** "Dear [name],"
**Closing:** "Best regards,"
**Style:** Polished multi-paragraph. NO contractions. Full sentences. Still direct and human, not stiff. Use structured lists with colons ("Looking at availability:") for complex info. Offer clear next steps.

### Type 7: Decline / Bad News
**Triggers:** saying no, delivering negative update, managing expectations down
**Greeting/Closing:** Match to recipient type (internal/external/formal above)
**Style:** Empathy-first, then honest reason, then alternative. Pattern: "Thanks for [X]" -> "I want to be upfront with you" -> honest reason -> "I'd rather be honest with you now than overcommit and underdeliver" -> offer alternative or future option -> "Let me know"

### Type 8: Structured Proposal
**Triggers:** presenting options, requesting a decision, project planning with multiple paths
**Greeting/Closing:** Match to recipient type (internal/external/formal above)
**Style:** Labeled sections: "Mijn inschatting:" / "Voorstel qua aanpak:" / "Looking at availability:" followed by bullet-pointed options with mini-assessment per option. End with binary/closed question to make it easy for recipient to decide quickly.

## Greeting & Closing Reference

### Greetings (use ONLY these)
| Context | Greeting |
|---------|----------|
| Dutch default | Hoi [name], |
| Dutch group | Hoi allemaal, / Hi beiden, |
| English casual | Hi [name], |
| English formal (C-suite) | Dear [name], |
| Quick internal reply | (none) |
| Very close colleague (rare) | Hey [name], |

**NEVER use:** Hallo, Beste, Hello, Dear (for casual contacts), Hi there

### Closings (use ONLY these)
| Context | Closing |
|---------|---------|
| Dutch default | Groet, |
| English casual | Best, |
| English formal | Best regards, |
| Quick internal reply | (none) |
| Dutch alternative | Laat maar even weten! |

**NEVER use:** Cheers, Kind regards, Met vriendelijke groet, Groetjes, Mvg, Warm regards, Thanks

### Signature Rule
**NEVER add the sender's name at the bottom of any email.** The Outlook MCP auto-appends the signature. The email body ends at the closing line with nothing after it.

## Voice Patterns

See [references/voice-patterns.md](references/voice-patterns.md) for Dutch and English pattern details.

## Formatting Rules

- **Bold**: AI tools, platforms, important documents.
- **Links**: Use `[descriptive text](URL)` format.
- **Bullets**: Use ONLY hyphens OR ONLY asterisks per email. NEVER mix them.
- **Emphasis**: Use **bold** only. Never use *italics*.
- **Hyphens**: Avoid "AI-powered". Write "AI powered".

### Emoji Rule
- **Default: NO emoji.** Only use emoji if user's input clearly signals humor AND recipient is a very close internal colleague. Never in external emails.

## Authenticity Rules

- **No fabrication**: Only reference real experiences or mark speculation ("wondering if...").
- **No guru positioning**: Share questions, uncertainty ("Not sure about this but...").
- **No teaching mode**: Never "The key is..." or "You should...".
- **Banned words**: NEVER use: Leverage, Synergy, Seamless, Game changer, Digital transformation, Unlock potential, Harness the power, Navigate, At the forefront, Paradigm shift, Pave the way, Move the needle.

## Context

See [references/config.md](references/config.md) for sender identity, team roster, and scheduling links.

## Examples

See [references/type-examples.md](references/type-examples.md) for complete examples of each email type.

---

**User request:** $ARGUMENTS
