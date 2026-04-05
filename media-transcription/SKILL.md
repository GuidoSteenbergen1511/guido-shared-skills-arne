---
name: operations-media-transcription
description: "Converts audio and video files into text, subtitles, or captions using OpenAI Whisper CLI. Supports multiple models for accuracy/speed tradeoff, language detection, and output formats (txt/srt/vtt/json). Triggers: user asks to transcribe audio, transcribe video, extract speech from media, generate subtitles, create captions, or build searchable transcripts."
---

# Media Transcription

## Why This Exists

Meeting recordings, interview videos, and webinars contain valuable information locked in audio/video format. Transcription extracts this as searchable text for documentation, accessibility, and downstream processing (summarization, citation, captioning). Whisper CLI provides fast, accurate offline transcription without API rate limits or per-minute costs.

# Media Transcription

Transcribe video and audio files using OpenAI Whisper CLI.

## Prerequisites

Whisper must be installed:
```bash
pip install openai-whisper
```

Verify installation:
```bash
whisper --help
```

## Step-by-Step Workflow

### Step 1: Navigate to the file location

```bash
cd "{baseDir}/Videos"
```

### Step 2: Run Whisper transcription

**Standard transcription (recommended defaults):**
```bash
whisper "filename.mp4" --model medium --language en --output_format txt
```

**Example with full path:**
```bash
whisper "{baseDir}/Videos/my_video.mp4" --model medium --language en --output_format txt
```

### Step 3: Find the output

Whisper creates the transcript in the **current working directory** with the same filename:
- Input: `my_video.mp4`
- Output: `my_video.txt`

To verify:
```bash
ls -la *.txt
```

### Step 4: Read the transcript

```bash
cat "my_video.txt"
```

Or use the Read tool to view in Claude.

## Complete Command Reference

### Basic Commands

| Task | Command |
|------|---------|
| Transcribe to text | `whisper "file.mp4" --model medium --language en --output_format txt` |
| Generate subtitles | `whisper "file.mp4" --model medium --language en --output_format srt` |
| Web captions (VTT) | `whisper "file.mp4" --model medium --language en --output_format vtt` |
| All formats at once | `whisper "file.mp4" --model medium --language en --output_format all` |

### Model Selection

| Model | Speed | Accuracy | VRAM | When to Use |
|-------|-------|----------|------|-------------|
| `tiny` | ~1 min/10min | Lower | ~1GB | Quick test, draft (accuracy sacrifice acceptable) |
| `base` | ~2 min/10min | Moderate | ~1GB | Clear speech, low background noise |
| `small` | ~4 min/10min | Good | ~2GB | General use, balanced cost/accuracy |
| `medium` | ~8 min/10min | High | ~5GB | **Default** - interviews, meetings, professional content |
| `large` | ~15 min/10min | Highest | ~10GB | Accents, poor audio, critical accuracy required |

### Language Codes

| Language | Code |
|----------|------|
| English | `en` |
| Dutch | `nl` |
| German | `de` |
| French | `fr` |
| Spanish | `es` |
| Auto-detect | (omit --language flag) |

## Real-World Examples

### Example 1: Transcribe a CEO interview video

```bash
cd "{baseDir}/Videos/"
whisper "CEO_Interview.mp4" --model medium --language en --output_format txt
cat "CEO_Interview.txt"
```

### Example 2: Generate subtitles for a presentation

```bash
whisper "Presentation_2025.mp4" --model medium --language en --output_format srt
```
Output: `Presentation_2025.srt` (can be imported into video editors)

### Example 3: Transcribe Dutch meeting recording

```bash
whisper "Teammeeting_Jan.mp4" --model medium --language nl --output_format txt
```

### Example 4: Quick draft of long video

```bash
whisper "3hour_webinar.mp4" --model tiny --language en --output_format txt
```
(Use tiny for speed when accuracy is less critical)

### Example 5: High-accuracy transcription with accents

```bash
whisper "International_Panel.mp4" --model large --output_format txt
```
(Omit --language to auto-detect, use large for best accuracy)

## Output Location Control

**Save to specific directory:**
```bash
whisper "video.mp4" --model medium --language en --output_format txt --output_dir "/path/to/output/"
```

**Save next to source file:**
```bash
cd "/path/to/source/folder" && whisper "video.mp4" --model medium --language en --output_format txt
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| CUDA out of memory | Use smaller model: `--model small` or `--model base` |
| Very slow | Use `--model tiny` or `--model base` |
| Poor accuracy | Use `--model large` and/or specify correct `--language` |
| Output in wrong folder | Use `--output_dir` or `cd` to target folder first |
| Command not found | Run `pip install openai-whisper` |

## Background Execution

For long videos, run in background:
```bash
whisper "long_video.mp4" --model medium --language en --output_format txt &
```

Check if still running:
```bash
ps aux | grep whisper
```

## Performance & Magic Numbers

| Setting | Value | Rationale |
|---------|-------|-----------|
| Default Model | `medium` | Balances accuracy (~90-95% WER for clear speech) with reasonable speed (~8min/10min video) and VRAM (~5GB typical) without extreme overhead |
| Default Language | `en` | Assumes English context; auto-detect (`--language` omitted) adds ~5-10% processing overhead but handles mixed-language audio |
| VRAM Threshold - Switch to `small` | 4GB available | `medium` requires ~5GB peak; below 4GB, `small` model recommended to avoid OOM |
| VRAM Threshold - Switch to `base` | 2GB available | Extreme resource constraint; `base` still provides acceptable accuracy for clear speech |
| Processing Speed Ratio | 1min Whisper per 10min video | Approximate for `medium` model on modern GPU; actual varies by audio quality, sampling rate, and hardware |

## Testing & Validation

### 1. Verify Installation
```bash
whisper --help
# Should print usage info; if "command not found", run: pip install openai-whisper
```

### 2. Test with Sample Audio
```bash
whisper "{baseDir}/test_sample.mp4" --model tiny --language en --output_format txt
# Rationale: Use tiny model for quick validation (30 seconds max processing)
cat "{baseDir}/test_sample.txt"
# Verify output is readable text with minimal formatting errors
```

### 3. Validate Output Formats
Test each output format on same file:
```bash
whisper "{baseDir}/test_sample.mp4" --model small --output_format txt
whisper "{baseDir}/test_sample.mp4" --model small --output_format srt
whisper "{baseDir}/test_sample.mp4" --model small --output_format vtt
# Verify .txt is plain text, .srt has timestamps [00:00:00,000 --> 00:00:05,000], .vtt is WebVTT format
```

### 4. Language Detection
```bash
whisper "{baseDir}/multilingual_sample.mp4" --output_format txt
# Omit --language flag to test auto-detection
# Check output header for detected language in JSON format if needed
```

### 5. Quality Checks
After each transcription:
- [VALIDATION] Text is readable and grammatically coherent
- [VALIDATION] Timestamps (if SRT/VTT) are sequential and match audio duration
- [VALIDATION] Output file created in expected location (--output_dir or CWD)
- [VALIDATION] No truncation or encoding errors (check for garbled characters)
