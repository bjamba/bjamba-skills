# Voice Analysis

This is the full protocol for the ORIENT phase's voice analysis step, plus how to write and update `_meta/voice-profile.md`.

The point of voice analysis is not to produce a lyrical description of the user's style. It's to build a specific, testable mental model you can use to generate a draft that could only have come from this user, not from a generic template. The user will know within two sentences whether you got it right.

---

## What to look at

Two corpora, two different treatments:

**`format-samples/`** — pieces shaped like the target output. Teach you *both* format and voice. A cover-letters repo's format-samples are past cover letters. A blog-posts repo's format-samples are past blog posts.

**`voice-samples/`** — any of the user's writing in any form. Teaches you *only* voice. Explicitly ignore format signals here. A cover-letters repo might have journal entries in voice-samples — those tell you how they think, not how they structure a letter.

If one is empty, fall back to the other. If both are empty, ask the user to provide at least one sample before drafting; you can't fake a voice from nothing.

---

## What to extract

Work through these dimensions. For each, find specific evidence in the corpus and be ready to quote it. Vague observations ("warm", "professional") are useless — replace them with concrete ones ("opens with a personal anecdote before stating the ask").

### Format (from `format-samples/` only)

1. **Length norms.** Average word count. Range. Is there a shape they gravitate to?
2. **Opening pattern.** How do they start? With a hook? A fact about the target? A personal detail? A direct statement of intent? Are they ever generic ("I am writing to apply for...") or do they avoid that?
3. **Closing pattern.** How do they end? A callback to the opening? An action they're offering? A forward-looking line? A simple thank-you?
4. **Paragraph rhythm.** Short paragraphs mixed with long? Consistent medium? Any single-sentence paragraphs used for punch?
5. **Section structure.** Do they use explicit sections/headers, or flow without them? Transitions — abrupt or connective?
6. **Signature moves.** Are there specific structural tics — a recurring pattern like "three concrete examples then a broader point", or "question → personal story → landing"?

### Voice (from all corpus, weighted toward format-samples + voice-samples)

1. **Sentence rhythm.** Short and punchy? Long and layered? Mixed, and if so, how?
2. **Vocabulary register.** Casual, professional, formal, literary, technical? Any specific word choices that recur? Any words they seem to avoid?
3. **Emphasis strategy.** Do they use italics, dashes, parentheses, single-sentence paragraphs? How do they highlight?
4. **First-person usage.** How much "I"? Centered on self, or deflecting to the work/target?
5. **Concreteness.** Do they lean on specific details (names, numbers, moments) or stay abstract?
6. **Humor / warmth.** Do they use it? What kind — dry, self-deprecating, observational? Or is it consistently serious?
7. **Transitions and connectives.** "However", "But,", "—", "And here's the thing", "So"... what glues their sentences together?
8. **What they don't do.** As important as what they do. Do they never use exclamation marks? Never end with "please let me know if you have questions"? Never say "passionate"?

---

## How to share the analysis with the user

Write 3–6 specific, quotable observations. Each one should be something the user could agree or disagree with. Include short quotes from their corpus as evidence.

**Bad:**
> You have a professional but warm voice with good attention to detail.

**Good:**
> A few things I'm noticing:
> - You open every letter with a concrete detail about the target — their product, their team, a talk someone gave — rather than a summary of yourself. ("I've been watching how the Zillow team approaches...")
> - Your paragraphs are short. Most are 2–3 sentences, max 4. Single-sentence paragraphs show up when you want to land a point.
> - You never use "passionate". You prefer specific verbs: "built", "shipped", "led", "owned".
> - You close with forward-looking action, not thanks. "Here's what I'd want to dig into first week" rather than "Thank you for your consideration."
> - You use dashes — often — for parenthetical emphasis. Rarely parentheses.
> - In voice-samples, you use semicolons and em-dashes heavily; I'll mirror that in prose but tone it down for a formal letter.

Then ask: "Does this sound right? Anything I'm overweighting or missing?"

If the user corrects, update your model before moving to brainstorm. If they sign off, move on.

---

## The voice profile file (`_meta/voice-profile.md`)

This is the skill's accumulated understanding of the user's voice across sessions. It's regenerated/updated in FINALIZE, not ORIENT. ORIENT reads it as a warm start; FINALIZE updates it based on what was learned in this session.

### Structure

```markdown
# Voice Profile

_Last updated: 2026-04-16 (session: 2026-04-16-zillow-senior-engineer)_

## Summary

One short paragraph summarizing the writer's voice in the most useful
terms — what makes their writing recognizably theirs.

## Format patterns (from format-samples/)

- Length: typically 280–320 words for cover letters.
- Opens with a concrete detail about the target, never a generic intro.
- Paragraph rhythm: short, 2–3 sentences. Single-sentence paragraphs for emphasis.
- Closes with forward-looking action; avoids "thank you for your consideration".

## Voice patterns (from voice-samples/ + format-samples/)

- Specific verbs preferred: "built", "shipped", "owned", "led". Avoids "passionate", "excited", "thrilled".
- Sentence rhythm: mixed, but leans short. Long sentences layer clauses with em-dashes.
- Uses em-dashes for parenthetical — frequently.
- Rarely uses exclamation points.
- First-person present but deflects to work: "we shipped X" more than "I did Y".

## What to avoid

- Cliché openers ("I am writing to apply for...")
- Generic closes ("Please feel free to reach out")
- Filler adjectives ("innovative", "dynamic", "passionate")
- Overly formal register — they prefer directness

## Evolution notes

- 2026-04-16: First session, profile initialized from 4 format-samples.
- 2026-04-22: Noticed heavier humor when writing to startups vs. large companies —
  may want to branch the profile by target type if this pattern holds.
```

### Update rules

- On first FINALIZE: create the file, populate from whatever samples exist + what you learned in the session.
- On subsequent FINALIZE: **append** observations — don't rewrite wholesale. Add to "Evolution notes" with the date and what you noticed. Update the core sections only when something is clearly sharper or has shifted.
- If two sessions contradict each other (e.g., one piece was short, one was long), note the contradiction and ask the user in the next session which applies — or whether the voice is context-dependent.

### What NOT to put in the voice profile

- The user's personal details (name, address, employers) — those belong in `about-me/`, curated by the user.
- Content from specific sessions (job descriptions, specific drafts) — those stay in session folders.
- Anything that would identify a specific target/recipient — the profile should be context-agnostic.

---

## When the corpus is thin

If there are only one or two samples:

- Be upfront with the user: "I only have two samples to work from, so my read of your voice is tentative. I'll draft based on what I see, but please expect to do more correction in review than usual."
- Lean harder on the brainstorm phase. The user's live explanation of what they want fills the gap when the corpus can't.
- Flag specific patterns as *hypotheses* rather than observations: "You seem to prefer short paragraphs — but I'm inferring from two samples, so tell me if that's wrong."

## When the corpus is rich but inconsistent

Some users have written in different voices for different contexts. A blog-posts repo might have playful personal posts alongside serious technical ones. When you see inconsistency:

- Don't average. Averaging produces a bland middle that doesn't sound like any of their real writing.
- Cluster. Identify 2–3 distinct registers and ask the user which applies to the current piece.
- Quote examples of each register so the user can point to the one they want.

---

## A reminder

The final draft either sounds like the user or it doesn't. The user will know immediately. Every step above exists to make v1 land closer to what the user would have written themselves — so the review loop is about sharpening, not rescuing from generic-AI-voice.
