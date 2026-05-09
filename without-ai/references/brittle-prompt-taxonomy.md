# Brittle-prompt taxonomy

Use this when categorizing the user's prompt in Phase 1, Step 2. The point is to give the user a vocabulary for *why* their prompt is or isn't a good candidate for the without-ai treatment, and to generalize their specific case to a class of prompts.

A prompt belongs to one or more of these categories. The more it matches, the stronger the case for building infrastructure.

---

## 1. Asset-generation-disguised-as-question

The user phrases it as a request, but the answer is a pile of generated assets — text, art, music, level layouts, character sheets, recipes, lesson plans, schedules. The LLM produces something on demand; the user wants those assets to be **owned, editable, and reproducible**.

**Examples:**
- "Design my game's cards." → wants a card-definition file format and an editor.
- "Generate art for my characters." → wants a sprite/portrait pipeline with consistent style controls.
- "Write the dialogue for my visual novel." → wants a script editor with character voice presets.
- "Plan my lessons for the semester." → wants a lesson-authoring tool with reusable units.

**Without-ai move:** Build the editor or pipeline. The user produces the assets; the infrastructure makes that producing fast and consistent.

**Tell-tale signs:** The user wants more than one asset; future versions will need to look or feel related; the LLM's output is non-deterministic and hard to iterate on.

---

## 2. Repeated-instance-of-the-same-pattern

The prompt looks like one question but the user is going to ask it a thousand times with small variations. They're paying tokens (and waiting on latency) for what should be a function call.

**Examples:**
- "Answer this kind of customer question for me." → wants a knowledge base + retrieval, not LLM-on-each-ticket.
- "Categorize this expense." → wants a rules engine over a category taxonomy.
- "Translate this product description." → wants a translation memory + glossary, possibly an LLM only for the unseen-before sentences.
- "Detect anomalies in my server logs." → wants a real metrics pipeline with thresholds.

**Without-ai move:** Build the deterministic version. AI can be the bootstrap (training the rules, populating the knowledge base) and the long-tail fallback (with logging so the fallbacks become rules over time). The 99% case stops paying tokens.

**Tell-tale signs:** The user uses the word "every time"; the prompt has obvious slots (`<insert customer message here>`); the answer rarely needs to be creative.

---

## 3. Stateful-thing-pretending-to-be-stateless

The prompt asks for an answer that should *remember* — workouts logged over months, books read over years, conversations with a partner, characters' arcs in a story. The LLM has at best a sliding window of memory; the user actually needs a database.

**Examples:**
- "Track my workouts and tell me when to deload." → wants a workout database with a heuristics layer.
- "Help me keep my novel's characters consistent." → wants a canon-bible app (see `/continuity-check`) layered on a character database.
- "Manage my reading list." → wants a books database, not a chat thread.

**Without-ai move:** Build the data model first, then the views, then *maybe* an LLM-backed query interface on top — but the data is the durable artifact.

**Tell-tale signs:** The user wants the answer to depend on history; "remind me when..." or "track..."; the prompt would degrade as the relevant history grows past context window.

---

## 4. Deterministic-rules-disguised-as-prose

The prompt asks the LLM to apply rules — game rules, tax rules, legal rules, scheduling rules — in natural language. LLMs apply rules unevenly. The right tool is a rules engine or DSL, possibly with an LLM as the *parser* of natural-language inputs into the formal model.

**Examples:**
- "Adjudicate this MTG turn." → wants a card-game rules engine.
- "Calculate my taxes given these inputs." → wants a tax-calc spreadsheet/program.
- "Schedule my team given these constraints." → wants a constraint solver.

**Without-ai move:** Design the formal model (DSL, schema, or constraint system). Build the evaluator. Optionally wire an LLM as the natural-language frontend — but it parses, not adjudicates.

**Tell-tale signs:** Words like "given", "calculate", "if-then"; the user gets frustrated when the LLM gets it slightly wrong; the same input should always produce the same output.

---

## 5. Personal-context-that-should-be-durable

The user wants the LLM to "know them" — their goals, projects, schedules, kids, food preferences, exercise routines. They re-supply this context every conversation. The infrastructure is **a personal data layer** they own.

**Examples:**
- "Plan my week given everything you know about me." → wants a personal context store + a planning tool that reads it.
- "Suggest meals based on my pantry and dietary stuff." → wants a pantry database + meal database.
- "Help me write to my friends in my voice." → see `/draft-me`, which is exactly this.

**Without-ai move:** Build the personal data store as the durable artifact. Tools read from it. The user can change LLMs (or stop using one) and keep the data.

**Tell-tale signs:** The user re-explains the same context in every prompt; they say "you know I have..." to a model that doesn't; the answer requires a stable view of *them*.

---

## 6. Creative-tool-the-user-actually-wants

The user prompts an LLM for something creative — a song, a comic, a game level, a piece of code — but what they actually want is **the satisfaction of making it themselves**. The LLM is a substitute for a tool they don't have.

**Examples:**
- "Write me a song." → wants a music sequencer with sample library.
- "Make me a webcomic." → wants a paneling/lettering tool with character templates.
- "Generate a dungeon for my D&D campaign." → wants a dungeon editor with random-table support.

**Without-ai move:** Build (or recommend) the tool. The without-ai output here is sometimes "use this existing tool" rather than scaffolding from scratch — be honest if Garage­Band, Tiled, Inkscape, etc. is already the right answer. Custom tools win when the user's needs are narrow enough that off-the-shelf is overkill or wrong.

**Tell-tale signs:** The user wants to *show people* what they made and feel ownership; they get visibly less satisfied with each LLM iteration; "I want to be able to..." phrasing.

---

## 7. Search-disguised-as-Q&A

The user is asking the LLM something that's actually answered by **the documents they already have** (or a public corpus they could index). The LLM is a smudgy proxy for full-text search + a small synthesis layer.

**Examples:**
- "What did I write in my journal about my grandmother?" → wants journal indexing.
- "Find that thing in my notes about the API rate limit." → wants notes search.
- "What are the takeaways from my last six all-hands?" → wants meeting-notes database.

**Without-ai move:** Index the corpus (SQLite FTS, ripgrep, or similar). Optional small LLM on top for synthesis if needed — but the search index is the durable thing.

**Tell-tale signs:** The user has the source documents already; they want quotes/citations; "where did I write...".

---

## When the prompt does *not* belong here

Some prompts are genuinely well-served by an LLM and the without-ai treatment is overkill or actively harmful:

- **One-shot creative prompts** the user will never repeat ("name my band").
- **Open-ended exploration** where the user is brainstorming and *wants* the LLM's randomness.
- **Tasks at the edge of the user's expertise** where the LLM is closing a knowledge gap, not a tooling gap.
- **Tasks where the LLM is the product** ("I want a chatbot that talks like me") — the LLM dependency is the feature.

If the user's prompt fits these, say so. The honest "this isn't a without-ai case" is more valuable than another pile of artifacts.

---

## How to use this in the overview

In `ai-vs-without-ai.md`, after categorizing the user's prompt, write a short section that:

1. Names the categories that apply.
2. For each, generalizes from the user's specific prompt to the class of prompts it represents ("any time you find yourself asking an LLM to *adjudicate game rules*, you're hitting category 4...").
3. Gives the user one or two other example prompts in the same category, so they recognize it next time.

This is the most reusable writing in the whole run — the user's mental model upgrades from "I had a question and the LLM answered it" to "I had a class of question and I built infrastructure for it."
