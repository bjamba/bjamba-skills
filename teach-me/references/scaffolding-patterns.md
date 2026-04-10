# Scaffolding Patterns

Reference guide for the types of artifacts and repo structures to build based on topic and learner profile. Read this when you need inspiration for what to build during Setup Mode.

The default artifact format is **interactive HTML** for almost everything. Markdown is only for README, TUTOR_CONTEXT, and the learner's own journal/notes. See the main SKILL.md for the full rationale.

## Table of Contents
1. [Knowledge/Memorization Topics](#knowledgememorization-topics)
2. [Practical/Hands-On Skills](#practicalhands-on-skills)
3. [Technical/Engineering Topics](#technicalengineering-topics)
4. [Creative Skills: Drawing and Visual Art](#creative-skills-drawing-and-visual-art)
5. [Creative Skills: Animation](#creative-skills-animation)
6. [Music and Ear Training](#music-and-ear-training)
7. [Tactile Crafts: Origami and Paper Arts](#tactile-crafts-origami-and-paper-arts)
8. [Cooking and Cuisine](#cooking-and-cuisine)
9. [Tabletop RPG and Games](#tabletop-rpg-and-games)
10. [Language Learning](#language-learning)
11. [Exam Prep / Certification](#exam-prep--certification)
12. [Current Events / Awareness Topics](#current-events--awareness-topics)

---

## Knowledge/Memorization Topics
**Examples:** wine pairing, beer styles, art history, anatomy, geography, music theory

**Best artifacts:**
- Flashcard app with spaced repetition (HTML, localStorage tracking)
- Visual reference sheets (HTML with images — CC-licensed or original)
- Self-quiz tools with immediate feedback
- Categorization exercises (drag-and-drop using Sortable.js)
- Tasting/observation worksheets (HTML forms they fill in)

**Repo pattern:**
```
topic/
├── dashboard.html
├── credits.html
├── tools/
│   ├── flashcards.html       # Spaced repetition flashcard app
│   └── quiz.html             # Self-assessment quiz
├── module-01/
│   ├── lesson-01.html        # Lesson content as styled HTML
│   ├── reference-sheet.html  # Visual reference card
│   └── exercises/
│       └── exercise-01.html  # Interactive exercise
```

---

## Practical/Hands-On Skills
**Examples:** cooking techniques, woodworking, gardening, photography, home repair

**Best artifacts:**
- Step-by-step HTML guides with embedded checklists
- Technique reference cards (HTML with CC-licensed images)
- Practice logs (HTML form that saves to localStorage)
- Skill progression trackers (HTML)
- Project plans with materials lists (HTML)

**Repo pattern:**
```
topic/
├── dashboard.html
├── tools/
│   └── practice-log.html    # Track practice sessions
├── module-01/
│   ├── lesson-01.html        # Technique explanation with visuals
│   ├── project-01.html       # Hands-on project guide
│   └── resources/
│       └── materials-list.html
```

---

## Technical/Engineering Topics
**Examples:** Python, data science, Kubernetes, system design, machine learning, web development

**Best artifacts for data/analysis topics (Python, ML, data science):**
- **Jupyter notebooks (.ipynb)** as the primary lesson format — combine narrative, code, and visualizations
- Interactive HTML reference cards and cheat sheets
- HTML quiz tools for concept review
- Real datasets to explore
- Project skeletons with tests

**Best artifacts for systems/language topics (Rust, Go, Kubernetes, infrastructure):**
- In-page CodeMirror editor (HTML) + actual runnable source files side by side
- HTML comparison tools (e.g., Go-to-Rust cheat sheet)
- CLI tools and scripts
- Configuration files they can experiment with
- Test suites that validate their solutions

**Repo pattern (data science):**
```
topic/
├── dashboard.html
├── tools/
│   ├── concept-quiz.html       # Interactive self-assessment
│   └── cheatsheet.html         # Quick reference
├── module-01/
│   ├── lesson-01.ipynb         # Jupyter notebook lesson
│   ├── exercises/
│   │   ├── exercise-01.ipynb   # Notebook exercise
│   │   └── exercise-01-solution.ipynb
│   └── resources/
│       └── dataset.csv
```

**Repo pattern (systems/language):**
```
topic/
├── dashboard.html
├── tools/
│   └── reference.html          # e.g., language comparison card
├── module-01/
│   ├── lesson-01.html          # Lesson with in-page CodeMirror editor
│   ├── exercises/
│   │   ├── exercise-01.html    # Interactive editor + instructions
│   │   ├── exercise-01.py      # Runnable starter file
│   │   └── exercise-01-solution.py
│   └── resources/
│       └── cheatsheet.html
```

---

## Creative Skills: Drawing and Visual Art
**Examples:** sketching, illustration, watercolor, life drawing, character design

**The core experience:** making marks, observing reference, comparing your work.

**Best artifacts:**
- **Drawing canvas tool** — p5.js canvas on the same page as the reference image. Learner can see the reference at 50% opacity, draw over or beside it, and toggle between view and draw mode. Include a "reveal" button to compare side by side.
- Reference galleries (HTML with CC-licensed images, full attribution)
- Observation exercises with guided prompts on the same page
- Self-critique worksheets (HTML with structured reflection fields)
- Prompt generators (HTML tool that gives creative prompts with reference images)

**Key principle:** The reference image and the drawing canvas must be on the same page. Never make the learner switch between files to compare.

**Repo pattern:**
```
topic/
├── dashboard.html
├── credits.html               # Required — reference images need attribution
├── tools/
│   └── prompt-generator.html # Random creative prompts with reference images
├── module-01/
│   ├── lesson-01.html         # Lesson with technique explanation
│   └── exercises/
│       └── exercise-01.html   # p5.js canvas + reference image, side by side
├── portfolio/
│   └── README.md              # How to save and organize their work
```

**p5.js drawing canvas skeleton:**
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.9.0/p5.min.js"></script>
<script>
let drawing;
function setup() {
  let canvas = createCanvas(600, 400);
  canvas.parent('canvas-container');
  background(255);
}
function draw() {
  if (mouseIsPressed) {
    strokeWeight(brushSize);
    stroke(brushColor);
    line(pmouseX, pmouseY, mouseX, mouseY);
  }
}
</script>
```

---

## Creative Skills: Animation
**Examples:** frame-by-frame animation, motion graphics, character animation, GIF creation

**The core experience:** creating movement by sequencing frames.

**Best artifacts:**
- **In-browser animation studio** — p5.js with frame management, onion skinning, playback controls, and export. Allow drawing frame by frame with a timeline strip at the bottom showing thumbnails.
- Timing and spacing exercises (animate a bouncing ball, show stretch/squash)
- Reference motion analysis tools (side-by-side video + frame breakdown — YouTube nocookie embeds for reference clips if licensed)
- Principle flashcards (12 principles of animation)

**Animation studio essentials:**
- Frame list stored in an array of pixel arrays
- Onion skin toggle (previous frame at 30% opacity)
- Play/pause at adjustable FPS
- Clear frame, duplicate frame, add frame, delete frame
- Export as downloadable PNG sequence or animated GIF (using gif.js via CDN)

**Repo pattern:**
```
topic/
├── dashboard.html
├── tools/
│   └── animation-studio.html  # Full p5.js animation studio
├── module-01/
│   ├── lesson-01.html          # Principles: squash and stretch, timing, etc.
│   └── exercises/
│       └── exercise-01.html    # Guided animation exercise with built-in studio
```

---

## Music and Ear Training
**Examples:** piano, music theory, ear training, guitar, music composition, rhythm

**The core experience:** hearing and playing notes.

**Best artifacts:**
- **Virtual keyboard** — Tone.js synthesizer with a clickable HTML keyboard (also playable with computer keyboard keys). Show note names, highlight intervals, display what's playing.
- **Ear training quiz** — plays a note or interval with Tone.js, learner identifies it, immediate feedback
- **Rhythm trainer** — metronome with Tone.js, tap-along exercise that measures timing accuracy
- **Scale/chord explorer** — shows a scale visually on the keyboard, plays it when clicked
- Music notation reference (HTML, SVG-based staff if possible)
- Interval and chord flashcards

**Key principle:** If the learner is being asked to identify something by ear, they must be able to hear it and interact with it on the same page. Never separate the listening from the exercise.

**Tone.js virtual keyboard skeleton:**
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/tone/14.8.49/Tone.js"></script>
<script>
const synth = new Tone.Synth().toDestination();
async function playNote(note) {
  await Tone.start(); // required for browser audio policy
  synth.triggerAttackRelease(note, '8n');
}
</script>
<!-- Map computer keyboard keys to notes in keydown handler -->
```

**Repo pattern:**
```
topic/
├── dashboard.html
├── tools/
│   ├── keyboard.html          # Full virtual keyboard with Tone.js
│   ├── ear-training.html      # Listen and identify intervals/chords
│   └── flashcards.html        # Music theory flashcards
├── module-01/
│   ├── lesson-01.html         # Lesson + embedded mini-keyboard to try examples
│   └── exercises/
│       └── exercise-01.html   # Ear training exercise with built-in audio
```

---

## Tactile Crafts: Origami and Paper Arts
**Examples:** origami, kirigami, paper folding, paper cutting

**The core experience:** folding paper step by step, seeing each transformation.

**Best artifacts:**
- **Virtual fold-along** — SVG or CSS-based paper representation that animates each fold step using Anime.js. Show the paper flat, then animate the fold with a 3D CSS transform or SVG path transition. Each step has a "next" button and a diagram alongside instructions.
- Step diagram gallery (original SVG diagrams or CC-licensed images with attribution)
- Printable template PDFs linked (don't embed unless CC-licensed)
- Practice checklist with difficulty ratings

**Fold animation approach:**
Use CSS 3D transforms (`rotateX`, `rotateY`) with a `perspective` wrapper to simulate paper folding. Anime.js controls the transition. For complex origami, break the shape into panels and fold each independently. Alternatively, use SVG `<polygon>` elements that morph between states.

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js"></script>
<script>
function animateFold(step) {
  anime({
    targets: '#panel-top',
    rotateX: [0, -180],
    duration: 800,
    easing: 'easeInOutQuad'
  });
}
</script>
```

**Repo pattern:**
```
topic/
├── dashboard.html
├── credits.html               # Required if any reference images are used
├── tools/
│   └── fold-explorer.html     # Browse and practice different folds
├── module-01/
│   ├── lesson-01.html         # Introduction to fold types (valley, mountain, etc.)
│   └── exercises/
│       └── crane-step-by-step.html  # Animated fold tutorial, one step at a time
```

---

## Cooking and Cuisine
**Examples:** Hungarian cooking, French pastry, Japanese cuisine, bread baking, knife skills

**The core experience:** following a recipe, understanding technique, building a repertoire.

**Best artifacts:**
- **Interactive recipe book** — Swiper.js carousel of recipe cards with CC-licensed food photography (from Wikimedia Commons or original). Each card links to a detail page.
- **Step-by-step recipe pages** — each step is a panel with: technique note, timer button (if the step has timing), ingredient checklist. Timers live on the same page — clicking "Start timer" shows a countdown without leaving.
- **Technique reference** — HTML with illustrations/video embeds (YouTube nocookie, if the video has explicit embedding permission) showing knife cuts, pastry folds, etc.
- **Ingredient glossary** — searchable HTML with CC-licensed images of ingredients
- Practice log (HTML form tracking what they've cooked and notes)

**Key principle:** Timers belong on the recipe page. If the learner is sautéing onions for 8 minutes, the 8-minute timer is right there — not a separate app.

**Built-in timer pattern:**
```html
<button onclick="startTimer(8 * 60)">⏱ Start 8-min timer</button>
<div id="timer-display" class="timer">8:00</div>
<script>
function startTimer(seconds) {
  let remaining = seconds;
  const display = document.getElementById('timer-display');
  const interval = setInterval(() => {
    if (remaining <= 0) { clearInterval(interval); display.textContent = 'Done!'; return; }
    const m = Math.floor(remaining / 60), s = remaining % 60;
    display.textContent = `${m}:${s.toString().padStart(2,'0')}`;
    remaining--;
  }, 1000);
}
</script>
```

**Repo pattern:**
```
topic/
├── dashboard.html
├── credits.html               # Required — food images need attribution
├── tools/
│   ├── recipe-book.html       # Swiper.js recipe card browser
│   └── ingredient-glossary.html
├── module-01/
│   ├── lesson-01.html         # Technique lesson with embedded video (nocookie)
│   └── exercises/
│       └── recipe-01.html     # Full interactive recipe with built-in timers
```

---

## Tabletop RPG and Games
**Examples:** D&D, Pathfinder, Call of Cthulhu, board game design, game theory

**The core experience:** rolling dice, building a character, playing through scenarios.

**Best artifacts:**
- **Animated dice roller** — CSS 3D dice that visually spin and land on a result. Support d4, d6, d8, d10, d12, d20, d100. Add roll history and modifiers. Use Anime.js for the roll animation.
- **Fillable character sheet** — HTML form with all character fields, saves to localStorage, and exports as JSON (downloadable). Includes computed fields (e.g., ability score modifiers calculated automatically).
- **Scenario sandbox** — a simple text-based scenario generator that uses the character sheet data and a set of prompts to create encounters. Can include branching choices and outcome tracking.
- **Rules reference** — searchable HTML quick-reference for the system being learned
- **Encounter builder** — for DMs learning to run games

**Key principle:** The dice roller should feel satisfying — animate it. The character sheet should be saveable and downloadable. These are the tools the learner will actually want to use during play.

**Repo pattern:**
```
topic/
├── dashboard.html
├── tools/
│   ├── dice-roller.html       # Animated d4/d6/d8/d10/d12/d20/d100
│   ├── character-sheet.html   # Fillable, saveable, exportable
│   └── scenario-sandbox.html  # Simple scenario generator
├── module-01/
│   ├── lesson-01.html          # Core rules introduction
│   └── exercises/
│       └── first-character.html # Guided character creation with built-in sheet
```

---

## Language Learning
**Examples:** Spanish, Japanese, Mandarin, ASL basics, sign language

**Best artifacts:**
- Vocabulary flashcards (HTML, ideally with audio pronunciation via Web Speech API — no external service needed)
- Grammar reference sheets (HTML with interactive examples)
- Conversation scenario simulators (branching HTML dialogs)
- Writing/typing exercises with instant feedback
- Cultural context pages

**Web Speech API for pronunciation (no API key, built into browsers):**
```html
<button onclick="speak('hola')">🔊 Hear it</button>
<script>
function speak(text, lang = 'es-ES') {
  const u = new SpeechSynthesisUtterance(text);
  u.lang = lang;
  speechSynthesis.speak(u);
}
</script>
```

**Repo pattern:**
```
topic/
├── dashboard.html
├── tools/
│   ├── flashcards.html        # Vocabulary with audio pronunciation
│   ├── conjugation-quiz.html  # Verb practice with immediate feedback
│   └── phrase-builder.html    # Sentence construction practice
├── module-01/
│   ├── lesson-01.html          # Lesson with interactive examples
│   └── exercises/
│       ├── conversation-01.html # Branching conversation simulator
│       └── writing-01.html      # Typing exercise with feedback
```

---

## Exam Prep / Certification
**Examples:** AWS certification, bar exam, sommelier exam, SAT, medical boards

**Best artifacts:**
- Timed practice test (HTML with countdown timer on the same page)
- Weak-area tracker (HTML that identifies topics to focus on, localStorage)
- Randomized question generator (pull from a question bank stored in the HTML)
- Formula/fact sheets (HTML reference cards)
- Study domain guides (HTML, organized by exam domain)

**Key principle:** Practice tests must be timed, and the timer lives on the test page. Seeing the clock tick is part of the practice.

**Repo pattern:**
```
topic/
├── dashboard.html
├── tools/
│   ├── practice-test.html     # Timed, randomized, with score tracking
│   ├── weak-areas.html        # Track what needs more work
│   └── quick-review.html      # Rapid-fire review tool
├── domain-01/
│   ├── study-guide.html        # Domain overview
│   └── exercises/
│       └── practice-set.html   # Domain-specific practice questions
```

---

## Current Events / Awareness Topics
**Examples:** world politics, economics, industry trends, science news

**Best artifacts:**
- Framework documents for analyzing events (HTML, not markdown)
- Comparison charts and timelines (HTML with Chart.js or D3.js if data-heavy)
- Curated link lists with context annotations (HTML)
- Discussion prompts and reflection questions (HTML with localStorage journal)
- Glossaries of key terms and concepts (HTML with search)

**Repo pattern:**
```
topic/
├── dashboard.html
├── tools/
│   └── timeline.html          # Interactive timeline of events
├── module-01/
│   ├── lesson-01.html          # Background/context
│   ├── frameworks.html         # How to analyze events
│   └── exercises/
│       └── analysis-01.html    # Apply the framework to a case
├── progress/
│   └── journal.html            # Ongoing reflections, localStorage-based
```

---

## General Tips for All Artifact Types

### HTML Single-File Apps
- Inline all CSS in `<style>`, all JavaScript in `<script>`
- Use `localStorage` for persisting state between sessions
- Use CSS custom properties (`--color-primary`, `--font-body`, etc.) for a consistent visual identity across all files in the curriculum
- Make them responsive — they should work on phones and tablets too
- Import libraries from CDN so they work as `file://` pages

### Timers
Any exercise with time pressure gets a timer built directly into the exercise page. Never link to a separate timer. The pattern is always: question + timer + input + feedback on one page.

### Navigation
Every HTML file gets a `<nav>` at the top with breadcrumbs linking back to the dashboard and to sibling pages. Every file gets prev/next at the bottom. Use the same nav style across all files.

### Credits
Any external resource (image, video, audio) that's embedded needs attribution directly below it. The `credits.html` file collects all attributions in one place. If you're not sure of the license, link to the source instead of embedding.
