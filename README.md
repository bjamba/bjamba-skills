# bjamba-skills

A collection of custom Claude Code skills by [@bjamba](https://github.com/bjamba).

## Skills

### teach-me

A personalized learning coach that builds a complete curriculum and study environment for any topic. Give it a topic — anything from wine pairing to Rust programming to being a better listener — and it builds you a complete, interactive learning environment tailored to how you learn.

**What it does:**

1. **Interviews you** about what you want to learn, your goals, timeline, and how you like to learn
2. **Designs a curriculum** with modules, lessons, exercises, and milestones
3. **Builds a full repository** of interactive HTML lessons, flashcard apps, quizzes, progress dashboards, and whatever artifacts fit your learning style
4. **Tutors you** when you come back — picks up where you left off, keeps you on track, adapts the pace, and creates new material on the fly

**Usage:**

```
/teach-me how to pair wines with cheeses
```

Or just describe what you want to learn:

```
I want to get better at machine learning classification models
```

The skill also activates automatically when you open a conversation inside an existing teach-me repo (one that has a `curriculum.json` file) — it'll pick up where you left off in tutor mode.

**What it produces:**

- **`dashboard.html`** — Interactive progress dashboard you open in your browser. Tracks your journey visually.
- **HTML lessons** — Styled, navigable lesson pages (not flat markdown). Just double-click to open.
- **Interactive tools** — Flashcard apps, quizzes, matching games, reference cards, scenario practice tools. All single-file HTML, no dependencies.
- **`curriculum.json`** — Machine-readable curriculum state so Claude can pick up where you left off.
- **Exercises** — Hands-on practice tailored to the topic. Could be coding exercises, tasting worksheets, conversation scenarios, creative prompts — whatever fits.

For technical topics, it uses Jupyter notebooks instead of raw code files. For non-technical topics, everything is browser-based — no terminal required.

## Installation

**One-liner (personal install — available in all your projects):**

```bash
git clone https://github.com/bjamba/bjamba-skills.git ~/.claude/skills/bjamba-skills
```

**Per-project install (available only in a specific project):**

```bash
git clone https://github.com/bjamba/bjamba-skills.git .claude/skills/bjamba-skills
```

After installing, restart your Claude Code session. Skills will be available by their slash command (e.g. `/teach-me`) or will activate automatically based on context.

## Structure

```
bjamba-skills/
├── README.md
└── teach-me/
    ├── SKILL.md              # The skill definition
    ├── references/
    │   └── scaffolding-patterns.md  # Artifact patterns by topic type
    └── evals/
        └── evals.json        # Test cases for skill evaluation
```

## Tested skills

**teach-me** has been tested with:

- Wine & cheese pairing (non-technical learner)
- ML classification (junior data scientist)
- Modern world history (engineer filling knowledge gaps)
- Rust programming (experienced Go/C++ developer)
- Active listening (personal development / soft skill)
