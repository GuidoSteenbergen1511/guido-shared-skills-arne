# AI Workshop Facilitation Guide

# AI Workshop Facilitation Guide

> Comprehensive evidence-based methodology for facilitating AI workshops, based on analysis of 30+ actual workshops. Covers demo selection, sequencing, delivery techniques, failure recovery, and complexity calibration.
> 

<aside>
🎯

For detailed descriptions of each demo type, platform capabilities, and the demo catalog, see [Demo Types & AI Capability Categories](https://www.notion.so/Demo-Types-AI-Capability-Categories-d78e32cbdeff427482ccd673ddbcd7de?pvs=21).

</aside>

**Last Updated**: January 2026
**Based On**: Analysis of 30 real workshops

---

## Table of Contents

1. [Demo Types Taxonomy](about:blank#1-demo-types-taxonomy)
2. [Platform Selection Matrix](about:blank#2-platform-selection-matrix)
3. [Audience Profiles & Matching](about:blank#3-audience-profiles--matching)
4. [Sequencing Patterns](about:blank#4-sequencing-patterns)
5. [Demo Packs by Workshop Type](about:blank#5-demo-packs-by-workshop-type)
6. [Engagement Triggers](about:blank#6-engagement-triggers)
7. [Common Questions & Responses](about:blank#7-common-questions--responses)
8. [Delivery Best Practices](about:blank#8-delivery-best-practices)
9. [Appendix: Evidence Base](about:blank#9-appendix-evidence-base)

---

## 1. Demo Types Taxonomy

### 1.1 Core Demo Types (Use in Every Workshop)

These demos appear in 80-100% of successful workshops. Always include at least one.

| Demo Type | What It Shows | When to Use | Typical Duration |
| --- | --- | --- | --- |
| **Simple Prompts** | Basic ChatGPT/Claude interaction for writing, analysis, summarization | Always - establishes baseline understanding | 5-10 min |
| **AI Assistants (Custom GPTs)** | Pre-built assistants with specific instructions, knowledge, and personality | When showing “what you’ll take away” - the deliverable | 10-15 min |

### 1.2 Standard Demo Types (Select Based on Audience)

These demos appear in 30-60% of workshops. Select based on audience technical level and use case.

| Demo Type | What It Shows | Best For | Typical Duration |
| --- | --- | --- | --- |
| **Deep Research** | AI reasoning through complex analysis, multi-step research, synthesis | Executives, analysts, researchers | 10-15 min |
| **Agentic Workflows** | Multi-step automation with human checkpoints | Process owners, operations teams | 15-20 min |
| **Excel Demos** | Data analysis, formula generation, pivot creation | Finance, operations, analysts | 10-15 min |
| **N8N/Zapier Automation** | Visual workflow building, system integration | Technical teams, IT, process automation | 15-20 min |
| **Coding Tools (Cursor)** | AI-assisted development, code generation | Developers, IT teams | 15-20 min |
| **Interactive Artifacts** | Live website/tool creation during demo | Technical audiences, innovation teams | 20-30 min |

### 1.3 Specialized Demo Types (Context-Dependent)

Use these in specific contexts or for specific audiences.

| Demo Type | What It Shows | Best For | Typical Duration |
| --- | --- | --- | --- |
| **Image/Video Generation** | Midjourney, DALL-E, video AI | Marketing, creative teams | 10-15 min |
| **MCPs (Model Context Protocols)** | System integration without custom code | Technical architects, developers | 15-20 min |
| **Voice-First Workflows** | Whisper Flow, speech-to-action | Field workers, accessibility focus | 10-15 min |
| **Multi-Model Comparison** | Side-by-side ChatGPT vs Claude vs Gemini | Decision-makers choosing platforms | 10-15 min |

### 1.4 Business Context Demos (Often Overlooked but Critical)

| Demo Type | What It Shows | Best For | Typical Duration |
| --- | --- | --- | --- |
| **Cost/ROI Analysis** | Business case calculations, time savings | Executives, budget holders | 5-10 min |
| **Security & Governance** | Data handling, compliance, approved vendors | IT security, legal, compliance | 10-15 min |
| **Communication Assistants** | Email drafting, meeting notes, follow-up automation | Operations, sales, customer service | 10-15 min |

### 1.5 Demo Type Selection Decision Tree

```
START: What is the primary audience?
│
├─► EXECUTIVE / C-SUITE
│   └─► Simple Prompts → Deep Research → Cost/ROI → Multi-Model Comparison
│
├─► TECHNICAL / IT
│   └─► Simple Prompts → Custom GPTs → N8N Workflows → MCPs → Coding Tools
│
├─► OPERATIONS / LINE MANAGERS
│   └─► Simple Prompts → Custom GPTs → Communication Assistants → Excel Demos
│
├─► MARKETING / CREATIVE
│   └─► Simple Prompts → Custom GPTs → Image Generation → Interactive Artifacts
│
└─► MIXED / GENERAL
    └─► Simple Prompts → Custom GPTs → Deep Research → Agentic Workflows
```

---

## 2. Platform Selection Matrix

### 2.1 Primary Platforms

| Platform | Strengths | Best Use Cases | Audience Comfort |
| --- | --- | --- | --- |
| **ChatGPT** | Familiar, versatile, good baseline | First demos, external clients, general tasks | Highest |
| **Claude** | Document analysis, Excel, reasoning, longer context | Technical tasks, data work, complex analysis | Medium-High |
| **Gemini** | Google integration, large context | Google Workspace clients, comparison demos | Medium |

### 2.2 Platform Selection by Client Ecosystem

| Client Environment | Primary Platform | Secondary | Rationale |
| --- | --- | --- | --- |
| **Microsoft 365** | ChatGPT → Claude | Copilot (if licensed) | Familiarity + capability |
| **Google Workspace** | Gemini → ChatGPT | Claude | Native integration |
| **Technical/Dev** | Claude → Cursor | ChatGPT | Reasoning + code quality |
| **Enterprise (regulated)** | Claude (paid) → ChatGPT Enterprise | - | Data privacy emphasis |

### 2.3 Platform Capability Comparison (For Multi-Model Demos)

| Capability | ChatGPT | Claude | Gemini |
| --- | --- | --- | --- |
| General writing | ★★★★★ | ★★★★☆ | ★★★★☆ |
| Data analysis | ★★★★☆ | ★★★★★ | ★★★★☆ |
| Code generation | ★★★★☆ | ★★★★★ | ★★★★☆ |
| Document processing | ★★★☆☆ | ★★★★★ | ★★★★★ |
| Reasoning/logic | ★★★★☆ | ★★★★★ | ★★★★☆ |
| Creative content | ★★★★★ | ★★★★☆ | ★★★★☆ |
| Integration options | ★★★★★ | ★★★☆☆ | ★★★★☆ |

### 2.4 Automation Platform Selection

| Platform | Best For | Learning Curve | Cost |
| --- | --- | --- | --- |
| **N8N** | Enterprise workflows, self-hosted | Medium-High | Free/Low |
| **Zapier** | Quick automations, SaaS integration | Low | Medium |
| **Make** | Complex logic, visual building | Medium | Medium |

---

## 3. Audience Profiles & Matching

### 3.1 Audience Profile Definitions

### Profile A: Executive / Strategic

- **Role**: C-suite, VPs, Directors, Board members
- **Technical Level**: Low to medium
- **Primary Interest**: ROI, competitive advantage, strategic positioning
- **Time Available**: 60-90 minutes
- **Decision Authority**: High (budget, direction)

**Demo Preferences**:
- Start with strategic context (“why AI matters”)
- Show simple, impressive demos (not complex)
- Emphasize business outcomes over technical details
- Include cost/ROI analysis
- End with clear next steps and roadmap

### Profile B: Technical / IT

- **Role**: Developers, architects, IT managers, data engineers
- **Technical Level**: High
- **Primary Interest**: Integration, architecture, implementation details
- **Time Available**: 2-4 hours (hands-on)
- **Decision Authority**: Medium (technical approval)

**Demo Preferences**:
- Skip basic explanations (assume AI familiarity)
- Go deep on technical implementation
- Show code, APIs, integration patterns
- Include hands-on building time
- Discuss security and architecture

### Profile C: Operations / Practitioners

- **Role**: Process owners, team leads, analysts, specialists
- **Technical Level**: Low to medium
- **Primary Interest**: Time savings, quality improvement, daily workflow
- **Time Available**: 2-3 hours
- **Decision Authority**: Low-Medium (adoption, feedback)

**Demo Preferences**:
- Show their actual pain points being solved
- Quantify time savings explicitly
- Build something they can use immediately
- Focus on ease of use over power
- Provide takeaway prompts/tools

### Profile D: AI Champions / Enablers

- **Role**: Internal AI leads, change managers, trainers
- **Technical Level**: Medium to high
- **Primary Interest**: Scaling adoption, training others, governance
- **Time Available**: Half-day to multi-day programs
- **Decision Authority**: Influence (not budget)

**Demo Preferences**:
- Train-the-trainer approach
- Cover full spectrum of capabilities
- Include governance and policy frameworks
- Provide materials they can reuse
- Build their confidence to demo to others

### 3.2 Audience Identification Questions

Ask these questions during discovery or at workshop start:

1. “What’s your current familiarity with AI tools like ChatGPT?” (1-10 scale)
2. “What would success look like from today’s session?”
3. “Are you evaluating tools, or ready to implement?”
4. “Who else needs to be convinced after today?”
5. “What’s your biggest current pain point that AI might solve?”

### 3.3 Audience Mix Handling

| Mix Type | Approach |
| --- | --- |
| **Exec + Technical** | Split session: strategic (together) → technical (breakout) |
| **Beginners + Advanced** | Pair advanced with beginners for peer learning |
| **Skeptics + Enthusiasts** | Let enthusiasts demo their wins first |
| **Large Group (20+)** | Focus on inspiration; hands-on in smaller follow-ups |

---

## 4. Sequencing Patterns

### 4.1 Pattern A: Problem → Solution → Integration

**Best for**: External sales workshops, proof-of-concept sessions

**Duration**: 2-3 hours

```
┌─────────────────────────────────────────────────────────────┐
│  PHASE 1: Problem Definition (15-20 min)                    │
│  ├── Show their current painful process                     │
│  ├── Quantify the pain (time, errors, cost)                │
│  └── "What if we could solve this in seconds?"              │
├─────────────────────────────────────────────────────────────┤
│  PHASE 2: Simple Solution (20-30 min)                       │
│  ├── Live demo solving their exact problem                  │
│  ├── ChatGPT/Claude basic prompt approach                   │
│  └── "This took 30 seconds instead of 30 minutes"           │
├─────────────────────────────────────────────────────────────┤
│  PHASE 3: Enhanced Solution (30-40 min)                     │
│  ├── Custom GPT with their context                          │
│  ├── Workflow automation with human checkpoints             │
│  └── Integration with their existing systems                │
├─────────────────────────────────────────────────────────────┤
│  PHASE 4: Roadmap & Next Steps (15-20 min)                  │
│  ├── Implementation timeline                                │
│  ├── Training and adoption plan                             │
│  └── Pilot proposal with success metrics                    │
└─────────────────────────────────────────────────────────────┘
```

**Example**: Customs document extraction workshop
- Phase 1: Show 500 manual extractions/day pain
- Phase 2: ChatGPT extracts 10 fields from invoice
- Phase 3: Custom GPT + N8N workflow for full automation
- Phase 4: 6-month rollout roadmap

### 4.2 Pattern B: Education → Hands-On → Hackathon

**Best for**: Training programs, AI Champions, technical enablement

**Duration**: Half-day to full-day

```
┌─────────────────────────────────────────────────────────────┐
│  PHASE 1: Foundation (30-45 min)                            │
│  ├── What is generative AI? (conceptual)                    │
│  ├── Model differences and selection                        │
│  └── Security and governance basics                         │
├─────────────────────────────────────────────────────────────┤
│  PHASE 2: Guided Practice (60-90 min)                       │
│  ├── Instructor-led demos with follow-along                 │
│  ├── Prompt engineering exercises                           │
│  └── Building first Custom GPT together                     │
├─────────────────────────────────────────────────────────────┤
│  PHASE 3: Open Hackathon (90-120 min)                       │
│  ├── Teams identify their own use cases                     │
│  ├── Build working prototypes                               │
│  └── Facilitator support and troubleshooting                │
├─────────────────────────────────────────────────────────────┤
│  PHASE 4: Show & Tell (30-45 min)                           │
│  ├── Teams present what they built                          │
│  ├── Peer feedback and ideas                                │
│  └── Next steps for implementation                          │
└─────────────────────────────────────────────────────────────┘
```

**Example**: AI Champions Session
- Phase 1: AI landscape overview, model comparison
- Phase 2: Build email assistant together
- Phase 3: Teams build their department-specific tools
- Phase 4: Demo day with voting on best solutions

### 4.3 Pattern C: Vision → Strategy → Governance

**Best for**: Executive briefings, board presentations, strategic planning

**Duration**: 60-90 minutes

```
┌─────────────────────────────────────────────────────────────┐
│  PHASE 1: Strategic Context (15-20 min)                     │
│  ├── AI market landscape and trends                         │
│  ├── Competitor positioning                                 │
│  └── "Why this matters for your business"                   │
├─────────────────────────────────────────────────────────────┤
│  PHASE 2: Capability Demonstration (20-30 min)              │
│  ├── 2-3 impressive but accessible demos                    │
│  ├── Focus on business outcomes, not technology             │
│  └── "Your employees could do this tomorrow"                │
├─────────────────────────────────────────────────────────────┤
│  PHASE 3: Implementation Framework (15-20 min)              │
│  ├── Phased adoption roadmap                                │
│  ├── Investment requirements (2-5% of labor costs)          │
│  └── Expected ROI and timeline                              │
├─────────────────────────────────────────────────────────────┤
│  PHASE 4: Governance Model (10-15 min)                      │
│  ├── Policy framework                                       │
│  ├── Risk management                                        │
│  └── Compliance considerations                              │
└─────────────────────────────────────────────────────────────┘
```

**Example**: Board briefing on AI strategy
- Phase 1: “Companies with AI fluency are pulling ahead”
- Phase 2: Live demo of document analysis + meeting automation
- Phase 3: 12-month transformation roadmap
- Phase 4: Data security and compliance framework

### 4.4 Sequencing Decision Matrix

| Audience | Workshop Goal | Pattern |
| --- | --- | --- |
| External + Sales | Conversion to pilot/project | A: Problem → Solution |
| Internal + Training | Skill building | B: Education → Hackathon |
| Executive + Strategy | Buy-in and direction | C: Vision → Governance |
| Mixed + Awareness | General understanding | A (simplified) or C |
| Technical + Deep-dive | Implementation capability | B (extended Phase 3) |

---

## 5. Demo Packs by Workshop Type

### 5.1 Inspiration Workshop (2 hours)

**Objective**: Create awareness and excitement, generate follow-up interest

| Segment | Duration | Demos | Platforms |
| --- | --- | --- | --- |
| AI Landscape | 20 min | None (presentation) | - |
| Simple Prompts | 15 min | Writing, analysis, Q&A | ChatGPT |
| Custom GPT Demo | 20 min | Pre-built assistant | ChatGPT |
| Deep Research | 15 min | Complex analysis task | Claude |
| Workflow Preview | 15 min | N8N automation (show, don’t build) | N8N |
| Q&A + Next Steps | 15 min | - | - |

**Deliverables**: Prompt library PDF, recording, follow-up workshop invitation

### 5.2 Hands-On Prompting Workshop (3-4 hours)

**Objective**: Build practical skills, create takeaway tools

| Segment | Duration | Demos | Platforms |
| --- | --- | --- | --- |
| Foundation | 30 min | Model comparison | ChatGPT, Claude, Gemini |
| Prompt Engineering | 45 min | Exercises (writing, analysis) | ChatGPT |
| Custom GPT Building | 60 min | Build together | ChatGPT |
| Advanced Features | 45 min | Memory, web search, voice | ChatGPT, Claude |
| Use Case Application | 45 min | Apply to their work | Mixed |
| Wrap-up | 15 min | - | - |

**Deliverables**: Custom GPT they built, prompt templates, cheat sheet

### 5.3 Technical Implementation Workshop (Full day)

**Objective**: Enable technical team to build and integrate AI solutions

| Segment | Duration | Demos | Platforms |
| --- | --- | --- | --- |
| Architecture Overview | 45 min | Integration patterns | Whiteboard |
| API Integration | 60 min | Code examples | Claude API, OpenAI API |
| Workflow Automation | 90 min | Build N8N workflow | N8N |
| MCP Deep-dive | 60 min | System integration | Claude + MCPs |
| Hackathon | 120 min | Build real solution | Mixed |
| Architecture Review | 45 min | Review builds | - |

**Deliverables**: Working integration, code repository, architecture documentation

### 5.4 Executive Briefing (90 minutes)

**Objective**: Strategic buy-in, budget approval, direction setting

| Segment | Duration | Demos | Platforms |
| --- | --- | --- | --- |
| Market Context | 15 min | None (presentation) | - |
| Live Demo 1 | 10 min | Document analysis | Claude |
| Live Demo 2 | 10 min | Custom assistant | ChatGPT |
| ROI Analysis | 15 min | Cost/benefit calculations | Spreadsheet |
| Roadmap | 20 min | Implementation plan | Presentation |
| Discussion | 20 min | Q&A | - |

**Deliverables**: Executive summary, ROI model, proposal document

### 5.5 AI Champions Program (Multi-session)

**Objective**: Build internal AI expertise, enable scaling

| Session | Focus | Key Demos |
| --- | --- | --- |
| 1 | Foundation & Prompting | Simple prompts, model comparison |
| 2 | Custom Assistants | GPT building, Claude Projects |
| 3 | Data & Analysis | Excel, document processing |
| 4 | Visual AI | Midjourney, video generation |
| 5 | Workflow Automation | N8N, Zapier basics |
| 6 | Advanced Automation | MCPs, agentic workflows |
| 7 | Governance & Policy | Security frameworks |
| 8 | Scaling & Training | Train-the-trainer |

**Deliverables**: Certification, tool library, training materials

---

## 6. Engagement Triggers

### 6.1 High-Engagement Demo Patterns

Based on workshop analysis, these demo moments consistently generate the most engagement:

| Trigger | Example | Why It Works |
| --- | --- | --- |
| **Quantified Time Savings** | “This took 30 seconds instead of 30 minutes” | Immediate, concrete value |
| **Their Actual Data** | Using their real documents/emails | Relevance and believability |
| **Live Building** | Creating a tool during the session | “I could do this” realization |
| **Error Correction** | AI makes mistake, show how to fix | Builds trust through honesty |
| **Before/After** | Side-by-side comparison | Visual proof of improvement |
| **Participant Success** | Attendee’s prompt works perfectly | Social proof and confidence |

### 6.2 Engagement Metrics to Track

| Metric | How to Measure | Good Threshold |
| --- | --- | --- |
| Questions asked | Count during Q&A | 5+ per hour |
| Hands-on participation | % attempting exercises | 80%+ |
| Follow-up requests | Explicit asks for more | 30%+ of attendees |
| Tool adoption | Check-in 2 weeks later | 50%+ tried on their own |

### 6.3 Re-Engagement Techniques

When energy drops or attention wanes:

1. **Switch modality**: Presentation → Live demo → Hands-on
2. **Call on someone**: “Sarah, what would you use this for?”
3. **Acknowledge the elephant**: “I see some skepticism - let’s address it”
4. **Surprise demo**: Show unexpected capability (voice, image, etc.)
5. **Break**: 10 minutes can reset attention

---

## 7. Common Questions & Responses

### 7.1 Security & Privacy Questions

| Question | Response Framework |
| --- | --- |
| “Is our data safe?” | Explain paid vs free tiers, enterprise agreements, data handling policies |
| “Will AI train on our data?” | Clarify opt-out options, enterprise terms, API vs consumer products |
| “What about GDPR?” | Reference compliance frameworks, data residency options |
| “Can employees use free ChatGPT?” | Recommend policy: no confidential data on free tiers |

### 7.2 Accuracy & Reliability Questions

| Question | Response Framework |
| --- | --- |
| “What about hallucinations?” | Acknowledge limitation, show verification workflows, human-in-loop |
| “How do we know it’s correct?” | Demonstrate fact-checking, citation features, confidence signals |
| “What if it makes mistakes?” | Show error correction, emphasize AI as draft generator not final authority |

### 7.3 ROI & Business Case Questions

| Question | Response Framework |
| --- | --- |
| “What’s the cost?” | Break down: licenses ($20-30/user/month), training, integration |
| “What’s the ROI?” | Framework: 2-5% of labor cost investment → 5-15% efficiency gain |
| “How long until we see results?” | Timeline: Quick wins in weeks, transformation in 6-12 months |

### 7.4 Implementation Questions

| Question | Response Framework |
| --- | --- |
| “Where do we start?” | Identify highest-pain, lowest-risk use cases first |
| “Who should lead this?” | Recommend AI Champions model, 3-4 people per 100 employees |
| “How do we scale?” | Phased approach: Pilot → Department → Enterprise |

---

## 8. Delivery Best Practices

### 8.1 Before the Workshop

- [ ]  Confirm audience profile and technical level
- [ ]  Prepare demos with their industry/context examples
- [ ]  Test all tools and logins (nothing worse than login failures live)
- [ ]  Prepare backup demos in case primary fails
- [ ]  Create prompt library document to share
- [ ]  Set up recording (if permitted)

### 8.2 During the Workshop

- [ ]  Start with a quick poll/question to gauge the room
- [ ]  Acknowledge different experience levels
- [ ]  Use their terminology, not tech jargon
- [ ]  Pause after demos for questions
- [ ]  Capture questions you can’t answer for follow-up
- [ ]  Take screenshots of successful participant work

### 8.3 After the Workshop

- [ ]  Send follow-up within 24 hours
- [ ]  Include: recording, prompts, resources, next steps
- [ ]  Schedule follow-up check-in (2 weeks)
- [ ]  Log workshop for future reference
- [ ]  Update this methodology with new learnings

### 8.4 Demo Failure Recovery

| Failure Type | Recovery Action |
| --- | --- |
| Tool won’t load | Switch to backup tool or pre-recorded demo |
| AI gives bad response | “Perfect example of why we verify” - show correction |
| Audience disengaged | Pivot to hands-on exercise or Q&A |
| Running over time | Skip to key demo, offer follow-up session |
| Technical questions you can’t answer | “Great question - I’ll get back to you” (and do) |

### 8.5 Language & Framing

**Do say**:
- “AI as a capable intern” (sets right expectations)
- “Draft generator, not final authority”
- “Augments your expertise”
- “Let me show you” (then do it live)

**Don’t say**:
- “AI will replace…” (triggers fear)
- “It’s magic” (undermines credibility)
- “Always correct” (sets up for failure)
- “Simple” (can feel condescending)

---

## 9. Appendix: Evidence Base

### 9.1 Workshop Categories Analyzed

| Category | Count | Description |
| --- | --- | --- |
| Workshop Summary | 10 | Post-workshop summaries and debriefs |
| Inspiration & Education | 10 | Awareness and introduction sessions |
| Hands-On AI Prompting | 7 | Practical skill-building workshops |
| Specialized AI Workshop | 2 | Deep technical training (N8N, MCPs) |
| Workshop Follow-Up | 1 | Implementation follow-up sessions |

### 9.2 Clients Represented

- Nederlandse Loterij (lottery/gaming)
- Facilicom (facilities management)
- Geluk Groep (technical services)
- Gaston Schul (customs/logistics)
- EyeCare (healthcare marketing)
- Slokker (construction)
- Hemingway (corporate finance)
- Pricon/Interswitch (technology)
- Multiple internal sessions

### 9.3 Demo Type Frequency Data

```
Simple Prompts          ████████████████████ 100%
AI Assistants           ████████████████░░░░  87%
Deep Research           ████████████░░░░░░░░  60%
Agentic Workflows       ██████████░░░░░░░░░░  53%
Excel Demos             ███████░░░░░░░░░░░░░  37%
N8N/Zapier              ██████░░░░░░░░░░░░░░  33%
Coding Tools            █████░░░░░░░░░░░░░░░  27%
Interactive Artifacts   █████░░░░░░░░░░░░░░░  27%
Image/Video Generation  ███░░░░░░░░░░░░░░░░░  17%
```

### 9.4 Platform Frequency Data

```
ChatGPT                 ████████████████████ 100%
Claude                  ██████████████░░░░░░  70%
Gemini                  ████████░░░░░░░░░░░░  40%
N8N                     ██████░░░░░░░░░░░░░░  33%
Cursor                  █████░░░░░░░░░░░░░░░  27%
Midjourney              ███░░░░░░░░░░░░░░░░░  17%
Copilot                 ██░░░░░░░░░░░░░░░░░░  10%
```

### 9.5 Continuous Improvement

This document should be updated when:
- New demo types emerge (e.g., new AI capabilities)
- Platform capabilities significantly change
- Workshop patterns show new successful approaches
- Failure patterns reveal needed adjustments

**Feedback**: Log insights after each workshop to contribute to methodology evolution.

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────────┐
│                    DEMO SELECTION QUICK GUIDE               │
├─────────────────────────────────────────────────────────────┤
│  AUDIENCE          │  START WITH        │  THEN ADD         │
├────────────────────┼────────────────────┼───────────────────┤
│  Executive         │  Vision + Simple   │  ROI + Strategy   │
│  Technical         │  Simple + GPTs     │  N8N + MCPs       │
│  Operations        │  Problem + Simple  │  GPTs + Excel     │
│  Creative          │  Simple + Images   │  GPTs + Artifacts │
│  Mixed             │  Simple + GPTs     │  Research + Demo  │
├─────────────────────────────────────────────────────────────┤
│  PLATFORM SELECTION                                         │
├─────────────────────────────────────────────────────────────┤
│  Default start     │  ChatGPT (familiar)                    │
│  Data/Excel work   │  Claude (better)                       │
│  Google clients    │  Gemini (native)                       │
│  Automation        │  N8N (enterprise) / Zapier (simple)    │
│  Code/Dev          │  Cursor + Claude                       │
├─────────────────────────────────────────────────────────────┤
│  SEQUENCING PATTERNS                                        │
├─────────────────────────────────────────────────────────────┤
│  Sales workshop    │  Problem → Solution → Integration      │
│  Training          │  Education → Hands-On → Hackathon      │
│  Exec briefing     │  Vision → Strategy → Governance        │
├─────────────────────────────────────────────────────────────┤
│  ENGAGEMENT TRIGGERS                                        │
├─────────────────────────────────────────────────────────────┤
│  ✓ Quantified time savings ("30 sec vs 30 min")            │
│  ✓ Their actual data/documents                              │
│  ✓ Live building (not just showing)                         │
│  ✓ Participant success moments                              │
│  ✓ Before/after comparisons                                 │
└─────────────────────────────────────────────────────────────┘
```

---

*Document maintained by the workshop methodology team.*

---

# Part 2: Deep Research Findings

> Evidence-based insights from detailed transcript analysis of 14 Inspiration & Education workshops (1M+ characters analyzed)
> 

---

## 10. Proven Prompt Patterns

### 10.1 The Prompt Library: Greatest Hits

Based on extraction of 118 prompts across workshops, these consistently generate strong reactions:

### Signature Teaching Prompts

| Prompt Name | Example | Why It Works |
| --- | --- | --- |
| **“The Honest Beginner”** | “Dear AI, I am new to this job and bluffed a bit on my resume…” | Lowers intimidation, shows conversational style works |
| **“Directional Guidance”** | “Look, first look at the data, THEN make the graph…” | Demonstrates how to prevent AI errors with sequencing |
| **“Merge Results”** | “Look, merge the best of both worlds from these two outputs” | Shows professional multi-AI workflow |

### “Wow Moment” Demos (High Impact)

| Demo | Duration | What Happens | Audience Reaction |
| --- | --- | --- | --- |
| **Three AI Research Agency** | 5-7 min | Run same brief through ChatGPT/Claude/Gemini, synthesize best parts | “We can do this?!” |
| **Excel Scenario Builder** | 3-5 min | Upload data → AI creates 4-sheet workbook with scenarios | Visible note-taking |
| **WhisperFlow Voice** | 5 min | Speak workflow description → AI builds it → Test live | Questions about setup |
| **Dashboard from Scratch** | 2-3 min | Upload messy files → Interactive dashboard appears | Requests to repeat |

### 10.2 Prompt Structure That Works

```
EFFECTIVE PROMPT PATTERN (observed in high-engagement moments):

1. CONTEXT: "I am [role] working on [task]..."
2. DIRECTION: "First do X, then do Y..."
3. CONSTRAINTS: "Make sure to [specific requirement]..."
4. OUTPUT FORMAT: "Present this as [format]..."

EXAMPLE:
"I'm a financial analyst preparing a board presentation.
First analyze these quarterly numbers for trends,
then identify the top 3 risks.
Make sure to cite specific figures.
Present as executive bullet points, max 5 per section."
```

### 10.3 Prompt Delivery Technique

**Don’t**: Type silently while audience watches
**Do**: Narrate as you type

> “I’m going to tell it WHO I am… then WHAT I need… and HOW I want it formatted. Watch how specific I’m being about the output…”
> 

---

## 11. Live vs Pre-Built Demo Strategy

### 11.1 The 78/22 Rule

**Research finding**: 78.9% of demos are pre-built, 21.1% are built live

| Approach | Percentage | When to Use |
| --- | --- | --- |
| **Pre-built** | ~80% | Complex systems, >5 min to build, mission-critical moments |
| **Live building** | ~20% | Teaching creation process, simple demos, audience requests |

### 11.2 Decision Matrix

```
              ┌─────────────────────────────────────┐
              │     SHOULD I BUILD THIS LIVE?       │
              └─────────────────────────────────────┘
                               │
              ┌────────────────┴────────────────┐
              ▼                                 ▼
      Takes >5 minutes?                  Teaching the BUILD
              │                           process matters?
     ┌───────┴───────┐                        │
     ▼               ▼                   ┌────┴────┐
    YES             NO                   ▼         ▼
     │               │                  YES        NO
     ▼               │                   │         │
PRE-BUILD            │                   ▼         ▼
                     │              BUILD LIVE  PRE-BUILD
                     │               (narrate)
                     ▼
            High failure risk?
                     │
              ┌──────┴──────┐
              ▼             ▼
             YES           NO
              │             │
              ▼             ▼
         PRE-BUILD     BUILD LIVE
                       (with backup)
```

### 11.3 The “Prepared Live” Hybrid (Best Practice)

**Show the creation process live, but paste prepared content:**

1. Open tool live, narrate what you’re doing
2. “I’m going to paste in some instructions I’ve refined…”
3. Paste pre-written, tested content
4. Continue building/testing live

**Benefits**: Educational value + Reliability + Time efficiency

### 11.4 What to Pre-Build vs Build Live

| Always Pre-Build | Can Build Live |
| --- | --- |
| Multi-step workflows | Simple Custom GPT (<5 min) |
| Named production tools (Maya, Emil) | Single prompts |
| Prompt libraries | Basic automations |
| Complex Custom GPTs | Real-time audience requests (if simple) |
| Integration demos | Iteration teaching |

### 11.5 Credibility Builders

Show usage stats for pre-built tools:

> “Email Maestro, just to prove it, 4,939 times used.” — Actual workshop quote
> 

This proves the tool is real, tested, and trusted.

---

## 12. Demo Failure & Recovery Playbook

### 12.1 The Core Insight

**Failures are intentional teaching tools, not accidents.**

The same “AI forgot to use calculator” demo appears in multiple workshops with nearly identical recovery scripts—this is rehearsed pedagogy.

### 12.2 The “This Is Interesting” Frame

When demos fail, expert facilitators use calm observation language:

```
FAILURE RECOVERY SCRIPT:

"So, okay, this is interesting. I now see that [describe what happened].
That's actually a great example of [teaching point].
This is why we [best practice]."
```

**Example from transcript**:
> “This is interesting. I now see that the AI forgot to use its calculator. That’s a bit dumb, right? This is why you need to know your tools better than the AI does.”

**Why it works**:
- Positions facilitator as expert observer, not surprised victim
- Turns failure into teaching moment
- Builds credibility (“I catch these things”)

### 12.3 Three Intentional Failure Demos

| Failure Demo | What Happens | Teaching Point |
| --- | --- | --- |
| **The Forgetful Calculator** | AI does math wrong without tools | “You need to manage AIs like you manage humans” |
| **The Three Strikes** | Wrong → wrong → wrong output | “Always verify, never trust first output” |
| **Real-World Troubleshoot** | Page won’t load, tool crashes | “AI work involves collaboration and patience” |

### 12.4 Recovery Techniques by Failure Type

| Failure Type | Recovery Technique | Script Template |
| --- | --- | --- |
| **Wrong output** | “Teaching moment” frame | “This is actually perfect because it shows…” |
| **Hallucination** | Verification demo | “And THIS is why we always check…” |
| **Technical crash** | Backup demo + explanation | “While this loads, let me show you…” |
| **Slow response** | Fill with context | “This is taking time because it’s doing X…” |

### 12.5 Failure Prevention Checklist

- [ ]  Test all demos within 1 hour of workshop
- [ ]  Have backup demo ready for each planned demo
- [ ]  Prepare “teaching moment” script for likely failures
- [ ]  Know which demos have highest failure risk
- [ ]  Have offline examples ready (screenshots, recordings)

---

## 13. Tool Switching Mastery

### 13.1 Tool Switch Reality (Corrected)

**Initial finding** (from metadata): 0-2 switches
**Actual finding** (from transcript analysis): **4-10 switches, average 7.8**

| Workshop | Tool Switches | Unique Tools |
| --- | --- | --- |
| Ecom | 10 | 11 |
| Hemingway | 9 | 10 |
| Slokker | 6 | 7 |
| Pricon & Interswitch | 10 | 11 |
| Geluk Groep | 4 | 5 |
| **Average** | **7.8** | **8.8** |

**Key insight**: High tool count is NOT a problem—it’s the value proposition. Clients ask “what’s the difference between ChatGPT and Claude?” Comparative demos require multiple tools.

### 13.2 The Three-Phase Tool Structure

Every Inspiration workshop follows this pattern:

```
PHASE 1: LLM Comparison (4 tools, ~40% of time)
├── ChatGPT (baseline, familiar)
├── Claude (reasoning, documents)
├── Gemini (Google integration)
└── Copilot (Microsoft integration)

PHASE 2: Specialized Tools (2-4 tools, ~30% of time)
├── Cursor (coding)
├── Midjourney/DALL-E (images)
├── Suno (audio)
└── Canva/Gamma (presentations)

PHASE 3: Automation (2-3 tools, ~30% of time)
├── Zapier (simple)
├── N8N (complex)
└── Make (visual)
```

### 13.3 When to Switch vs When to Compare Verbally

| Scenario | Action | Rationale |
| --- | --- | --- |
| **Showing capability differences** | SWITCH | Clients need to see, not hear |
| **Excel/code work** | SWITCH to Claude | Demonstrably better results |
| **Document-heavy (20+ files)** | SWITCH to Copilot | Integration advantage |
| **Similar capabilities** | VERBAL comparison | “Gemini does this too” saves time |
| **Awareness only** | VERBAL mention | No need to demo everything |

### 13.4 Smooth Transition Phrases

**Switching TO Claude**:
> “For Excel work, I’m going to switch to Claude because it’s specifically very good at data analysis…”

**Switching TO Copilot**:
> “Normally I wouldn’t use Copilot, but it’s perfect for this use case because we have 49 documents to work with…”

**Verbal comparison (NO switch)**:
> “Claude has this too—they call it Extended Thinking. Gemini also has it. They all have similar capabilities, just different names.”

### 13.4 Typical Workshop Tool Flow

```
START
  │
  ▼
ChatGPT (60 min) ─── Baseline, familiar interface
  │
  ▼
[OPTIONAL] Claude (20 min) ─── Excel/code demo only
  │
  ▼
ChatGPT (30 min) ─── Wrap-up, Q&A
  │
  ▼
END

Total switches: 0-2
```

### 13.5 Managing Multiple Tool Switches

With 7-10 switches per workshop, structure and signposting matter:

**DO**:
- Announce phase transitions: “We’ve covered LLMs, now let’s look at automation”
- Group related tools: Show all LLMs together, then all automation tools
- Vary demo depth: 10 min on core tools, 2 min on awareness tools
- Provide decision matrix handout: “When to use which tool”

**DON’T**:
- Jump randomly between unrelated tools
- Give equal time to all tools (prioritize the 3-4 most relevant)
- Assume audience tracks which tool you’re in (verbally confirm)

**Success metric**: Not “fewer switches” but “Demo Depth Ratio” = 70% time on 3-4 core tools, 30% on breadth awareness

---

## 14. Real-Time Complexity Calibration

### 14.1 The 20:1 Simplification Ratio

**Research finding**: Facilitators simplify 20 times for every 1 complexity increase

| Action | Frequency per 4-hour workshop |
| --- | --- |
| Understanding checks | 45-84 times |
| Simplifications (“basically…”) | 85-139 times |
| Complexity increases | 4-6 times |

### 14.2 Calibration Signals to Read

**GREEN LIGHT (audience ready for more)**:
- Sophisticated questions using correct terminology
- Requests for “more advanced” content
- Note-taking increases
- Leaning forward, nodding

**YELLOW LIGHT (stay at current level)**:
- Basic questions
- Silence after “any questions?”
- Checking phones
- Confused expressions

**RED LIGHT (simplify immediately)**:
- “What do you mean?”
- “Can you go back?”
- Side conversations
- Visible frustration

### 14.3 The Permission Protocol (Before Going Advanced)

**Never increase complexity without explicit permission:**

```
1. READ the room (look for green light signals)
2. VALIDATE: "I feel you guys can get this"
3. ASK: "Should we go to the more advanced stuff?"
4. WAIT for clear YES signal
5. PROCEED only with confirmation
```

**From actual transcript**:
> Facilitator: “Should we go more to the more advanced stuff?”
> Facilitator: “I feel you guys can get this.”
> [Audience asks sophisticated question about Bing/SEO]
> Facilitator: “Let’s go.”

This happened ONCE in a 3-hour workshop.

### 14.4 Magic Phrases for Calibration

**Simplifying (use constantly)**:
- **“Basically…”** (used 201 times across 5 workshops = ~40x per workshop)
- “At its core…”
- “In simple terms…”
- “The key thing is…”
- “Let me show you…” (shift to concrete demo)

> What is “Basically” usage?
Facilitators literally say the word “basically” before explaining any technical concept. It’s a verbal signal that simplification is coming, which lowers audience cognitive load and anxiety.
> 
> 
> Example: Instead of “The model uses transformer architecture” → “Basically, the AI reads your whole message and figures out what matters most”
> 

**Checking understanding**:
- “Does that make sense?”
- “Any questions so far?”
- “Is everyone following?”
- “What questions do you have?” (assumes questions exist)

**Going advanced (rare, with permission)**:
- “Should we go more advanced?”
- “For those who want to go deeper…”
- “A bit more complex, but worth understanding…”

### 14.5 The “Basically” Technique

**Before every technical concept, add “basically”:**

❌ “The model uses transformer architecture with attention mechanisms”
✅ “Basically, the AI looks at your whole message and figures out which parts are most important”

❌ “We’re implementing a RAG pipeline”
✅ “Basically, we’re teaching the AI to look stuff up in your documents first”

### 14.6 When Confusion Happens

**Don’t**: Explain more with words
**Do**: Demonstrate concretely

```
Audience: "What do you mean?"
Facilitator: "Let me show you..." → [immediate demo]
```

**Concrete examples > More explanation**

### 14.7 Calibration Self-Assessment

After each workshop, check your ratios:

| Metric | Target | If Below | If Above |
| --- | --- | --- | --- |
| Understanding checks | 45+ | Check more often | Fine |
| “Basically” uses | 50+ | Simplify more | Fine |
| Complexity increases | 4-6 | You’re being too cautious | Slow down |

---

## 15. Quick Reference Cards

### 15.1 Pre-Workshop Checklist

```
□ Test all demos (within 1 hour of workshop)
□ Prepare backup for each demo
□ Load prompt library
□ Check tool logins (ChatGPT, Claude, etc.)
□ Prepare "teaching moment" failure scripts
□ Review audience profile
□ Set complexity starting point
□ Prepare 2-3 "wow moment" demos
□ Have offline backups (screenshots)
```

### 15.2 During-Workshop Mental Checklist (Every 5 Minutes)

```
□ Check understanding ("Does that make sense?")
□ Read the room (green/yellow/red?)
□ Use "basically" before technical terms
□ Demo, don't explain when confusion appears
□ Stay on current tool unless Excel/documents need
```

### 15.3 Demo Selection Quick Guide

```
┌─────────────────────────────────────────────────────────────┐
│                   DEMO SELECTION MATRIX                      │
├─────────────────────────────────────────────────────────────┤
│  TIME AVAILABLE    │  DEMO APPROACH                         │
├────────────────────┼────────────────────────────────────────┤
│  < 5 minutes       │  Pre-built, narrate what it does       │
│  5-10 minutes      │  "Prepared live" hybrid                │
│  > 10 minutes      │  Can build live if teaching creation   │
├─────────────────────────────────────────────────────────────┤
│  FAILURE RISK      │  APPROACH                              │
├────────────────────┼────────────────────────────────────────┤
│  High              │  Pre-built + backup ready              │
│  Medium            │  Live with practiced recovery script   │
│  Low               │  Build live, embrace the process       │
├─────────────────────────────────────────────────────────────┤
│  AUDIENCE          │  COMPLEXITY LEVEL                      │
├────────────────────┼────────────────────────────────────────┤
│  Executive         │  Simple demos, business outcomes       │
│  Technical         │  Can go advanced (with permission)     │
│  Mixed             │  Start simple, bifurcate if needed     │
└─────────────────────────────────────────────────────────────┘
```

---

## Appendix: Research Methodology

### Data Sources

- **Workshops analyzed**: 30 initial + 14 deep-dive
- **Total transcript characters**: 1.8M+
- **Date range**: October 2025 - January 2026
- **Categories**: Inspiration & Education, Hands-On Prompting, Specialized

### Analysis Methods

- Pattern matching for key phrases
- Frequency analysis of calibration language
- Context extraction (500-char windows)
- Cross-workshop validation of patterns

### Key Workshops for Deep Analysis

| Workshop | Duration | Characters | Key Findings |
| --- | --- | --- | --- |
| AI Masterclass @ Slokker | 4 hours | 234K | Failure recovery, calibration |
| Van Zanten | 3+ hours | 212K | Tool comparisons, prompts |
| Pricon & Interswitch | 3+ hours | 233K | Dutch delivery, intentional failures |
| Imker Capital Partners | 3 hours | 199K | Complexity calibration |
| Eden Akers | 2+ hours | 134K | Live vs pre-built |

---

*End of Deep Research Findings*