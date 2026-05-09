# The Pitch Meeting Format

Every candidate gets a full simulated meeting. The meeting is the pitch's most valuable artifact — more than the deck, more than the scorecard. It exposes how an idea actually lands when investors push back, and it gives the user something they can review on their own time, in any of three modes:

- **Read** the transcript markdown
- **Watch** the visual-novel HTML (Shark-Tank-/Dragons'-Den-style episode replay)
- **Listen** via Web Speech API (zero setup, click play in the visual novel) or render to ElevenLabs / OpenAI TTS for higher-quality audio

The transcript is **voice-render-ready by design** — speaker tags are stable, line breaks are clean, stage directions are italicized on their own lines so TTS engines ignore them gracefully.

## Structure

A meeting has six parts. Run them in order; save each as a separate artifact in `pitches/<slug>/pitch-meeting/` so the user can dip into any of them.

### 1. Pre-pitch perception survey

**Saved as**: `pitch-meeting/pre-pitch-survey.md`

Every panelist (5 fixed investors + Domain Expert + Customer + Founder = 8 people) rates the idea on three axes **without seeing the pitch deck**. They get only:
- The pitch's one-line thesis
- The commitment mode under evaluation
- The chosen domain (so the Domain Expert and Customer have context)

Each rates:
- **Idea quality** (1–10) — "Is this a good idea on the merits?"
- **Viability** (1–10) — "Could this actually be built and run?"
- **Profitability** (1–10) — "Could this make money in the chosen mode?"
- **One-line gut reaction**

Why pre-pitch matters: it captures the **cold opinion**. Without this, you can't measure how much the actual pitch moved the room.

### 2. Founder narrative + deck walkthrough

**Captured in**: `pitch-meeting/transcript.md`

The founder (rendered as a solo founder for any solo-mode pitch; a small team for team modes) opens with a **customer moment** (per `references/storytelling-lessons.md`), not market size. They walk through the deck briefly — emphasize the wedge, the buyer, the one non-obvious insight, and the demo or prototype.

Aim for ~5–8 dialogue turns from the founder before Q&A starts. Keep it tight; investors get fidgety with monologues over 3 minutes of read time.

### 3. Q&A

**Captured in**: `pitch-meeting/transcript.md` (continues)

The longest section. Round-robin starting with whichever investor has the strongest natural appetite for the chosen commitment mode. Each investor asks 2–4 questions; the founder answers; allow 1–3 inter-investor crosstalk exchanges per meeting (e.g., the Skeptic and the Growth VC disagreeing about the moat). Domain Expert and Customer interject with reality-checks.

Aim for **25–45 total dialogue turns** including the narrative section. Less than 20 turns is shallow; more than 60 turns becomes hard to follow.

Stay in voice. The Bootstrapper sounds different from the Growth VC. Don't let everyone converge on a single critical voice — investors disagree, and the disagreement is signal.

### 4. Closing remarks

**Captured in**: `pitch-meeting/transcript.md` (final section)

Each investor (5 fixed + Domain Expert + Customer = 7 closers; Founder closes separately) gives:

- 2–3 sentence final reflection
- **Decision for the chosen commitment mode**: `PASS` / `SOFT-PASS` / `INTERESTED` / `INVEST`
- **Best-fit commitment mode** note: "I'd pass at unicorn but it's an INVEST at full-time-solo"
- **Score components**:
  - Pitch fit for chosen mode (1–10)
  - Idea soundness regardless of mode (1–10)

The Founder's close is separate, in `founder-reflection.md` (see below).

### 5. Post-pitch perception survey

**Saved as**: `pitch-meeting/post-pitch-survey.md`

Same three axes as pre-pitch. Each panelist re-rates after seeing the deck and Q&A.

This is where the **perception gap** becomes legible. A pitch where the cold opinion was 5/10/4 and the post-pitch is 8/9/7 moved the room dramatically. A pitch that started 7/8/7 and ended 5/6/5 *broke* the room — the more they heard, the less they liked it.

### 6. Perception-gap analysis

**Saved as**: `pitch-meeting/perception-gap.md`

A short analytical document:
- Per-panelist pre-vs-post deltas, with sign and magnitude.
- The **founder's gap from the room**: did the founder's pre-pitch optimism match the room's, or were they alone?
- Which axes moved most (idea / viability / profitability)?
- One-paragraph synthesis: did the pitch persuade, fail to persuade, or actively un-persuade?

This is the meeting's most analytical artifact. The user can skim 10 of these across a season and see patterns: "Pitches that opened with a customer moment moved viability by +1.5 on average. Pitches that opened with TAM moved viability by 0."

## The transcript format (voice-render-ready)

The full transcript lives in `pitch-meeting/transcript.md`. It's intentionally formatted to be:

1. **Pleasant to read** as plain markdown.
2. **Trivial to parse** for a visual-novel renderer or TTS pipeline.
3. **Compatible with major TTS services** (ElevenLabs Studio, OpenAI TTS, Play.ht, Murf, Cartesia, Web Speech API).

### Format rules

- Each turn is one paragraph.
- Speaker name is bold and uppercase, followed by a colon: `**FOUNDER:**`
- Stage directions are italicized lines on their own (e.g., `*The Skeptic glances at the deck.*`). TTS engines should be configured to skip these.
- Use plain English punctuation (`,` `.` `?` `!`). Avoid em-dashes mid-sentence (some TTS engines stutter on them) — use commas or short sentences.
- Reasonable line lengths; one paragraph per turn.
- No headers inside the dialogue. Section headers are `## Section name` and stand alone between paragraphs.

### Example excerpt

```markdown
## Q&A

**BOOTSTRAPPER:** OK so the buyer is solo lawyers running IOLTAs, you said five hundred thousand of them in the US. How does customer number one find you?

**FOUNDER:** Cold email to the California Bar audit cohort. Roughly two hundred names per quarter, public list, real targeting.

**BOOTSTRAPPER:** Conversion rate?

**FOUNDER:** I haven't tested yet. The benchmark for compliance-fear cold email in adjacent verticals is two to three percent.

*The Skeptic shifts forward.*

**SKEPTIC:** Two to three percent of two hundred is four to six customers per quarter. At fifteen dollars a month, that's roughly seventy to a hundred dollars in new MRR per quarter. How long until you're at one thousand MRR?

**FOUNDER:** Twelve to eighteen months on cold email alone. State bar listing partnerships shorten that.
```

Stable speaker tags (BOOTSTRAPPER, OPERATOR, SEED_VC, GROWTH_VC, SKEPTIC, DOMAIN_EXPERT, CUSTOMER, FOUNDER) make it trivial for any TTS engine to assign distinct voices.

### Companion JSON

For each transcript, also write `transcript.json` with the same content as structured turns. This is what the visual-novel HTML and the audio-export tooling consume.

```json
{
  "pitch_slug": "trust-ledger-desktop",
  "commitment_mode": "passive-income",
  "panel": ["BOOTSTRAPPER", "OPERATOR", "SEED_VC", "GROWTH_VC", "SKEPTIC", "DOMAIN_EXPERT", "CUSTOMER", "FOUNDER"],
  "turns": [
    { "speaker": "FOUNDER", "kind": "narrative", "text": "Imagine you're a solo lawyer in California..." },
    { "speaker": "BOOTSTRAPPER", "kind": "question", "text": "OK so the buyer is..." },
    { "speaker": "FOUNDER", "kind": "answer", "text": "Cold email to the California Bar..." },
    { "speaker": "stage", "kind": "direction", "text": "The Skeptic shifts forward." },
    { "speaker": "SKEPTIC", "kind": "question", "text": "Two to three percent of..." }
  ]
}
```

## Audio rendering

The skill produces every transcript in a format ready for audio playback. The user has a spectrum of options from "click play right now, $0" to "studio-grade voiced episode."

### Tier 1 — Web Speech API (zero setup, in-browser, free)

The `assets/visual-novel-template.html` ships with a "▶ Play" button that walks through the transcript using the browser's built-in `SpeechSynthesisUtterance` API. No keys, no signup, no install.

**Honest tradeoffs:**
- macOS Safari and Chrome have decent voices (Samantha, Daniel, Karen, Moira). Set `voice` per speaker so the panel sounds different.
- Windows Edge has Microsoft Neural voices (Aria, Guy) which are noticeably better.
- Linux/Chromium's default voices are robotic.
- Pacing is mechanical (no emotion).
- **Verdict**: fine for first-draft listening, "feels like an audiobook on 1.0x speed". Not a polished podcast. The user can decide whether that bar is good enough; many people will find it sufficient for getting the gist while doing other tasks.

The visual-novel HTML maps speakers to voices automatically. The user can override voices via the dropdown in the playback panel.

### Tier 2 — OpenAI TTS API (cheap, good quality, ~$0.30 per pitch)

OpenAI's `tts-1` and `tts-1-hd` endpoints support 6 voices (alloy, echo, fable, nova, onyx, shimmer) at $15/1M characters. A typical pitch transcript is ~5K characters, so generating audio costs ~$0.075 per pitch on `tts-1`, ~$0.30 on `tts-1-hd`.

`pitches/audio-rendering.md` includes a Python script that takes `transcript.json`, assigns voices per speaker, and produces a single concatenated MP3 per pitch.

### Tier 3 — ElevenLabs Studio (best quality, paid, ~$5–$300/mo)

Highest fidelity. ElevenLabs Studio accepts a multi-speaker script with stable speaker tags. The user can:
1. Upload `transcript.md` directly to Studio.
2. Assign one voice per stable speaker tag (BOOTSTRAPPER, OPERATOR, etc.) — set this once, reuse across pitches.
3. Render the whole episode in 30–90 seconds per minute of script.

ElevenLabs voices have emotion-tagging via SSML if the user wants to escalate. For most pitches, the default reading is plenty.

### Tier 4 — Play.ht / Murf / Cartesia / Resemble (similar tier to ElevenLabs)

All accept the same `transcript.md` format. Voice quality and pricing vary; the user picks based on preference. The skill's transcripts work in any of them.

### Tier 5 — Local / private (open-source TTS)

For privacy-conscious users or zero-cost-at-scale: Piper, Coqui XTTS, Bark, StyleTTS 2. These run locally on consumer hardware. Quality varies — Piper is fast and acceptable; XTTS is higher quality but slower; Bark sounds the best but is the slowest.

`pitches/audio-rendering.md` provides a pointer to the relevant repos and a minimal `transcript.json → wav` script for Piper.

### Recommended default

For first-time use: **Web Speech API in the visual novel** (Tier 1). It's free, immediate, and pleasant enough to validate the format. If the user wants to share a polished episode externally, **upgrade to ElevenLabs Studio** (Tier 3). For batch-processing many pitches into a podcast feed, **OpenAI TTS** (Tier 2) is the sweet spot.

The skill writes `pitches/audio-rendering.md` per run with concrete copy-paste instructions for each tier, customized to the run's transcript format.

## The visual novel — Shark Tank / Dragons' Den replay

`assets/visual-novel-template.html` renders one pitch as a single-page HTML "episode." It loads `transcript.json` (sibling file) and renders:

- A header with the pitch name, commitment mode, and panel decision spread (e.g., "2 INVEST · 3 INTERESTED · 2 PASS")
- An avatar row at the top showing each panelist with their decision badge
- A speech-bubble flow rendering each turn
- A "▶ Play" button that triggers Web Speech API playback through the turns
- A speed slider (0.75×, 1×, 1.25×, 1.5×, 2×)
- A "skip-to-decisions" jump button
- "Pre-pitch / Post-pitch perception" radar overlay (optional toggle) that shows the room's opinion shift

The visual style is intentionally TV-show-coded — it should feel like an episode of Shark Tank or Dragons' Den, not a corporate pitch deck. Dark stage, bright spotlights on speakers, a season counter in the corner ("S1 E4 of 10").

## The season recap

`assets/season-recap-template.html` is the run-level landing page. It links every pitch's visual novel as an "episode card" — like a streaming service's season grid. Each card shows:

- Pitch name + slug + episode number (E1 of N)
- One-line thesis
- Decision spread badge
- Pitch-style tag (bold/novel · niche · laser · solid)
- Composite score
- Click → opens the visual novel for that pitch

The recap also includes a "Showrunner's notes" panel summarizing the post-mortem: what landed across the season, what bombed, what the user should pay attention to.

## What "good" looks like in a transcript

- The room **disagrees** with each other in non-trivial ways (Skeptic + Growth VC arguing about moat; Operator + Bootstrapper agreeing on bootstrappability but disagreeing on margin).
- The Founder gets **specific** with numbers when pressed, and admits when they don't have a number.
- **Customer Avatar interjects** at least twice and at least once notices something the investors missed (because the customer cares about workflow fit, not market size).
- The Domain Expert calls out one regulatory / cultural / industry-specific thing at least once.
- The transcript ends with **at least two contrasting decisions** in the closing remarks — pure unanimous PASS or unanimous INVEST is rare in real pitches.

## What "bad" looks like in a transcript

- Everyone sounds the same. Distinct voices are the whole point.
- The Founder is uniformly confident or uniformly defensive. Real founders are nervous in places, overconfident in others.
- Investors quote each other's portfolio companies in stilted ways. Composite ≠ impression.
- The Customer Avatar is silent or repeats investor talking points.
- All decisions cluster in one direction.

If a draft transcript reads like any of the above, rewrite it with sharper voice differentiation per `references/investor-panel.md`.
