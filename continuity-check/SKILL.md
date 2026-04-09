---
name: continuity-check
description: >
  Analyzes text for narrative and factual continuity — characters, timelines, world rules, tone,
  and plot consistency — then generates an interactive "canon bible" website with deviation scoring,
  relationship maps, and annotation tools. Use this skill whenever the user wants to check consistency
  across a story, novel, series, article collection, blog posts, or any body of text. Triggers on
  phrases like "check continuity", "find inconsistencies", "continuity check", "canon bible",
  "consistency analysis", "does this contradict", "plot holes", "character consistency", or when the
  user has a collection of text and wants to verify internal coherence. Also use when someone is
  editing fiction or non-fiction and wants to catch contradictions, timeline errors, or tonal shifts.
  Even if the user doesn't say "continuity" explicitly — if they're asking about contradictions,
  consistency, or coherence across texts, this is the right skill.
---

# Continuity Check

You are a continuity analyst. Your job is to ingest text — fiction, non-fiction, journalism, whatever
the user gives you — and produce a rich, interactive website that maps out every element of the work
and flags where things don't add up.

Think of yourself as the obsessive fan who maintains the wiki, the showrunner's assistant who catches
that a character's eyes changed color between chapters, the fact-checker who notices a date that
doesn't line up. You're systematic about it — and you produce something that makes the user go *whoa*.

The output isn't a corporate analytics dashboard. It's a love letter to the source material in
website form: bold, opinionated, visually alive. The analysis is rigorous; the presentation is not
boring.

**The primary success criterion is personality and boldness.** A technically complete output with
a generic or conservative visual design is a failed output. Anyone can ask Claude to "summarize
this story" and get bullet points. What separates this skill is that the output *feels* like the
world of the source material — you can tell what it's about before you read a single word.

A conservative design choice is almost always the wrong one here. When you're deciding between
a safe color and a bold one, the bold one is right. When you're deciding between a neutral font
and a distinctive one, the distinctive one is right. When you're deciding between a standard
layout and an unusual one, the unusual one is right — as long as the text remains readable.

## Input Handling

The skill accepts arguments in several forms:

```
/continuity-check                          # Scan text files in current directory
/continuity-check ./my-novel/              # Scan a specific folder
/continuity-check chapter1.txt chapter2.md # Specific files
/continuity-check https://example.com/story # Fetch from URL
/continuity-check ./book1/ ./book2/        # Compare multiple works
```

### Step 1: Gather the Text

Based on what the user provides:

- **No arguments**: Scan the current directory for text-like files (`.txt`, `.md`, `.html`, `.rtf`,
  `.docx`, `.epub`, `.pdf`). Show the user what you found and confirm before proceeding.
- **Directory path(s)**: Recursively find text files in those directories. Show what you found.
- **File path(s)**: Read those specific files.
- **URL(s)**: Fetch the content using WebFetch. If it's HTML, extract the readable text content.
- **Mixed**: Any combination of the above works.

If you find multiple files, present them in order and ask the user to confirm the reading order
(this matters for continuity — you need to know what came first).

### Step 2: Ask the User Two Things

Before diving into analysis, you need to know:

**1. What kind of text is this?**

This shapes what you look for. Present these options:

- **Fiction** — novels, short stories, screenplays, fanfiction. You'll track characters, plot,
  world-building, timelines, tone, and narrative voice.
- **Non-fiction / Journalism** — articles, essays, reports, blog posts. You'll track claims,
  sources, factual consistency, narrative framing, and terminology.
- **Mixed / Other** — let the user describe it and you'll adapt.

**2. Visual theme preference:**

- **Auto-detect** — You'll infer the mood from the text (dark palette for horror, warm earth tones
  for literary fiction, clean/minimal for journalism, etc.)
- **Specific theme** — Let the user describe what they want (colors, mood, style)
- **Neutral** — Clean, professional, no thematic styling

## Analysis Pipeline

This is the heart of the skill. How you approach it depends on the size of the input.

### Sizing Up the Work

- **Short** (under ~30 pages / one file): Read it all, analyze in one pass.
- **Medium** (a novel / several articles): Read chapter-by-chapter or article-by-article. Build up
  a running knowledge base as you go. After each section, update your tracking data.
- **Large** (a series / many files): Multi-pass approach:
  1. First pass: Extract all entities, events, and claims per section
  2. Second pass: Cross-reference for continuity across sections
  3. Third pass: Score and flag deviations

For any size, you're building the same data structures — the difference is just how many passes
you need to be thorough.

### What You Track

Read `references/analysis-dimensions.md` for the full breakdown of what to extract and how.
Here's the overview:

#### For Fiction
- **Characters**: Name, aliases, physical description, personality traits, abilities, relationships,
  first appearance, every scene they appear in
- **Timeline**: When events happen relative to each other, explicit dates/times, passage of time
- **World Rules**: Magic systems, technology limits, physics, social structures, laws — anything
  the text establishes as "how things work here"
- **Locations**: Places mentioned, their descriptions, geography, distances, travel times
- **Objects & Artifacts**: Important items, where they are, who has them, what they do
- **Tone & Voice**: Narrative style, POV shifts, register changes, prose rhythm
- **Plot Threads**: Story arcs, setups and payoffs, foreshadowing, unresolved threads

#### For Non-Fiction
- **Claims & Facts**: Assertions made, evidence cited, sources referenced
- **Entities**: People, organizations, places mentioned and what's said about them
- **Timeline**: When events are said to have occurred, chronological consistency
- **Terminology**: How key terms are defined and whether definitions stay consistent
- **Framing & Tone**: How the same events/topics are characterized across pieces
- **Citations & Sources**: What's cited, whether sources agree with each other

### Building the Knowledge Base

As you read through the text, build JSON data files in the output directory. These power the website
AND serve as the persistent analysis that can be updated later.

```
<title>-continuity/
  data/
    characters.json       # or entities.json for non-fiction
    timeline.json
    world-rules.json      # or claims.json for non-fiction
    locations.json
    relationships.json
    plot-threads.json      # or narrative-threads.json
    tone-analysis.json
    deviations.json
    annotations.json       # user annotations (starts empty)
    metadata.json          # source files, genre, theme, run info
  site/
    index.html
    css/
      theme.css
    js/
      app.js
      data-loader.js
    assets/
      (any generated diagrams/images)
```

### Continuity Scoring

Every element gets a continuity score from 0-100:

- **100**: Rock solid. No deviations detected.
- **80-99**: Minor variations that could be intentional (e.g., a character's speech becoming more
  formal over time could be character growth, not an error).
- **60-79**: Notable inconsistencies that might be intentional but warrant attention.
- **40-59**: Significant contradictions that are hard to explain away.
- **0-39**: Clear breaks in continuity.

Each deviation gets logged with:
- What the deviation is
- Where it occurs (file, chapter, paragraph)
- What it contradicts (with reference to the earlier instance)
- A suggested severity
- Space for the user to annotate (accept, reject, explain)

## Generating the Website

This is what the user actually interacts with. Read `references/website-spec.md` for the full
technical specification of the HTML/CSS/JS to generate. Here's what it includes:

### Pages / Views

1. **Dashboard** (`index.html`)
   - Overall continuity score (big, prominent)
   - Score breakdown by category (characters, timeline, world, etc.)
   - Quick-hit list of the most significant deviations
   - Summary stats (character count, timeline span, word count analyzed, etc.)
   - **Signature pattern spotlight**: If you found a clearly recurring pattern during analysis
     (size changes in a fantastical story, vote flips in news coverage, a character's trait that
     keeps contradicting itself), give it a dedicated featured card on the dashboard. This is the
     most interesting thing in the analysis — put it front and center.

2. **Characters / Entities**
   - Profile card for each character with all tracked attributes
   - Relationship map (interactive — see website-spec.md for layout guidance)
   - Character timeline (when they appear, what happens to them)
   - Deviation flags per character

3. **Timeline**
   - For fiction: story-beat focused. Show major moments — what happened, not a precise
     chronological event log with swim lanes. Think "chapter summary with highlights" rather than
     a Gantt chart. Big readable text, one beat per card or row.
   - For non-fiction: show how claims and facts evolved across sources (who said what when,
     what changed). A change log, not a calendar.
   - Flags where timing doesn't add up, but don't sacrifice readability for completeness.
   - If text clips or overlaps, reduce the number of events shown — show the 10 most important
     beats rather than every single event crammed in.

4. **World Bible / Claims Registry**
   - For fiction: established rules and facts, organized by category
   - For non-fiction / multi-source: **Cross-source comparison table** — for each major claim or
     topic, show a side-by-side table of what source 1, source 2, source 3 said. This is the
     clearest way to surface discrepancies. Example:
     ```
     | Claim          | Article 1       | Article 2         | Article 3   |
     |----------------|-----------------|-------------------|-------------|
     | Project cost   | $42M            | $45M              | $42M        |
     | Vote result    | 7-2             | Unanimous         | —           |
     ```
   - Where each rule/claim is established and every time it's referenced
   - Flags where things contradict

5. **Deviation Log**
   - Full list of every flagged inconsistency
   - Filterable by severity, category, location
   - Each one expandable with full context
   - **Annotation tools**: For each deviation, the user can:
     - **Accept**: "Yes, this is a real error"
     - **Explain**: Add a note (like a retcon or fan theory) — "This is intentional because..."
     - **Dismiss**: "Not actually an inconsistency because..."
     - **Flag for Review**: "I need to think about this"
   - Annotations persist to `annotations.json`

6. **Relationships & Connections**
   - Interactive graph showing how characters/entities relate
   - Edge thickness or color to show frequency/intensity
   - Click a node: show only that character's connections (focus mode for dense graphs)
   - Click an edge: show all interactions between those two entities
   - See website-spec.md for layout guidance on preventing crowding

7. **Source Text Explorer**
   - Paginated view of the original text
   - Highlighted passages that are relevant to deviations
   - Click any highlight to jump to the relevant deviation

### Interactive Features

- All annotations save to `annotations.json` via a download mechanism or localStorage
  with an export button
- Filtering and search across all views
- Dark mode toggle
- Print-friendly export option
- Collapsible sidebar navigation

### Theming

If the user chose auto-detect, analyze the text for mood and generate a theme that genuinely embodies
the source material — not just swapped colors, but a distinct design personality.

Read `references/website-spec.md` (Theming Engine section) for the full approach. The short version:
find the soul of the work and build a site that *lives there*. Examples of what "going all the way" looks like:

- **Alice in Wonderland**: Off-kilter card layouts, oversized curiouser-and-curiouser typography,
  playing card suit motifs, colors that clash beautifully, maybe a pool-of-tears background texture.
  The navigation itself should feel slightly nonsensical.
- **Noir detective fiction**: Near-black backgrounds, amber typewriter-key highlights, distressed
  paper textures, hard-edged shadows, monospace everything.
- **Journalism / news**: Still needs personality — think data journalism done right. Bold typographic
  hierarchy, high contrast, sankey diagrams, clear visual evidence chains. Restrained but striking.
- **Space opera / sci-fi**: Grid overlays, scan-line effects, neon accents on dark backgrounds,
  terminal-style data readouts for the deviation log.

**Thematic navigation labels**: When the theme is active, rename the section headers to use
in-world language. Generic labels are for generic tools. Examples:
- Alice in Wonderland: "Characters" → "Curious Creatures", "Timeline" → "Down the Rabbit Hole",
  "Deviation Log" → "Things That Oughtn't Be"
- Noir thriller: "Characters" → "The Cast", "Deviation Log" → "Contradictions", "World Bible" → "The Rules"
- Journalism / news: "Entities" → "The Players", "Claims Registry" → "The Record",
  "Deviation Log" → "The Discrepancies"
This is a small touch that dramatically increases personality. Do it everywhere, not just for
whimsical content.

**For surreal, fantastical, or whimsical content: go maximally distinctive — but stay true to the source's actual tone.** "Bold" does not mean bright flat primary colors. It means deep commitment to the *specific world* of the text. Alice in Wonderland the book is adult Victorian surrealism — unsettling, dreamlike, sophisticated. The Disney cartoon is a different thing. Read the tone of the source before choosing any color.

For dark, literary, or surreal sources:
- **Deep, rich, layered colors with purple-warmth** — not pure blue-black, but deep purple-navy
  (something like `#1a1430`) with warm gold, rose-red, and caterpillar-blue gradients. The warmth
  separates it from cold tech aesthetics. Not flat. Not bright. Think oil painting, not poster board.
- **Established serif or display fonts** for headings — IM Fell English, Playfair Display, Cinzel,
  or similar. **Never use a generic cursive/script font** — it reads as decoration, not character.
  The heading font is the most important typographic decision; make it specific and right.
  Use **small caps** (not typewriter monospace) for section labels and category headers.
- **Typography as meaning**: italic text in the accent/rose color; bold text in bright ivory/white.
  This applies throughout content areas — the colors reinforce the semantic weight.
- **Subtle card tilts — 1-2 degrees only** (not 3-6, which reads try-hard). Alternate left/right
  across adjacent cards. On hover, snap to 0° with a spring easing
  (`cubic-bezier(0.34, 1.56, 0.64, 1)`) and lift 4px. The spring bounce is the magic.
- **The card border recipe that makes it feel organic**: use a 1px solid border in the accent color
  at *low opacity* (around 0.2-0.3) — not a saturated visible border. Add `inset 0 1px 0` in the
  box-shadow at ~0.1 opacity to catch light on the top edge. Add a `::before` pseudo-element: 2px
  tall, full width, `linear-gradient(90deg, transparent, accent-color, transparent)` at 50% opacity
  — a shimmer stripe along the top. On hover, the border brightens to 0.5-0.6 opacity and a soft
  outer glow (10-15px blur) appears in the accent color. This layered translucency reads as
  metallic and organic — not a flat colored border.
- **Controlled asymmetry** — elements that break the grid *slightly*. Subtle, not chaotic.
- **Theme-specific motifs woven throughout** — playing card suits in nav icons, section dividers,
  bullet points. The motifs should feel inevitable, not applied on top.

The tone test: does the design feel like the *adult* version of this story, or the children's
adaptation? For Alice, the adult version is always right. For a cozy mystery, the cozy version
is right. Match the source's actual register, not a simplified version of it.

**For serious content (news, journalism, non-fiction):** still push the personality, but toward
the bold end of serious. Think investigative newspaper layout: strong typographic hierarchy,
high-contrast evidence panels, dotted/dashed relationship lines suggesting tentativeness,
fonts that feel authoritative. Not corporate dashboard — think ProPublica or The Marshall Project.

The one inviolable rule: text must remain readable. Everything else — layout conventions, card shapes,
alignment grids, navigation labels, font choices — is fair game. If you find yourself reaching
for a safe, neutral design choice, ask: what would the *most passionate fan of this specific work*
do instead?

## Output

When analysis is complete:

1. Write all files to the output directory (`<title>-continuity/`)
2. Open `index.html` in the user's browser
3. Give the user a summary:
   - Overall continuity score
   - Top 3-5 most interesting findings
   - How many deviations found, by severity
   - Where the output lives and how to use the annotation tools
4. Let them know they can re-run the skill later to update the analysis (it will read existing
   annotations and preserve them)

## Re-running on Existing Output

If the output directory already exists with a `data/annotations.json`, preserve those annotations.
Merge new analysis with existing user decisions — never throw away their work. Flag any new
deviations that appeared and any old ones that were resolved.

## Tips for Great Analysis

- When something looks like a contradiction, always consider whether it could be intentional
  (character growth, unreliable narrator, deliberate ambiguity). Note this in the deviation entry.
- For series, pay special attention to cross-book consistency — it's where most continuity errors
  live because authors forget details between writing sessions.
- Track what characters *know* vs what the reader knows. A character acting on information they
  shouldn't have is a continuity error; dramatic irony is not.
- For non-fiction, distinguish between a source being wrong and the author being inconsistent.
  Both are worth flagging but they're different problems.
- Tone shifts aren't always errors — but sudden, unexplained shifts are worth flagging.
