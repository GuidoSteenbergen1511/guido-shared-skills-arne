# Slide Removal Rules

Empirically derived from analysis of 4+ real workshop decks. Load this file when reviewing removal decisions or adjusting detection thresholds.

---

## Rule Matrix

| # | Rule | Programme Type | Always Keep Override |
|---|------|----------------|----------------------|
| 1 | Blank/transition | Both | None |
| 2 | Video-only | Both | None |
| 3 | Exact duplicate (>90%) | Both | Keep the first occurrence |
| 4 | Near-duplicate (>80%) | Both | Keep the first occurrence |
| 5 | Welcome/greeting | Both | None |
| 6 | Quote-only philosophical | Both | None |
| 7 | Tool exploration exercise | Multi-session only | Methodology exercises are exempt |
| 8 | In-session recap reference | Multi-session only | None |
| 9 | Lesson-learned series | Multi-session only | Keep summary slide |

---

## Rule 1: Blank and Transition Slides

**Trigger:** Total text across all shapes on the slide is fewer than 10 characters.

**Why remove:** These are section dividers, countdown timers, or animation-holder slides that exist for in-person pacing. Participants reading the deck at home have no context for them.

**Examples of text that triggers removal:**
- "" (empty)
- "."
- "1"
- A slide with only an image and no text

**Never remove** the title/cover slide regardless of text length (index 0 is always kept).

---

## Rule 2: Video-Only Slides

**Trigger:** Slide contains a video or media element AND has fewer than 20 characters of text.

**Why remove:** Embedded video references do not survive PPTX-to-PDF conversion and are often broken in participant copies. If the trainer played a video during the session, participants can find it via the resources link.

**Detection:** Shape type codes 3 (movie), 13 (OLE), 14, 15, 16 are treated as media. Also checks for `media_type` attribute on the shape object.

---

## Rule 3 and 4: Duplicate Slides

**Trigger:** Text similarity ratio with any previously kept slide exceeds threshold.
- Exact duplicate: >90% similarity (SequenceMatcher ratio)
- Near-duplicate: >80% similarity (keep first occurrence)

**Why remove:** Multi-session programmes often reuse recap slides verbatim. Participants receive the same information twice, which feels sloppy.

**Important:** Similarity is calculated on extracted plain text only (not formatting or images). Two slides with different visual designs but the same text are treated as duplicates.

**Ordering:** The first slide in the deck wins. Later duplicates are removed.

---

## Rule 5: Welcome and Greeting Slides

**Trigger:** Slide text contains one of the greeting patterns AND total text is fewer than 100 characters.

**Patterns detected:**
- "nice to meet you"
- "welcome!"
- "welkom!"
- "welkom,"
- "goed om je te zien"

**Why remove:** These slides are designed for the moment the trainer first sees the audience. They have no re-read value and signal to participants that they are receiving an unedited internal deck.

**Note:** This rule does NOT affect the title/cover slide (Rule: first slide always kept).

---

## Rule 6: Quote-Only Philosophical Slides

**Trigger:** Slide contains quotation marks (straight or curly) AND is short (fewer than 300 characters) AND has 4 or fewer non-empty lines. Attribution patterns ("— Name") also trigger detection.

**Why remove:** Standalone inspirational quotes are openers used by the trainer to set tone. Without the trainer's framing, they read as filler. If a quote appears inside a slide with substantial educational content, the whole slide is kept.

**Examples that trigger removal:**
- "The best way to predict the future is to create it. — Alan Kay"
- A slide with only: "AI will not replace humans. Humans with AI will replace humans without AI."

**Examples that do NOT trigger (kept):**
- A slide with a quote followed by three bullet points explaining its business relevance
- A quote embedded in a case study or framework explanation

---

## Rule 7: Tool Exploration Exercises (Multi-Session Only)

**Trigger:** Slide text starts with "EXERCISE" AND contains tool exploration language.

**Tool exploration patterns:**
- "let's try", "laten we proberen"
- "let's test", "let's explore"
- "exploring"
- "go to chatgpt", "open chatgpt"
- "go to claude", "open claude", "open claude.ai"
- "ga naar chatgpt"

**Why remove (multi-session only):** In multi-session programmes, live tool exploration is guided by the trainer in real-time. The slide instructs participants to try a specific feature during the session. Without the trainer present, the instruction is orphaned. Single-workshop participants often receive exercises to attempt on their own after the session, so the same pattern is retained.

**Distinction from methodology exercises:**
- REMOVE: "EXERCISE: Go to ChatGPT > try the voice mode feature"
- KEEP: "EXERCISE: Map a workflow from your team using the 5-step use case canvas"
- KEEP: "EXERCISE: Complete the AI business case template for your department"

The detection checks for tool platform references ("go to chatgpt", "open claude") as the signal that the exercise is tool-guided rather than methodology-guided.

---

## Rule 8: In-Session Recap References (Multi-Session Only)

**Trigger:** Slide contains phrases referencing content from a previous session.

**Patterns detected:**
- "remember when you"
- "you already practiced"
- "remember this overview"
- "weet je nog dat jij"
- "je hebt al geoefend"

**Why remove:** These slides reference experiences ("remember when you tried X in session 2") that are meaningless to someone reading a static PDF. They were designed to activate episodic memory in the room, not to convey information.

---

## Rule 9: Lesson-Learned Series Slides (Multi-Session Only)

**Trigger:** Slide text contains a numbered series pattern like "(1/6)", "(2/6)", "(3/6)", etc.

**Why remove:** Programmes sometimes have a "most common AI mistakes" or "lessons learned" sequence where each slide in a deck covers one item in the series. In a live session, the trainer walks through all of them. In the send-out, only the summary overview slide (which lists all items without the "(1/6)" counter) is kept.

**What is kept:** The summary/overview slide that introduces the series without a counter (e.g., "The 6 most common AI adoption mistakes").

---

## Calibration Guidance

If removal rate is unexpected, run with `--dry-run` and inspect the per-slide output. Common calibration issues:

| Symptom | Likely cause | Adjustment |
|---------|-------------|-----------|
| Important content slides removed | Quote rule over-triggering | Increase quote threshold from 300 to 500 chars or increase max lines from 4 to 6 |
| Exercises retained that should be removed | Exercise language in different phrasing | Add the specific phrase to tool_exploration_patterns in the script |
| Duplicate removed incorrectly | Slides share agenda text but are different | Reduce near_duplicate threshold from 0.80 to 0.70 |
| Too many blanks retained | Short but non-blank divider slides | Reduce blank threshold from 10 to 5 chars |

To adjust thresholds, edit the constants near the top of `scripts/create_sendout.py`:
```python
NEAR_DUPLICATE_THRESHOLD = 0.80   # lower to be less aggressive on near-duplicates
EXACT_DUPLICATE_THRESHOLD = 0.90  # lower to be less aggressive on exact-duplicates
```

And in the `categorize_slide` function, the per-rule thresholds (text_len < 100 for welcome, text_len < 300 for quotes) can be adjusted inline.
