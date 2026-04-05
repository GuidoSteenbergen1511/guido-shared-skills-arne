# Shared Skills for Arne

Claude Code skills for business development, writing, research, consulting delivery, and presentations.

## Installation

```bash
# Clone the repo
git clone https://github.com/GuidoSteenbergen1511/guido-shared-skills-arne.git

# Initialize the last30days submodule
git submodule update --init --recursive

# Symlink or copy skills into your Claude Code skills folder
cp -r guido-shared-skills-arne/writer ~/.claude/skills/writer
cp -r guido-shared-skills-arne/editor ~/.claude/skills/editor
# ... repeat for each skill you want
```

Or symlink the whole folder for instant access to all skills:

```bash
for skill in guido-shared-skills-arne/*/; do
  ln -s "$(pwd)/$skill" ~/.claude/skills/
done
```

---

## Skills

### Writing & Communication

| Skill | Command | What it does |
|-------|---------|-------------|
| Writer | `/writer` | Conversion copywriter framework (PAS, AIDA, BAB, etc.) for proposals, websites, and executive copy |
| Editor | `/editor` | Seven Sweeps editing — rewrites for clarity, tone, evidence, and specificity |
| Email | `/email` | Professional email writer with 8 type classifications (quick reply, coordination, forwarding, formal, decline, etc.) |

**Email skill setup:** Before using `/email`, copy `email/references/config-template.md` to `email/references/config.md` and fill in your identity, team, and voice.

### Research & Analysis

| Skill | Command | What it does |
|-------|---------|-------------|
| Last 30 Days | `/last30days` | Researches any topic from the last 30 days across Reddit, X/Twitter, and the web — delivers a structured intelligence brief |
| GenAI Use Case Research | `/genai-use-case-research` | Parallel research workers that discover GenAI implementations for any industry. Requires Claude Code agent orchestration |

**Last 30 Days setup:** Requires `OPENAI_API_KEY` and optionally Reddit API keys and Bird CLI for X access. See `last30days/README.md` for full setup.

### Consulting Delivery

| Skill | Command | What it does |
|-------|---------|-------------|
| Process Workflow Mapper | `/process-workflow-mapper` | Creates company-wide workflow maps from interview transcripts |
| As-Is Workflow Documentation | `/as-is-workflow-documentation` | Captures current-state business processes phase by phase |
| To-Be Workflow Designer | `/to-be-workflow-designer` | Designs AI-augmented future-state workflows with time and cost estimates |
| Demo Factory | `/demo-factory` | Transforms client interviews and documents into workshop-ready AI demo packages |
| Prompt Wizard | `/prompt-wizard` | Creates professional prompts for custom GPTs and LLMs with dual-version output (comprehensive + size-constrained) |

### Meetings & Documentation

| Skill | Command | What it does |
|-------|---------|-------------|
| Meeting Notes | `/meeting-notes` | Standardized meeting documentation with decisions, action items, and follow-ups |
| Media Transcription | `/media-transcription` | Converts audio and video files to text using OpenAI Whisper CLI |

**Media Transcription setup:** `pip install openai-whisper`

### Presentations & Documents

| Skill | Command | What it does |
|-------|---------|-------------|
| Confidential PDF | `/confidential-pdf` | Creates participant-ready send-out versions of workshop decks (removes internal slides, adds confidentiality watermark) |
| Slide Image | `/slide-image` | Generates editorial photography for executive slides using the Nano Banana MCP |

**Confidential PDF setup:** Requires `python-pptx`, `reportlab`, `pypdf`, LibreOffice, and Ghostscript.

**Slide Image setup:** Requires the [Nano Banana MCP](https://github.com/nano-banana/nano-banana-mcp) server configured in your Claude Code settings.

---

## Dependencies Summary

| Skill | Requires |
|-------|---------|
| email | Outlook MCP (optional — falls back to text output) |
| last30days | Python, `OPENAI_API_KEY`, optional Bird CLI + Reddit API |
| genai-use-case-research | Claude Code agent orchestration (TeamCreate, SendMessage) |
| confidential-pdf | `python-pptx`, `reportlab`, `pypdf`, LibreOffice, Ghostscript |
| slide-image | Nano Banana MCP |
| media-transcription | `pip install openai-whisper` |
| demo-factory | `markitdown` MCP (for reading uploaded documents) |

---

## License

MIT — see LICENSE file.
