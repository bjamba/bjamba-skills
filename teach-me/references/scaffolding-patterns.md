# Scaffolding Patterns

Reference guide for the types of artifacts and repo structures to build based on topic and learner profile. Read this when you need inspiration for what to build during Setup Mode.

## Table of Contents
1. [Knowledge/Memorization Topics](#knowledgememorization-topics)
2. [Practical/Hands-On Skills](#practicalhands-on-skills)
3. [Technical/Engineering Topics](#technicalengineering-topics)
4. [Creative Skills](#creative-skills)
5. [Current Events / Awareness Topics](#current-events--awareness-topics)
6. [Language Learning](#language-learning)
7. [Exam Prep / Certification](#exam-prep--certification)

---

## Knowledge/Memorization Topics
**Examples:** wine pairing, beer styles, art history, anatomy, geography, music theory

**Best artifacts:**
- Single-file HTML flashcard app with spaced repetition (uses localStorage to track what they know)
- Visual reference sheets (HTML with images/diagrams)
- Self-quiz tools (HTML forms that check answers and track scores)
- Categorization exercises (drag-and-drop or matching in HTML)
- Tasting/observation worksheets (markdown templates they fill in)

**Repo pattern:**
```
topic/
├── tools/
│   ├── flashcards.html      # Spaced repetition flashcard app
│   └── quiz.html            # Self-assessment quiz
├── module-01/
│   ├── lesson-01.md
│   ├── reference-sheet.html  # Visual reference
│   └── exercises/
│       └── worksheet.md
```

---

## Practical/Hands-On Skills
**Examples:** cooking techniques, woodworking, gardening, photography, home repair

**Best artifacts:**
- Step-by-step guides with checklists (markdown)
- Project plans with materials lists
- Technique reference cards (HTML with embedded images/diagrams)
- Practice logs (markdown templates)
- Skill progression trackers (HTML)

**Repo pattern:**
```
topic/
├── tools/
│   └── practice-log.html    # Track practice sessions
├── module-01/
│   ├── lesson-01.md          # Technique explanation
│   ├── project-01.md         # Hands-on project
│   └── resources/
│       ├── materials-list.md
│       └── safety-notes.md
├── progress/
│   └── practice-log.md
```

---

## Technical/Engineering Topics
**Examples:** Python, data science, Kubernetes, system design, machine learning, web development

**Best artifacts for data/analysis topics (Python, ML, data science):**
- **Jupyter notebooks (.ipynb) as the primary lesson format** — they combine narrative, code, and visualizations naturally. Much more engaging than raw .py files for learning.
- Interactive HTML reference cards and cheat sheets
- HTML quiz tools for concept review
- Real datasets to explore
- Project skeletons with tests

**Best artifacts for systems/language topics (Rust, Go, Kubernetes, infrastructure):**
- Working code projects with exercises (actual runnable code in the target language)
- HTML comparison tools (e.g., Go-to-Rust cheat sheet)
- CLI tools and scripts
- Configuration files they can experiment with
- Test suites that validate their solutions

**Repo pattern (data science):**
```
topic/
├── dashboard.html              # Progress tracker
├── tools/
│   ├── concept-quiz.html       # Interactive self-assessment
│   └── cheatsheet.html         # Quick reference
├── module-01/
│   ├── lesson-01.ipynb         # Jupyter notebook lesson
│   ├── exercises/
│   │   ├── exercise-01.ipynb   # Notebook exercise
│   │   └── ...
│   └── resources/
│       └── dataset.csv
├── projects/
│   └── capstone/
│       ├── README.md
│       └── starter.ipynb
```

**Repo pattern (systems/language):**
```
topic/
├── dashboard.html
├── tools/
│   └── comparison-reference.html  # e.g., Go-vs-Rust side-by-side
├── module-01/
│   ├── lesson-01.html          # Lesson as styled HTML
│   ├── exercises/
│   │   ├── exercise-01/
│   │   │   ├── README.md
│   │   │   ├── starter.rs
│   │   │   ├── solution.rs
│   │   │   └── test.rs
│   │   └── ...
│   └── resources/
│       └── cheatsheet.html
├── projects/
│   └── project-01/
│       ├── Cargo.toml
│       └── src/
```

---

## Creative Skills
**Examples:** writing, drawing, music composition, design, storytelling

**Best artifacts:**
- Prompt generators (HTML tool that gives creative prompts)
- Templates and frameworks (markdown)
- Example galleries with analysis (HTML)
- Critique worksheets (structured markdown for self-review)
- Portfolio structure (for collecting their work)

**Repo pattern:**
```
topic/
├── tools/
│   ├── prompt-generator.html  # Random creative prompts
│   └── self-critique.html     # Guided self-review tool
├── module-01/
│   ├── lesson-01.md
│   └── exercises/
│       ├── prompt-01.md
│       └── examples/          # Reference works to study
├── portfolio/                  # Their creative output
│   └── README.md              # How to organize their work
```

---

## Current Events / Awareness Topics
**Examples:** world politics, economics, industry trends, science news

**Best artifacts:**
- Curated reading lists with context (markdown)
- Framework documents for analyzing events (markdown)
- Comparison charts and timelines (HTML)
- Discussion prompts and reflection questions
- Glossaries of key terms and concepts

**Repo pattern:**
```
topic/
├── frameworks/
│   ├── how-to-read-news.md
│   └── analysis-template.md
├── module-01/
│   ├── lesson-01.md           # Background/context
│   ├── reading-list.md        # Curated sources
│   └── exercises/
│       └── analysis-01.md     # Apply the framework
├── progress/
│   └── journal.md             # Ongoing reflections
```

---

## Language Learning
**Examples:** Spanish, Japanese, Mandarin, ASL basics, programming languages

**Best artifacts:**
- Vocabulary flashcards with audio pronunciation guides (HTML)
- Grammar reference sheets (HTML with examples)
- Conversation scenario scripts (markdown)
- Writing exercises with space for their attempts
- Cultural context notes

**Repo pattern:**
```
topic/
├── tools/
│   ├── flashcards.html        # Vocabulary flashcards
│   ├── conjugation-quiz.html  # Verb practice
│   └── phrase-builder.html    # Sentence construction practice
├── module-01/
│   ├── lesson-01.md
│   ├── vocabulary.md          # Word list for this module
│   └── exercises/
│       ├── conversation-01.md # Practice dialogue
│       └── writing-01.md      # Writing prompt
```

---

## Exam Prep / Certification
**Examples:** AWS certification, bar exam, sommelier exam, SAT, medical boards

**Best artifacts:**
- Practice test generators (HTML with randomized questions)
- Study guides organized by exam domain (markdown)
- Weak-area trackers (HTML that identifies what to focus on)
- Timed practice tools (HTML with countdown timer)
- Formula/fact sheets (markdown or HTML reference cards)

**Repo pattern:**
```
topic/
├── tools/
│   ├── practice-test.html     # Timed practice tests
│   ├── weak-areas.html        # Track what needs more work
│   └── quick-review.html      # Rapid-fire review tool
├── domain-01/
│   ├── study-guide.md
│   ├── key-concepts.md
│   └── practice-questions/
│       ├── set-01.md
│       └── ...
├── progress/
│   └── test-scores.md         # Track practice test results
```

---

## General Tips for Artifact Creation

### HTML Single-File Apps
When building HTML tools, make them fully self-contained:
- Inline all CSS in a `<style>` tag
- Inline all JavaScript in a `<script>` tag
- Use `localStorage` for persisting state between sessions
- Use modern CSS (grid, flexbox, custom properties) for clean layouts
- Make them responsive (they should work on phones too)
- Include a brief "how to use" section at the top of the page
- Use a clean, modern design — the learner should enjoy using these tools

### Progress Visualization
Consider adding a progress dashboard as an HTML file at the repo root that reads from curriculum.json (or has its own localStorage state) and shows:
- Modules completed vs remaining
- Current streak
- Time spent
- Weak areas (if applicable)
