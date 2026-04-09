# Website Specification

Technical specification for the interactive continuity analysis website.

## Table of Contents
1. [Architecture](#architecture)
2. [Dashboard](#dashboard)
3. [Characters / Entities View](#characters--entities-view)
4. [Timeline View](#timeline-view)
5. [World Bible / Claims Registry](#world-bible--claims-registry)
6. [Deviation Log](#deviation-log)
7. [Relationships View](#relationships-view)
8. [Source Explorer](#source-explorer)
9. [Annotation System](#annotation-system)
10. [Theming Engine](#theming-engine)
11. [Navigation & Layout](#navigation--layout)

---

## Design Philosophy

This is not a generic analytics dashboard. It's an artifact that should feel like it belongs to the
world of the source material — the kind of thing a devoted fan would make and share.

**What this means in practice:**
- **The theme shapes the layout, not just the colors.** For surreal or whimsical source material,
  the layout itself can be unconventional: tilted cards, asymmetric grids, oversized pull quotes,
  elements that break the expected box model. For serious journalism, go bold typographically —
  big stark numbers, high contrast, data journalism aesthetic.
- **Bold choices are correct. Safe choices are wrong.** When choosing between two options, the
  bolder one is almost always right. A generic dashboard with accurate data is a failed output.
  A visually striking, distinctive dashboard with accurate data is a success.
- **The test**: could someone look at the output for 5 seconds without reading any text and know
  what kind of source material it's analyzing? If yes, you've succeeded. If it could be about
  anything, you've failed.
- **Delight matters.** The deviation log should be fun to scroll through. The character profiles
  should feel like wiki pages written by someone who loved these characters. The relationship graph
  should invite exploration.
- **Less is more on data density.** Show the most interesting findings prominently rather than
  burying them in exhaustive tables. Every section should have one "headline" insight — the
  rest is detail for those who want to dig.

The only hard constraint: text must be readable, data must be accurate. Everything else — colors,
fonts, layout, whitespace, shape, personality — should be pushed as far as possible toward
capturing the soul of the source material.

---

## Architecture

The site is a single-page application using vanilla HTML/CSS/JS — no build tools, no frameworks,
no npm. Everything runs from local files.

```
site/
  index.html          # Shell + all page containers
  css/
    base.css          # Layout, typography, reset
    components.css    # Cards, badges, buttons, modals
    theme.css         # Generated per-analysis theme
  js/
    app.js            # Router, init, page switching
    data-loader.js    # Reads JSON from ../data/, makes it available
    dashboard.js      # Dashboard rendering
    characters.js     # Character profiles + filtering
    timeline.js       # Timeline visualization (canvas or SVG)
    world-bible.js    # Rules/claims registry
    deviations.js     # Deviation log + annotation interface
    relationships.js  # Force-directed graph
    source-explorer.js # Text viewer with highlights
    annotations.js    # Annotation CRUD + persistence
    search.js         # Global search across all data
    utils.js          # Shared helpers (formatting, color, etc.)
  assets/
    (generated diagrams if any)
```

### Data Loading

`data-loader.js` loads all JSON files from the `../data/` directory at startup. Since this runs
from local files, use relative paths. The data is stored in a global `window.ContinuityData` object
that all page modules can access.

```javascript
// Data loader reads these:
// ../data/characters.json (or entities.json)
// ../data/timeline.json
// ../data/world-rules.json (or claims.json)
// ../data/locations.json
// ../data/relationships.json
// ../data/plot-threads.json (or narrative-threads.json)
// ../data/tone-analysis.json
// ../data/deviations.json
// ../data/annotations.json
// ../data/metadata.json
```

Since browsers block `fetch()` on `file://` URLs, embed the JSON data directly into the HTML
as script tags:

```html
<script id="data-characters" type="application/json">
  [... characters data ...]
</script>
```

Then `data-loader.js` reads from these script tags:
```javascript
const characters = JSON.parse(document.getElementById('data-characters').textContent);
```

This avoids any CORS/file-protocol issues.

---

## Dashboard

The landing page. At a glance, the user should understand the overall health of their text.

### Layout
- **Hero section**: Large continuity score (0-100) with a color-coded ring/gauge
  - Green (80-100), Yellow (60-79), Orange (40-59), Red (0-39)
- **Category breakdown**: Row of cards, each showing score for one category
  (characters, timeline, world rules, tone, etc.)
- **Key stats bar**: Word count, character count, timeline span, file count, deviation count
- **Top deviations**: The 5 most significant deviations, each clickable to jump to detail
- **Quick actions**: Links to each main section

### Interactivity
- Clicking a category card navigates to that section
- Clicking a deviation jumps to its entry in the deviation log
- Hover on the score ring to see a breakdown tooltip

---

## Characters / Entities View

### Character List (sidebar or grid)
- Card per character with avatar placeholder (initials in a colored circle), name, role/title,
  continuity score badge
- Sort by: name, first appearance, number of deviations, continuity score
- Filter by: has deviations, appears in (file/chapter)

### Character Profile (main panel)
When a character is selected:
- **Header**: Name, aliases, score badge
- **Physical description**: Table of attributes with source references
- **Personality & Traits**: Tags with hover for source quotes
- **Timeline**: Horizontal strip showing every scene they appear in
- **Relationships**: Mini relationship graph centered on this character
- **Deviations**: List of continuity issues involving this character
- **Quotes**: Key quotes from/about this character

---

## Timeline View

The timeline's job is to be **useful and readable**, not comprehensive. The goal is story beats,
not event log completeness.

### Design principles
- **Fiction**: Show major beats — one card/row per meaningful moment. What happened? Who was
  there? Any continuity issue? Think chapter-level summary, not minute-by-minute log. 8-15 beats
  for a short story, 20-30 for a novel. No swim lanes unless the story has genuinely parallel
  plotlines that need distinguishing.
- **Non-fiction / multi-source**: Show how claims evolved over time and across sources. Each
  entry: what was said, who said it, when, and whether it contradicts an earlier source.
- If you have more events than fit cleanly, curate down to the most important ones. Fewer big
  readable beats > many cramped tiny ones.

### Layout
- Card-based vertical scroll (for most cases) OR horizontal scroll track with cards — either
  works, choose based on content density and theme.
- Each beat gets: a clear heading, brief description, source reference, and deviation flag if relevant.
- Deviation markers should be visually distinct (color badge, warning icon) but not replace the text.

### Text clipping prevention (critical)
- **Never clip or truncate labels without a hover fallback.** If text is too long, wrap it — don't
  cut it with `overflow: hidden` or `clipPath`.
- Card-based layouts naturally handle wrapping. If using SVG, use `foreignObject` for text.
- Minimum height per event: enough to show the full heading + one line of description without scrolling.
- Test mentally: can you read every event label without hovering? If not, enlarge or reduce event count.

### Controls
- Filter by character, event type, or deviation status
- Click event for detail popup (full description, source reference, related deviations)

---

## World Bible / Claims Registry

### Organization
- Categorized by domain (magic, technology, geography, politics, economics, etc. for fiction;
  topics/themes for non-fiction)
- Each entry shows:
  - The rule/claim as stated
  - Where it's established (source reference)
  - Every subsequent reference to it
  - Whether it's ever contradicted
  - Continuity score

### Interactivity
- Expandable entries
- Click source references to jump to Source Explorer
- Filter by category, score, has-deviations

---

## Deviation Log

This is the most interactive page — it's where the user does their annotation work.

### List View
- Sortable table/cards: severity, category, location, status
- Color-coded severity badges
- Status indicators (unreviewed, accepted, explained, dismissed, flagged)
- Bulk actions: select multiple, mark all as reviewed

### Detail View (expanded or modal)
- **Title**: What the deviation is
- **Severity**: Score with color badge
- **Description**: Full explanation
- **Evidence**: Side-by-side quotes from the conflicting instances
  - First instance: file, location, quoted text
  - Conflicting instance: file, location, quoted text
- **Possible explanations**: System-generated theories
- **Annotation tools**: (see Annotation System below)

### Filters
- By severity range (slider)
- By category (character, timeline, world, tone, etc.)
- By status (unreviewed, accepted, explained, dismissed, flagged)
- By file/chapter
- By character/entity involved
- Text search

---

## Relationships View

### Force-Directed Graph
- Nodes = characters/entities
- Edges = relationships
- Node size proportional to importance (scene count or mention frequency)
- Edge thickness proportional to interaction frequency
- **Edge labels**: every edge gets a short (1-2 word) label describing the relationship type —
  "ally", "rival", "mentor", "family", "enemy", "colleague", "loves", "suspects", etc.
  Labels appear on the edge line itself (centered, small font, slightly offset). These make the
  graph immediately readable without clicking. Use dotted lines for uncertain/antagonistic
  relationships, solid for confirmed/positive ones. Use the body serif font for labels (not
  monospace/typewriter) — it reads more naturally and matches the rest of the typographic system.
- **Hover on node**: highlight all connected edges, dim unconnected ones
- **Click node**: enter focus mode — show ONLY that character and their direct connections.
  This is critical for dense graphs with many characters. Include a "Show all" button to return.
- Click edge: show all interactions between those two characters

### Controls
- Drag nodes to rearrange
- Zoom and pan
- Filter by relationship type
- Toggle character groups (if the text has factions/families/organizations)
- **Focus mode** (see above) — the most important UX for large casts

### Implementation
- Render with SVG for crisp lines and text. **Never use canvas for the graph** — canvas scales
  poorly on high-DPI displays and produces blurry text and edges. SVG stays sharp at any zoom.
- Use a force-directed layout: repulsion between all nodes, attraction along edges, with collision
  detection. Run at least 300 iterations before first render.
- **Collision detection**: enforce minimum distance of 3× node radius between node centers.
  Without this, nodes pile up in the center and the graph becomes unreadable.
- Labels should be drawn outside the node circle (below or to the right), in the SVG's
  coordinate space. Never use HTML overlaid on canvas — it won't align after zoom/pan.
- **Zoom to fit**: On load, calculate the bounding box of all nodes and scale/translate the SVG
  so everything is visible. The user can then zoom in.
- For large casts (10+ characters): default to showing only the top 8-10 most connected nodes,
  with a button to reveal all. Or use focus mode as the primary UX.

---

## Source Explorer

### Layout
- Paginated text view (chapter/section at a time)
- Navigation sidebar listing all files/chapters
- Highlighted passages with color coding:
  - Character mentions (subtle underline, color per character)
  - Deviation-relevant passages (yellow highlight with warning icon)
  - Timeline markers (blue accent)
  - World rule references (green accent)

### Interactivity
- Click any highlight to see a popup with context (which character, which deviation, etc.)
- Jump-to from any other view: "See in context" links
- Toggle highlight types on/off
- Search within text

---

## Annotation System

### Per-Deviation Annotations

Each deviation in the log has an annotation panel:

```
[Accept] [Explain] [Dismiss] [Flag for Review]

[ Text input for notes ]

[Save Annotation]
```

**Statuses:**
- **Unreviewed** (default): No action taken
- **Accepted**: User confirms this is a real continuity error
- **Explained**: User provides an explanation (retcon, intentional choice, etc.)
- **Dismissed**: User says this isn't actually an inconsistency
- **Flagged**: User wants to come back to this later

### Persistence

Annotations save to `annotations.json` in the data directory. Two persistence mechanisms:

1. **localStorage**: Annotations auto-save as the user works. This is the primary method.
2. **Export/Import**: A button in the nav bar lets the user:
   - **Export**: Download `annotations.json` (saves to Downloads)
   - **Import**: Upload a previously exported `annotations.json`
   - **Save to project**: If the user opened the site from a local project, they can manually
     copy the exported JSON back to the data directory

### Annotation Data
```javascript
{
  deviation_id: "dev_001",
  status: "explained",        // unreviewed | accepted | explained | dismissed | flagged
  note: "User's explanation",
  timestamp: "ISO-8601"
}
```

On save, the annotation UI updates the status badge on the deviation immediately.

---

## Theming Engine

### Auto-Detection

Analyze the text for these cues:
- **Genre keywords**: horror → dark; romance → warm; sci-fi → cool/neon; fantasy → earth/gold
- **Setting era**: medieval → serif + parchment; modern → clean sans-serif; futuristic → monospace + glow
- **Mood words**: aggregate emotional valence of descriptive language
- **Time of day**: if the text is predominantly set at night → darker palette

### Going Beyond Colors

A great theme does more than change the color palette — it changes the personality of the interface.
For each content type, consider whether these elements should be modified:

- **Typography**: font pairing, size hierarchy, letter-spacing, whether headings feel authoritative
  or playful
- **Layout rhythm**: strictly grid-aligned (serious) vs. slightly irregular/asymmetric (whimsical)
- **Card/component style**: sharp corners + high contrast (modern/noir) vs. rounded + soft (cozy/
  literary) vs. ornate borders (fantasy/Victorian)
- **Visual motifs**: use the content to inspire decorative elements. Playing cards for Wonderland,
  circuit board traces for sci-fi, ink blots for horror, newsprint column rules for journalism.
- **Data visualization style**: choose chart types that fit the mood. Whimsical content → bubble
  charts and radial diagrams. Journalism → bar charts and sankey diagrams. Fantasy → radial/
  circular layouts that feel like maps.

The goal is that someone who's read the source material opens the output and immediately recognizes
the sensibility — it should feel *right* for that world.

### Theme CSS Variables

`theme.css` sets CSS custom properties that `base.css` and `components.css` consume:

```css
:root {
  --color-bg: #1a1a2e;
  --color-bg-secondary: #16213e;
  --color-text: #e0e0e0;
  --color-text-muted: #a0a0a0;
  --color-accent: #e94560;
  --color-accent-secondary: #0f3460;
  --color-success: #4ecca3;
  --color-warning: #f9a825;
  --color-danger: #e94560;
  --color-info: #00b4d8;
  --font-heading: 'Georgia', serif;
  --font-body: 'system-ui', sans-serif;
  --font-mono: 'Courier New', monospace;
  --border-radius: 8px;
  --shadow: 0 2px 8px rgba(0,0,0,0.3);
}
```

### Dark Mode

Include a toggle that swaps between the themed palette and a high-contrast dark mode.
Store preference in localStorage.

---

## Navigation & Layout

### Shell
- **Sidebar** (collapsible): Navigation links to each view, with icons and active state
- **Top bar**: Title of the analyzed work, overall score badge, search bar, dark mode toggle,
  export button
- **Main content**: Fills remaining space, scrollable

### Responsive
- Sidebar collapses to hamburger menu below 768px
- Cards stack vertically on mobile
- Timeline switches to vertical layout on narrow screens
- Force graph gets a simpler layout on mobile

### Keyboard Navigation
- Arrow keys for prev/next in lists
- Escape to close modals/popups
- `/` to focus search
- `1-7` to switch between main views
