# Condensing Guide for <8000 Character Prompts

This guide provides detailed strategies for reducing prompt length while preserving functionality.

---

## Why 8000 Characters?

Custom GPTs in ChatGPT have an 8000 character limit for instructions. Prompts exceeding this limit cannot be used as custom GPT configurations.

---

## Condensing Priority Order

Apply these strategies in sequence until under 8000 characters:

### Level 1: Example Reduction (Saves 500-2000 chars)

Before:
```
# Output example:

Example 1: Simple query
User: What is your return policy?
Response: Our return policy allows returns within 30 days...

Example 2: Complex query
User: I bought something but it arrived damaged...
Response: I'm sorry to hear that your item arrived damaged...

Example 3: Edge case
User: Can I return a gift?
Response: Yes, gifts can be returned...
```

After:
```
# Output example:

User: What is your return policy?
Response: Our return policy allows returns within 30 days of purchase. Would you like details on how to initiate a return?
```

### Level 2: Guideline Compression (Saves 300-1000 chars)

Before:
```
# Guidelines

- Always greet the user with a warm and friendly message at the start of each conversation

- Before providing any solution, make sure to ask clarifying questions to understand the full context of the user's issue

- When explaining technical processes, break them down into numbered step-by-step instructions that are easy to follow

- If you encounter a problem that is beyond your capabilities, offer to escalate the conversation to a human support agent
```

After:
```
# Guidelines

- Greet warmly

- Ask clarifying questions first

- Use step-by-step instructions

- Escalate when needed
```

### Level 3: Description Condensing (Saves 200-500 chars)

Before:
```
You are a customer support assistant working for a Software-as-a-Service company that provides project management tools to businesses of all sizes. Your primary responsibilities include helping users troubleshoot technical issues they encounter while using the platform, answering questions about the various features and capabilities of the software, and identifying when issues need to be escalated to human support agents for more complex resolution.
```

After:
```
You are a customer support assistant for a SaaS project management tool. Help users troubleshoot issues, answer feature questions, and escalate complex problems when needed.
```

### Level 4: Structural Simplification (Saves 500-1500 chars)

Remove optional sections entirely:

- Background/context sections

- Multiple input format descriptions

- Detailed constraint explanations

- "Nice to have" behaviors

Keep only:
- Role description (1-2 sentences)
- Core guidelines (3-5 bullets max)
- Output format (brief)
- One example

---

## Character Counting Tips

### Quick Estimation

- One line of text ~ 60-80 characters

- One bullet point ~ 40-100 characters

- One example block ~ 300-800 characters

- Section header + content ~ 200-500 characters

### Accurate Counting

Use this command to count characters in a markdown file:
```bash
wc -c filename.md
```

Or in Python:
```python
len(open('filename.md').read())
```

---

## Common Patterns

### Before/After: Role Description

Full (~400 chars):
```
You are an expert data analyst assistant designed to help business users understand their data, create visualizations, write SQL queries, and interpret statistical results. You have deep knowledge of databases, spreadsheets, and business intelligence tools. You communicate complex technical concepts in simple terms that non-technical users can understand.
```

Condensed (~180 chars):
```
You are a data analyst assistant helping business users understand data, create visualizations, and write queries. Explain technical concepts simply.
```

### Before/After: Output Format

Full (~350 chars):
```
# Output format:

Structure your responses in the following format:
1. Summary: A brief one-sentence summary of the answer
2. Details: The full explanation with relevant context
3. Next Steps: Suggested actions the user can take
4. Related Topics: Other areas they might want to explore
```

Condensed (~150 chars):
```
# Output format:

1. Summary (one sentence)
2. Details with context
3. Suggested next steps
```

---

## Preservation Rules

Never remove or condense:

- The opening "You are..." statement

- The core task definition

- The `# Output format:` section

- At least one concrete example

- Critical safety or behavioral constraints

---

## Quality Check

After condensing, verify:

- [ ] Under 8000 characters

- [ ] Core functionality preserved

- [ ] At least one example remains

- [ ] Output format is clear

- [ ] No critical rules removed

- [ ] Still reads naturally (not just keywords)
