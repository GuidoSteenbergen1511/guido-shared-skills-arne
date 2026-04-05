# Use Case Output Template

## Per Use Case Structure

```markdown
## [Company] - [Initiative Name]
**Confidence:** [HIGH/MEDIUM] | **Sources:** [N]

### Problem Solved
[1-2 sentences describing the business challenge addressed]

### How They Did It
- **GenAI Technology:** [GPT-4 / Claude / DALL-E / Gemini / Custom LLM / etc.]
- **Vendor/Platform:** [OpenAI / Anthropic / Google / Azure / AWS Bedrock / In-house]
- **Implementation:** [API integration / Fine-tuned / RAG / Agent / etc.]
- **Deployment:** [Customer-facing / Internal / B2B platform]

### Quantitative Results
| Metric | Value | Source |
|--------|-------|--------|
| [Metric name] | [+X% / -X% / Nx] | [[Source 1]] |
| [Metric name] | [Value] | [[Source 2]] |

### Sources
1. **[Source 1 Title]** ([Publisher], [Date])
   - URL: [full URL]
   - Confirms: [what this source validates]

2. **[Source 2 Title]** ([Publisher], [Date])
   - URL: [full URL]
   - Confirms: [what this source validates]

3. **[Source 3 Title]** ([Publisher], [Date]) [if available]
   - URL: [full URL]
   - Confirms: [what this source validates]
```

---

## Example: Completed Use Case

```markdown
## Zalando - AI Fashion Assistant
**Confidence:** HIGH | **Sources:** 3

### Problem Solved
Customers struggled to find the right products among millions of SKUs, leading to decision fatigue and high return rates.

### How They Did It
- **GenAI Technology:** GPT-4o mini (migrated from GPT-3.5)
- **Vendor/Platform:** OpenAI API
- **Implementation:** Custom fashion-trained model with RAG on product catalog
- **Deployment:** Customer-facing assistant across 25 European markets in 20+ languages

### Quantitative Results
| Metric | Value | Source |
|--------|-------|--------|
| Basket size increase | +40% | [OpenAI Case Study] |
| Product clicks | +23% | [Zalando Corporate] |
| Return rate reduction | 5-10% | [TacticOne Analysis] |
| Session duration | +52% vs generic chatbots | [OpenAI Case Study] |

### Sources
1. **OpenAI Customer Story: Zalando** (OpenAI, Oct 2024)
   - URL: https://openai.com/index/zalando/
   - Confirms: Technology choice (GPT-4o mini), traffic scaling (12x), migration timeline

2. **Inspiring and Empowering Customers** (Zalando Corporate, 2024)
   - URL: https://corporate.zalando.com/en/technology/inspiring-and-empowering-customers-ai-powered-experiences
   - Confirms: Market reach (25 markets), customer engagement metrics

3. **How Zalando Uses AI** (TacticOne, 2024)
   - URL: https://www.tacticone.co/blog/how-zalando-uses-ai-to-inspire-engage-and-reduce-returns
   - Confirms: Return rate impact, sizing technology integration
```

---

## Confidence Scoring

### HIGH Confidence
- 3+ independent sources
- Metrics consistent across sources
- Primary source is company official (press release, case study)
- Recent (within 18 months)

### MEDIUM Confidence
- 2 independent sources
- Metrics may have minor variance (±10%)
- At least one credible news/analyst source
- Reasonably recent (within 24 months)

### LOW Confidence (EXCLUDE)
- Single source only
- Metrics conflict between sources
- Only unverified blog posts
- Older than 24 months
- Cannot confirm GenAI technology specifically

---

## Final Report Structure

```markdown
# GenAI Use Cases: [Industry]
*Research Date: [Date]*
*Total Validated: [N] use cases*

## Executive Summary
[2-3 sentence overview of key findings]

## Use Cases

### Category 1: [e.g., Customer Experience]
[Use case 1]
[Use case 2]

### Category 2: [e.g., Content & Marketing]
[Use case 3]
[Use case 4]

### Category 3: [e.g., Operations]
[Use case 5]

## Key Themes
- [Theme 1]: [Companies doing this]
- [Theme 2]: [Companies doing this]

## Methodology
- Sources searched: [N]
- Use cases discovered: [N]
- Use cases validated: [N]
- Excluded (single source): [N]
- Excluded (not GenAI): [N]
```
