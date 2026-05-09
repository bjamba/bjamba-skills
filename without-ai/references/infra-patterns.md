# Infrastructure patterns

Standard moves for replacing AI with infrastructure. Each pattern names what AI is doing today, what the without-ai equivalent looks like, and what the AI-trending-to-zero curve typically looks like for it. Use these as building blocks when you design the architecture in Phase 1, Step 4.

Most non-trivial systems combine several of these.

---

## Data patterns (state and content)

### Pattern: Schema + database + admin UI

**AI is doing:** Holding state in its context window — characters, recipes, workouts, books, customers.

**Without-ai version:** A SQLite (or Postgres if multi-user) database with a schema, plus a thin web or CLI admin UI to read/write rows. JSON or YAML files can substitute when the volume is small.

**AI bootstrap role:** Generate the initial schema, the migrations, and a seed of placeholder rows. Generate the admin UI scaffolding (CRUD forms).

**Steady-state AI role:** Zero. The user adds and edits rows directly.

**When this pattern fits:** Anywhere the user wants the system to remember things across sessions. Almost every category 3 or 5 prompt.

### Pattern: Indexed corpus + search

**AI is doing:** Reading the user's notes/journal/docs into context to answer questions.

**Without-ai version:** Index the corpus (SQLite FTS5, Tantivy, ripgrep, or — for larger collections — a vector DB you self-host like Qdrant or Chroma). Build a search UI that returns hits with surrounding context.

**AI bootstrap role:** Write the indexer, the search UI, and the initial query parser. Optionally a small synthesis layer for "summarize the top 5 hits" — but the user can always read the hits directly.

**Steady-state AI role:** Optional and small. Synthesis on top of search results if the user wants it. The index is the durable thing.

**When this pattern fits:** Category 7 prompts. Also any "remind me what I said about X" use case.

### Pattern: Personal context store

**AI is doing:** Reaccepting the user's personal context every conversation.

**Without-ai version:** A structured personal data layer — facts about the user, goals, projects, relationships, preferences, ongoing situations. YAML or markdown files in a folder, indexable, hand-editable. Tools (planners, writers, schedulers) read from it.

**AI bootstrap role:** Help the user enumerate and structure the initial set of facts. Suggest categories.

**Steady-state AI role:** Zero. The user (and the user's tools) edit it directly. *If* an LLM is in the loop later, it reads from this store rather than asking the user to re-explain.

**When this pattern fits:** Category 5 prompts. Foundation for many personal-tool builds.

---

## Logic patterns (rules and decisions)

### Pattern: Domain-specific language (DSL) + interpreter

**AI is doing:** Adjudicating rules in prose ("does this card's ability trigger?").

**Without-ai version:** Define a small DSL — a JSON/YAML schema, an s-expression syntax, a Lua sandbox, or a hand-rolled mini-language — that captures the rules formally. Build an interpreter that evaluates it deterministically.

**AI bootstrap role:** Help the user design the DSL grammar. Translate sample prose-rules into DSL. Generate test cases.

**Steady-state AI role:** Zero. The interpreter is the source of truth. *Optionally*, an LLM at the *frontend* can parse natural-language inputs into DSL — but the DSL is what runs.

**When this pattern fits:** Category 4 prompts. Card games, tax/legal calc, scheduling, eligibility checks, anything with formal rules.

**Watch for:** People often underestimate how small the DSL needs to be. Start with the smallest grammar that covers 80% of cases. Hand-write the 20% as exceptions.

### Pattern: Rules engine over a taxonomy

**AI is doing:** Categorizing or routing items ("which folder does this email belong in").

**Without-ai version:** A taxonomy (tags, categories, types) plus rules — regex, simple ML if warranted, or hand-curated patterns. Logged misses become new rules.

**AI bootstrap role:** Generate the initial taxonomy and the seed rules from a sample of items.

**Steady-state AI role:** Optional fallback for items the rules don't catch, with logging so the rules grow.

**When this pattern fits:** Category 2 prompts. Email triage, expense categorization, support-ticket routing.

### Pattern: Constraint solver

**AI is doing:** Producing schedules, assignments, or layouts that satisfy constraints.

**Without-ai version:** A real constraint solver (OR-Tools, MiniZinc, Z3) or a hand-rolled solver if the problem is small. Inputs are structured, outputs are deterministic.

**AI bootstrap role:** Help the user encode the constraints. Generate test cases.

**Steady-state AI role:** Zero, unless natural-language constraint editing is a feature, in which case LLM-as-parser is the right shape.

**When this pattern fits:** Scheduling, packing, room assignments, fantasy-sports lineups, level-design constraints.

---

## Asset-tool patterns

These are the patterns most central to the user's brief — the cases where AI is generating creative output and the without-ai answer is *a tool the user uses to make those assets themselves*.

### Pattern: Custom editor

**AI is doing:** Generating creative assets on demand (cards, sprites, levels, lessons).

**Without-ai version:** A handcrafted editor calibrated to the user's specific needs. Web-based (Canvas, SVG, WebGL) is usually the lowest-friction; native (Tauri, Electron, or a Pygame-style framework) when needed.

The editor reads and writes a **human-readable file format** — YAML, JSON, or a custom DSL — so files can be hand-edited, diffed, and version-controlled. Editing is *bidirectional*: the editor never owns more than the format.

**Asset-tool design checklist:**
- What's the smallest editing unit? (one card; one sprite; one lesson plan.)
- What primitives speed up the user? (templates, snippets, copy-from-similar, palette swaps.)
- What's the on-disk format and is it human-readable?
- What's the preview loop — can the user see their asset *in context* (the card in a hand; the sprite on the map; the lesson in a daily schedule)?
- Is bulk import/export possible? (CSV→cards, folder-of-PNGs→sprites.)
- Can two assets reference each other without breaking? (cross-references, IDs.)
- Smallest version that's actually useful (the v0 — often a textarea + a save button + a preview pane).

**AI bootstrap role:** Scaffold the editor. Generate placeholder assets to pre-populate so the user has something to react to.

**Steady-state AI role:** Zero, ideally. *Acceptable* residual roles: an "auto-fill from sketch" button that the user explicitly invokes; suggested completions the user accepts/rejects. The user is the author.

### Pattern: Procedural generator + curation

**AI is doing:** Generating endless variations of a thing (dungeons, names, NPCs, problem sets).

**Without-ai version:** A procedural generator with **knobs** — a seeded generator with parameters the user controls, plus a curation UI that lets them save/edit/discard outputs. The generator is deterministic given a seed; the user can rerun with the same seed and get the same output, or tweak the parameters.

**AI bootstrap role:** Help write the generator and the parameter set. Generate the random tables that feed it.

**Steady-state AI role:** Zero. The user owns the generator and the tables.

**When this pattern fits:** Anywhere an LLM is being used as a "give me 20 of these" engine — names, NPC backstories, math problems, enemy layouts.

### Pattern: Style/template library

**AI is doing:** Producing variations on a stylistic pattern (UI mocks, marketing copy templates, character portraits).

**Without-ai version:** A template library — hand-built or curated — that the user composes from. Could be SVG components, copy snippets, layered Photoshop files, mood boards.

**AI bootstrap role:** Generate the seed templates. Help organize them.

**Steady-state AI role:** Zero — the library is the asset. The user adds to it over time.

---

## Interface patterns

### Pattern: LLM-as-parser-only

**AI is doing:** Both parsing natural-language input *and* doing the underlying work.

**Without-ai version:** Demote the LLM to *parser-only* — it converts natural language into a structured query/command, and the deterministic system handles the rest. The LLM dependency shrinks because parsers are cheap, replaceable, and the load-bearing logic is yours.

**Use when:** Natural-language input is a real ergonomic win (search, command palette, voice notes) but the underlying operation should be deterministic.

**Concrete shape:** Natural language → small LLM call → JSON intent → your code → result. The user can also *bypass* the LLM and write the JSON intent directly (or use a structured form), so the system is fully usable without an API key.

### Pattern: Forms over chat

**AI is doing:** Conversing with the user to extract structured information.

**Without-ai version:** A form. Forms are deterministic, faster, and don't drift. Multi-step wizards for branching cases. If the form is long, save partial progress.

**Use when:** The information you need from the user is structured and bounded. Almost always the right move when the user is doing a *task* (booking, ordering, scheduling, configuring) rather than exploring.

### Pattern: Shortcuts over generation

**AI is doing:** Generating output the user could reach via a button.

**Without-ai version:** Buttons. A library of templates, shortcuts, recent items, "use last", "duplicate and edit". Generation gets reserved for the cases where shortcuts genuinely run out.

---

## How to combine

A typical without-ai design uses **3–6 patterns** wired together. Example for the MTG-clone case:

- **Schema + database** for the card library and decklists.
- **DSL + interpreter** for the rules engine.
- **Custom editor** for card creation.
- **Procedural generator + curation** for booster-pack generation and balance testing.
- **Style/template library** for art consistency (frames, mana symbols, type lines).
- **Forms over chat** anywhere the user is configuring (deck building, tournament setup).

Show the combination explicitly in `_overview.md` — name each pattern and what it's doing. The reader gets a vocabulary they can apply to the next prompt.

---

## A note on hosting

All patterns above should run on commodity hardware: the user's laptop, a Raspberry Pi, a single VPS, a NAS. Avoid:

- Cloud-native frameworks that assume a managed control plane.
- Anything that requires a GPU in steady state (LLM inference, image generation) unless the user explicitly wants to run a local model.
- Services with per-request billing.

Prefer:

- SQLite over Postgres unless multi-user write concurrency is real.
- Static-file deployment over containers when possible.
- A single binary or a single `docker-compose up` over multi-service architectures.
- Standard tools the user already has (the file system, ripgrep, sqlite3 CLI) over bespoke services.

The infrastructure should be something a solo person could keep running on a $5/month VPS or a laptop in a closet — not because that's the goal, but because *being able to* is the durability the user is paying for.
