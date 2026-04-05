# Demo Types & AI Capability Categories

This is your **demo catalog and reference guide** for understanding AI capability types and selecting the right demos for your audience.

<aside>
📊

Based on our [](https://www.notion.so/21cb165a85e58066a3d3ce1756e07cd1?pvs=21) (700+ use cases) and validated through analysis of 30+ workshops.

</aside>

<aside>
🎓

For workshop delivery methodology, sequencing patterns, failure recovery, and facilitation techniques, see [AI Workshop Facilitation Guide](https://www.notion.so/AI-Workshop-Facilitation-Guide-2ebb165a85e58092bddbe067145a0bcd?pvs=21).

</aside>

---

## Demo Type Frequency (Based on 30+ Workshops)

```
Simple Prompts          ████████████████████ 100%  ← Always include
AI Assistants           ████████████████░░░░  87%  ← Almost always
Deep Research           ████████████░░░░░░░░  60%  
Agentic Workflows       ██████████░░░░░░░░░░  53%  
Excel Demos             ███████░░░░░░░░░░░░░  37%  
N8N/Zapier              ██████░░░░░░░░░░░░░░  33%  
Coding Tools            █████░░░░░░░░░░░░░░░  27%  
Interactive Artifacts   █████░░░░░░░░░░░░░░░  27%  
Image/Video Generation  ███░░░░░░░░░░░░░░░░░  17%  
```

---

## Demo Types by Priority Tier

### 🔴 Tier 1: Core Demos (Include in Every Workshop)

| Demo Type | What It Shows | Duration | Primary Platform |
| --- | --- | --- | --- |
| **Simple Prompts** | Basic AI interaction for writing, analysis, summarization | 5-10 min | ChatGPT |
| **AI Assistants** | Pre-built assistants with instructions, knowledge, personality | 10-15 min | ChatGPT / Claude |

### 🟡 Tier 2: Standard Demos (Select Based on Audience)

| Demo Type | What It Shows | Duration | Primary Platform | Best For |
| --- | --- | --- | --- | --- |
| **Deep Research** | Multi-step research, reasoning, synthesis | 10-15 min | Claude / Perplexity | Executives, analysts |
| **Agentic Workflows** | Multi-step automation with human checkpoints | 15-20 min | Claude / ChatGPT | Process owners, operations |
| **Excel & Data** | Data analysis, formula generation, insights | 10-15 min | Claude (best) / ChatGPT | Finance, analysts |
| **Automation Workflows** | Visual workflow building, system integration | 15-20 min | N8N / Zapier | Technical teams, IT |
| **Coding Tools** | AI-assisted development, code generation | 15-20 min | Cursor / Claude Code | Developers, IT |
| **Interactive Artifacts** | Live dashboard/tool creation | 20-30 min | Claude | Technical, innovation teams |

### 🟢 Tier 3: Specialized Demos (Context-Dependent)

| Demo Type | What It Shows | Duration | Primary Platform |
| --- | --- | --- | --- |
| **Image/Video Generation** | Midjourney, DALL-E, video AI | 10-15 min | Midjourney / DALL-E |
| **MCPs** | System integration without custom code | 15-20 min | Claude + MCPs |
| **Voice Workflows** | Speech-to-action, Whisper Flow | 10-15 min | WhisperFlow / ChatGPT |
| **Multi-Model Comparison** | Side-by-side ChatGPT vs Claude vs Gemini | 10-15 min | Multiple |
| **Enterprise Agents** | SharePoint/M365 integration | 15-20 min | Copilot Studio |
| **Cost/ROI Analysis** | Business case calculations | 5-10 min | Spreadsheet + AI |

**For platform selection, audience matching, and workshop sequencing, see the [AI Workshop Facilitation Guide](https://www.notion.so/AI-Workshop-Facilitation-Guide-2ebb165a85e58092bddbe067145a0bcd?pvs=21).**

---

## Detailed Demo Type Descriptions

### 1. Simple Prompts

**What it is:** Standalone prompts that can be copy-pasted into any AI interface (ChatGPT, Claude, Copilot) to perform a specific task.

**When to use:**

- First AI introduction for beginners
- Quick wins and immediate value demonstration
- When clients don't have enterprise AI tools yet
- Teaching prompt engineering fundamentals
- Showing the "before" in a before/after comparison
- Validating that a use case works before building an assistant

**Characteristics:**

- No setup required — anyone can start immediately
- Platform-agnostic — works across ChatGPT, Claude, Gemini, Copilot
- Easy to share and replicate via copy-paste
- Good starting point before building Custom GPTs
- Low risk — if it doesn't work, just iterate
- Great for showing prompt structure and engineering principles

**High-impact prompt patterns (proven in workshops):**

- **"The Honest Beginner"**: "Dear AI, I am new to this job and bluffed a bit on my resume…" — Lowers intimidation, shows conversational style works
- **"Directional Guidance"**: "Look, first look at the data, THEN make the graph…" — Demonstrates how to prevent AI errors with sequencing
- **"Merge Results"**: "Look, merge the best of both worlds from these two outputs" — Shows professional multi-AI workflow

**Prompt structure that works:**

```
1. CONTEXT: "I am [role] working on [task]..."
2. DIRECTION: "First do X, then do Y..."
3. CONSTRAINTS: "Make sure to [specific requirement]..."
4. OUTPUT FORMAT: "Present this as [format]..."
```

**Demo approach:** 

1. Show the prompt structure before typing
2. Narrate as you type (don't type silently)
3. Explain: "I'm telling it WHO I am… WHAT I need… HOW I want it formatted"
4. Run it live
5. Show iteration when output isn't perfect
6. Quantify time savings: "This took 30 seconds instead of 30 minutes"

**Platforms:** ChatGPT (default), Claude, Gemini, Copilot

---

### 2. AI Assistants (Custom GPTs / Claude Projects / Gemini Gems)

**What it is:** Persistent AI assistants configured with custom instructions, knowledge files, and specific behaviors that can be reused across sessions.

**When to use:**

- When the same type of task is performed repeatedly
- When context (company info, processes, guidelines) needs to persist
- For team-wide deployment of a standardized tool
- When beginners need guided AI interaction
- For embedding organizational knowledge in AI
- When you want to share AI capabilities with non-technical users

**Characteristics:**

- Persistent instructions and personality
- Knowledge files for context (documents, guidelines, examples)
- Reusable across multiple sessions and users
- Can be shared via links or deployed to teams
- Reduces prompting effort for end users
- Maintains consistency in outputs
- Good upgrade path from simple prompts

**Examples from our library:**

- Professional Communication Assistants (email writer, meeting prep)
- Strategy Meeting Notes + Action Items generator
- Due Diligence Document Analyst
- Sales Proposal Generator
- Customer Service Response Helper
- HR Policy Q&A Assistant

**Demo approach:**

1. Show the creation interface (don't just use a finished GPT)
2. Walk through instructions, knowledge, and behavior settings
3. Demonstrate how it responds differently than base AI
4. Show sharing and team deployment options
5. Have audience think about their own use cases
6. Build one together if time allows

#### Platform Comparison

**Custom GPTs (OpenAI/ChatGPT)**

| Pros | Cons |
| --- | --- |
| Largest ecosystem (GPT Store) | Limited context window |
| Web browsing + DALL-E + code | Knowledge retrieval inconsistent |
| Easy sharing via links | Enterprise licensing expensive |
| API access for integration | Less transparent reasoning |

**Claude Projects (Anthropic)**

| Pros | Cons |
| --- | --- |
| Largest context (200K tokens) | No native web browsing |
| Superior reasoning | No marketplace |
| Artifacts for interactive outputs | Requires Pro/Business subscription |
| Fewer hallucinations | Less flexible file handling |

**Gemini Gems (Google)**

| Pros | Cons |
| --- | --- |
| Google Workspace integration | Less mature |
| Native Google Search | Inconsistent quality |
| Competitive pricing | Limited customization |
| Multimodal (text, image, video) | Smaller community |

**Copilot Agents (Microsoft)**

| Pros | Cons |
| --- | --- |
| SharePoint + M365 integration | Expensive licensing |
| Enterprise compliance (SOC 2, GDPR) | Complex setup |
| Auto-syncing knowledge | Slower iteration |
| Built-in governance | Ecosystem dependent |

**When to use which:**

| Scenario | Best Choice | Why |
| --- | --- | --- |
| General-purpose | Custom GPT | Broadest capabilities |
| Complex documents | Claude Project | Largest context, best reasoning |
| Google Workspace org | Gemini Gem | Native integration |
| M365 enterprise | Copilot Agent | SharePoint, compliance |
| Interactive visuals | Claude Project | Artifacts feature |

---

### 3. Deep Research

**What it is:** Specialized prompts and tools designed for comprehensive market research, competitive analysis, or due diligence using AI's research and reasoning capabilities.

**When to use:**

- Market sizing and opportunity analysis
- Competitor intelligence gathering
- Due diligence preparation (PE, M&A)
- Strategic planning support
- Finding precedent transactions or comparable companies
- Patent and IP research
- Industry trend analysis

**Characteristics:**

- Multi-source synthesis from web, documents, and databases
- Structured output formats (tables, summaries, citations)
- Often combined with company-specific context
- Can feed into agentic workflows for larger projects
- Requires verification of sources and facts
- Best when given specific research questions, not vague topics

**Platforms:**

- **ChatGPT with browsing** — Good general research, familiar interface
- **Perplexity** — Best for cited research, includes Patents search
- **Claude with web access** — Superior reasoning and synthesis
- **Gemini Deep Research** — Comprehensive multi-step research mode

**Examples from our library:**

- Market Opportunity Analyst (regional market intelligence)
- Bedrijfsprofiel Generator (company profiles for M&A)
- Weekly Market Intelligence reports
- CCA Company Discovery & Description Generator

**"Wow moment" demo: Three AI Research Agency**

- Run the same research brief through ChatGPT, Claude, and Gemini
- Show how each finds different angles and sources
- Synthesize the best parts from each with "merge the best of both worlds"
- Duration: 5-7 minutes
- Audience reaction: "We can do this?!"

**Demo approach:**

1. Start with a real research question from their industry
2. Show the research process — don't just show the output
3. Highlight source quality and how to verify
4. Demonstrate synthesis across multiple sources
5. Compare output quality across platforms if time allows

---

### 4. Agentic Workflows (Parallel Agents)

**What it is:** Multiple specialized AI agents working together autonomously, often in parallel, to complete complex tasks that would take humans hours or days.

**When to use:**

- Complex document generation (IC memos, proposals, reports)
- Multi-step analysis requiring different expertise areas
- Tasks that would take hours manually
- Demonstrating cutting-edge AI orchestration
- When quality validation between steps is critical
- Standardizing complex deliverables across teams

**Characteristics:**

- Modular design — each agent has one specific job
- Parallel execution for speed
- Quality validation checkpoints between steps
- Human-in-the-loop at critical decision points
- Often 70-90% time savings (e.g., 8-10 hours → 1 hour)
- Requires upfront design of agent architecture

**Key concepts:**

- **Skills**: Reusable capabilities given to agents (different from Assistants — skills are building blocks, assistants are complete tools)
- **Orchestration**: Managing how multiple subagents work together
- **Human checkpoints**: Quality validation between steps
- **Modular prompts**: Each agent has a focused, testable prompt

**Examples from our library:**

- TICA Modular System (12 agents for target intelligence — reduces 8-10 hours to ~1 hour)
- Apheon Modular IC Memo System (12 agents for investment committee memos)
- Synergia IC-LC Investment Memo (7 specialized agents)
- Portfolio Reporting Harmonization
- Beaufort Corporate Advisory Report Suite

**Platforms:**

- Claude (best for complex reasoning steps)
- ChatGPT (good for parallel execution)
- Cursor/Claude Code (for orchestration with MCP tools)

**Demo approach:**

1. Explain the orchestration concept — "like a team of specialists"
2. Show the agent breakdown visually (diagram or list)
3. Demonstrate one or two agents running
4. Highlight time savings with specific numbers
5. Show quality control between steps
6. Emphasize this is the future of knowledge work

---

### 5. Excel & Data Capability Demos

**What it is:** Demonstrations of AI's ability to work with Excel files, analyze data, generate insights, create formulas, and produce formatted outputs.

**When to use:**

- Finance and analyst audiences
- Showing AI can handle "their" data (makes it real)
- Business case calculations
- Data cleaning and transformation
- Creating pivot tables, charts, and summaries
- Formula generation and debugging
- Scenario modeling

**Characteristics:**

- Works with real client data formats (Excel, CSV)
- Can generate charts, tables, and visualizations
- Often includes Python code generation for complex analysis
- Outputs can be downloaded and used immediately
- Shows AI as "analyst augmentation" not replacement
- Very high credibility with finance audiences

**Platforms:**

- **Claude** — Demonstrably better for data work, recommended
- **ChatGPT Advanced Data Analysis** — Good, familiar interface
- **Copilot in Excel** — For M365 environments

**Examples from our library:**

- Teknor Apex Viscosity Data Analyst
- Teknor Apex Manufacturing Plant Analyst
- xSuite Data Analysis & Dashboard Building
- Financial Intelligence Dashboard (Slokker)

**"Wow moment" demo: Excel Scenario Builder**

- Upload raw, messy data
- AI creates 4-sheet workbook with scenarios
- Duration: 3-5 minutes
- Audience reaction: Visible note-taking, requests to see again

**Demo approach:**

1. Use realistic sample data (or their actual data if available)
2. Show the analysis process, not just the output
3. Highlight insights that would take hours manually
4. Demonstrate formula generation and explanation
5. Show downloadable output they can use immediately
6. Quantify: "This analysis would normally take 2 hours"

---

### 6. Interactive Artifacts (Claude Artifacts)

**What it is:** AI-generated interactive outputs like dashboards, calculators, maps, and self-assessment tools that run directly in the chat interface.

**When to use:**

- Visual decision support tools
- Self-service assessments and calculators
- Data visualization needs
- Proof-of-concept for apps before development
- Rapid prototyping of internal tools
- When you want to show "the art of the possible"

**Characteristics:**

- React-based interactive components
- No deployment needed — runs directly in Claude
- Shareable via conversation links
- Great for rapid prototyping
- Can include charts, maps, forms, calculators
- Iterative — easy to modify based on feedback

**Platform:** Claude (Artifacts feature is unique to Claude)

**Examples from our library:**

- AI Readiness Self-Assessment (radar charts)
- Asia Customer Visit Map (Leaflet.js)
- S&OP Dashboard for Production Planning
- Facilicom Dashboard Check-Ins
- Financial Intelligence Dashboard

**"Wow moment" demo: Dashboard from Scratch**

- Upload messy files → Interactive dashboard appears
- Duration: 2-3 minutes
- Audience reaction: Requests to repeat, "how did you do that?"

**Demo approach:**

1. Build the artifact live (this is the wow)
2. Start with a simple request, then iterate
3. Show interactivity — click buttons, filter data
4. Demonstrate how easy it is to modify ("make it blue", "add a filter")
5. Explain this is a prototype, not production — but shows feasibility

---

### 7. Coding Tools & App Building

**What it is:** Using AI coding assistants to build functional applications, websites, dashboards, and internal tools.

**When to use:**

- Technical audiences who want to see "how it's built"
- Showing rapid prototyping capabilities
- Building internal tools during the workshop
- Demonstrating AI-assisted development workflow
- When clients have development teams
- "Vibe coding" — conversational app building

**Characteristics:**

- Can build functional apps in minutes
- Requires some technical understanding to guide
- Best when starting from a clear business problem
- Iterative development with AI as pair programmer
- Can generate both frontend and backend code
- Shows the future of software development

**Subtypes:**

- **Cursor prompts** — For professional developers, IDE integration
- **Claude Code** — Terminal-based, good for complex projects
- **GitHub Copilot** — Inline code suggestions
- **Lovable / v0** — No-code/low-code app builders
- **Replit** — Browser-based development with AI

**Examples from our library:**

- PCI Schadeproces Dashboard (damage tracking website)
- PCI ROI Dashboard Generator
- Wajer Visual Inspection AI & Report Generator
- Peer Analysis Dashboard

**"Wow moment" demo: WhisperFlow Voice**

- Speak a workflow description out loud
- AI builds it while you watch
- Test it live
- Duration: 5 minutes
- Audience reaction: Questions about setup, "can we do this?"

**Demo approach:**

1. Start with a business problem, not a technical spec
2. Build the solution live (or use "prepared live" hybrid)
3. Narrate what the AI is doing as it codes
4. Iterate based on feedback — "make the button bigger"
5. Deploy or run the result to show it works
6. Acknowledge limitations: "This is a prototype, not production-ready"

---

### 8. Automation Workflows (N8N/Zapier/Make)

**What it is:** Visual workflow building that connects AI to other systems, running on triggers or schedules.

**When to use:**

- Recurring tasks (daily/weekly reports)
- Email processing and routing
- Document generation at scale
- Integration between systems (CRM, email, databases)
- When clients want AI to "run in the background"
- Process automation with human checkpoints

**Characteristics:**

- Runs in background without human intervention
- Trigger-based (email arrives, form submitted) or scheduled
- Often combines multiple AI calls in sequence
- Integrates with existing tools (Slack, email, CRM, databases)
- Visual builder makes it accessible to non-developers
- Requires initial setup but then runs autonomously

**Platform comparison:**

| Platform | Best For | Learning Curve | Cost |
| --- | --- | --- | --- |
| **N8N** | Enterprise workflows, self-hosted, complex logic | Medium-High | Free/Low (self-hosted) |
| **Zapier** | Quick automations, SaaS integration, beginners | Low | Medium (€20-50/month) |
| **Make** | Complex logic, visual building, mid-level | Medium | Medium |
| **Power Automate** | M365 environments, enterprise compliance | Medium | Included in M365 |

**Examples from our library:**

- Meeting notes → Action items → Task creation workflow
- Email classification and routing
- Document processing pipelines
- Weekly intelligence report generation

**Demo approach:**

1. Show the workflow diagram first — visual understanding
2. Explain triggers: "When this happens, the workflow starts"
3. Walk through each step in the flow
4. Demonstrate an example run (or show a recent run log)
5. Highlight where AI fits in the workflow
6. Discuss: "Once set up, this runs every day without you"

---

### 9. Image & Video Generation

**What it is:** AI tools that create images, videos, and visual content from text descriptions.

**When to use:**

- Marketing and creative teams
- Content creation workflows
- Prototyping visual concepts
- Social media content
- Presentation graphics
- When showing the breadth of AI capabilities

**Characteristics:**

- Impressive for non-technical audiences
- Quality varies significantly by tool and prompt
- Requires prompt engineering for good results
- Copyright and usage rights considerations
- Fast iteration on visual concepts
- Best for ideation, not final production (usually)

**Platforms:**

- **Midjourney** — Highest quality images, Discord-based
- **DALL-E** — Good quality, integrated in ChatGPT
- **Stable Diffusion** — Open source, self-hostable
- **Runway / Sora** — Video generation
- **Suno** — Music and audio generation

**Demo approach:**

1. Start with a simple, clear prompt
2. Show iteration: "Now let's make it more corporate"
3. Demonstrate style consistency across images
4. Discuss limitations and appropriate use cases
5. Don't oversell — acknowledge when results aren't perfect

---

### 10. MCPs (Model Context Protocols)

**What it is:** System integration without custom code — connecting AI to databases, APIs, and enterprise systems through standardized protocols.

**When to use:**

- Technical architects and developers
- Enterprise integration discussions
- When clients want AI connected to their systems
- Demonstrating "AI that can take action"
- Advanced automation scenarios

**Characteristics:**

- Enables AI to read/write to external systems
- No custom API development required
- Standardized protocol (like USB for AI)
- Requires technical setup
- Cutting-edge capability

**Platform:** Claude with MCP servers

**Demo approach:**

1. Explain the concept: "AI that can actually do things, not just talk"
2. Show a simple integration (calendar, database)
3. Demonstrate read and write capabilities
4. Discuss security and permissions
5. Position as the future of enterprise AI

---

### 11. Background Tasks ('Tasks' Demo)

**What it is:** AI agents that work asynchronously on longer tasks, similar to giving work to a junior analyst who comes back with results.

**When to use:**

- Tasks that take more than a few minutes
- Research that requires multiple steps
- When users want to "hand off" work and come back later
- Demonstrating AI as a delegated worker
- Complex analysis that benefits from extended thinking

**Characteristics:**

- Runs in background while you do other things
- Can take minutes to hours depending on complexity
- Returns comprehensive results
- Good for complex research and analysis
- Changes the mental model from "chat" to "delegation"

**Platforms:**

- ChatGPT Tasks
- Claude with extended thinking
- Custom orchestration systems

**Demo approach:**

1. Submit a complex task
2. Explain: "This will run while we look at something else"
3. Come back to reveal the comprehensive output
4. Highlight depth that wouldn't be possible in real-time chat

---

### 12. Enterprise AI Agents (Copilot Agents)

**What it is:** AI agents built within Microsoft 365 Copilot that connect to enterprise data sources like SharePoint.

**When to use:**

- Organizations with M365 enterprise licenses
- Need for SharePoint/OneDrive integration
- Compliance and data governance requirements
- HR, legal, or policy assistants
- When data must stay within Microsoft ecosystem

**Characteristics:**

- Enterprise security and compliance (SOC 2, GDPR)
- Auto-syncs with organizational knowledge bases
- Source citations from internal documents
- Integrates with Teams, Outlook, Microsoft Graph
- Built-in governance and admin controls
- Requires M365 Copilot licensing

**Examples from our library:**

- Eneco HR Assistant
- Eneco Treasury Agent
- BARoZa Customer Service Copilot (Royal Van Zanten)
- xSuite Sales Reference Finder

**Demo approach:**

1. Show the Copilot Studio setup interface
2. Demonstrate knowledge retrieval from SharePoint
3. Highlight source citations
4. Discuss enterprise compliance features
5. Compare to standalone tools (trade-offs)

---

### 13. Notion AI

**What it is:** AI capabilities built directly into Notion for workspace-specific assistance.

**When to use:**

- Organizations already using Notion
- Document drafting and editing
- Workspace search and Q&A
- Meeting notes and summaries
- When AI should work within existing workflow

**Characteristics:**

- Native integration with Notion data
- No separate tool needed
- Context-aware suggestions
- Database querying and analysis
- Works within existing workspace structure

**Demo approach:**

1. Show within a real Notion workspace
2. Demonstrate context awareness ("summarize this page")
3. Show database queries and analysis
4. Highlight that it works where they already work

---

---

## Delivery Tips

### Live vs Pre-Built (The 78/22 Rule)

**~80% pre-built** for complex systems, >5 min to build, mission-critical

**~20% live building** for teaching creation, simple demos, audience requests

**Best practice: "Prepared Live" Hybrid**

1. Open tool live, narrate what you're doing
2. "I'm going to paste in some instructions I've refined…"
3. Paste pre-written, tested content
4. Continue building/testing live

### When Demos Fail

Use the **"This is interesting"** frame:

> "So, okay, this is interesting. I now see that [describe what happened]. That's actually a great example of [teaching point]. This is why we [best practice]."
> 

Failures become teaching moments, not accidents.

### Tool Switching

Expect **7-10 tool switches** per workshop. This is the value proposition, not a problem.

**DO:** Announce phase transitions, group related tools, vary demo depth

**DON'T:** Jump randomly, give equal time to all tools

---

## Related Resources

- [](https://www.notion.so/21cb165a85e58066a3d3ce1756e07cd1?pvs=21) — Full library of 700+ demos
- [AI Workshop Facilitation Guide](https://www.notion.so/AI-Workshop-Facilitation-Guide-2ebb165a85e58092bddbe067145a0bcd?pvs=21) — Deep-dive on delivery techniques, failure recovery, complexity calibration
- [AI Champions Programme ](https://www.notion.so/AI-Champions-Programme-238b165a85e580219bdac84e1787526c?pvs=21) — Multi-session program structure