# Analysis Dimensions

This document details every dimension of continuity to track, how to extract it, and what constitutes a deviation.

## Table of Contents
1. [Fiction Dimensions](#fiction-dimensions)
2. [Non-Fiction Dimensions](#non-fiction-dimensions)
3. [Universal Dimensions](#universal-dimensions)
4. [Data Schemas](#data-schemas)

---

## Fiction Dimensions

### Characters

**What to extract per character:**
- Full name and all aliases/nicknames/titles (track changes over time)
- Physical description: height, build, hair color, eye color, distinguishing features, age
- Personality traits: demonstrated through action, not just described
- Skills, abilities, powers (with any stated limitations)
- Backstory elements: origin, history, formative events
- Speech patterns: vocabulary level, catchphrases, dialect, verbal tics
- Relationships: to every other character, with nature and evolution
- Arc: how they change over the course of the narrative
- Scene log: every scene they appear in, with what they do/say/learn

**Deviation signals:**
- Physical description changes without in-narrative explanation
- Personality inconsistency (shy character suddenly bold without development)
- Knowledge the character shouldn't have (or forgetting what they should know)
- Ability changes (suddenly can/can't do something previously established)
- Relationship continuity (enemies suddenly friendly without reconciliation scene)
- Speech pattern shifts (formal character becoming casual without reason)

### Timeline

**What to extract:**
- Explicit dates and times mentioned
- Relative time markers ("three days later", "the following spring")
- Duration of events ("the battle lasted two hours")
- Character ages at specific points
- Seasonal/weather references that imply time of year
- Day/night cycle references
- Travel durations between locations

**Deviation signals:**
- Dates that don't add up (Monday followed by "two days later, on Wednesday")
- Seasons that shift impossibly fast
- Characters aging inconsistently
- Travel times that contradict established distances
- Events that happen simultaneously but reference different times of day
- "Three months later" that only accounts for one month of events

### World Rules

**What to extract:**
- Magic systems: what's possible, what's not, costs/limitations
- Technology: what exists, what doesn't, capability levels
- Physics: anything non-standard about how the physical world works
- Social structures: government, class system, customs, laws
- Geography: maps, distances, terrain, climate
- Economics: currency, trade, wealth distribution
- History: past events that shape the present world

**Deviation signals:**
- Magic/tech doing something previously stated as impossible
- Characters violating social rules without consequence when consequences were established
- Geography shifting (a city that was north is now east)
- Historical events being described differently in different places
- Rules applied inconsistently (magic costs energy in chapter 3 but is free in chapter 12)

### Locations

**What to extract:**
- Name, description, notable features
- Relative position to other locations
- Travel routes and times between locations
- Interior layout (for buildings/spaces described in detail)
- Atmosphere, sensory details
- Who lives/works there
- What events happen there

**Deviation signals:**
- Physical description changes (a room gains or loses windows)
- Relative positions shifting
- Travel times that vary without explanation
- Features appearing or disappearing

### Objects & Artifacts

**What to extract:**
- Name, description, appearance
- Current location/possessor (track transfers)
- Capabilities, limitations
- Origin/history
- Significance to plot or characters

**Deviation signals:**
- Object in two places at once
- Capabilities changing
- Object appearing after being destroyed
- Description changes

### Plot Threads

**What to extract:**
- Setup: where a thread is introduced
- Development: how it progresses
- Payoff/resolution: where it concludes
- Connected characters and locations
- Foreshadowing elements

**Deviation signals:**
- Threads that are set up but never resolved (dangling threads)
- Resolutions that contradict the setup
- Characters forgetting about active plot threads they're involved in
- Foreshadowing that points to something that never happens

---

## Non-Fiction Dimensions

### Claims & Facts

**What to extract:**
- Each factual assertion made
- Evidence or source cited (if any)
- Confidence level implied by the author's language
- Context in which the claim is made

**Deviation signals:**
- Contradictory claims within the same work or across works
- Claims that contradict cited sources
- Statistics that don't add up
- Claims stated as fact in one place, hedged in another

### Entities (People, Orgs, Places)

**What to extract:**
- How each entity is described/characterized
- Role or function in the narrative
- Attributes stated (title, location, size, etc.)
- Relationships to other entities

**Deviation signals:**
- Title/role changes without explanation
- Contradictory characterizations
- Attributes that shift

### Terminology

**What to extract:**
- Key terms and how they're defined
- First usage and context
- Subsequent usages

**Deviation signals:**
- Terms used with different meanings in different places
- Definitions that evolve without acknowledgment
- Inconsistent capitalization/formatting of terms (when it implies different meaning)

### Framing & Perspective

**What to extract:**
- How topics are framed (positive, negative, neutral)
- Whose perspective is centered
- What's emphasized vs. downplayed
- Rhetorical devices used

**Deviation signals:**
- Same event framed contradictorily in different pieces
- Perspective shifts without acknowledgment
- Tone shifts that suggest different authorial intent

---

## Universal Dimensions

These apply to both fiction and non-fiction.

### Tone & Voice

**What to extract:**
- Overall narrative voice (formal, casual, lyrical, terse, etc.)
- Sentence structure patterns
- Vocabulary level and register
- Humor style (if any)
- Emotional register

**Deviation signals:**
- Sudden shifts in formality
- Vocabulary level jumping (academic prose suddenly becoming colloquial)
- Humor style changes
- Prose rhythm changes (short punchy sentences becoming long flowing ones)

### Structural Consistency

- Formatting conventions (how chapters/sections are structured)
- Naming conventions
- Narrative frame consistency
- Point of view consistency

---

## Data Schemas

### characters.json
```json
[
  {
    "id": "char_001",
    "name": "Character Name",
    "aliases": ["Nick", "The Shadow"],
    "physical": {
      "description": "Tall, dark hair, green eyes",
      "details": [
        {"attribute": "hair_color", "value": "dark brown", "source": "ch1:p3", "quote": "..."}
      ]
    },
    "personality": ["brave", "impulsive", "loyal"],
    "abilities": [
      {"ability": "swordfighting", "level": "expert", "source": "ch2:p1", "limitations": "..."}
    ],
    "first_appearance": {"file": "chapter1.txt", "location": "paragraph 5"},
    "scenes": [
      {"file": "chapter1.txt", "location": "p5-p12", "summary": "Introduced at the tavern"}
    ],
    "relationships": [
      {"target": "char_002", "nature": "rival", "evolution": [...]}
    ],
    "arc_notes": "Starts as a loner, learns to trust",
    "continuity_score": 92,
    "deviations": ["dev_003", "dev_007"]
  }
]
```

### timeline.json
```json
{
  "events": [
    {
      "id": "evt_001",
      "description": "The battle of Northmere",
      "time_absolute": "Year 342, Spring",
      "time_relative": "Three days after the council",
      "duration": "Two hours",
      "characters": ["char_001", "char_003"],
      "location": "loc_005",
      "source": {"file": "chapter5.txt", "location": "p1-p15"},
      "deviations": []
    }
  ],
  "time_markers": [
    {"source": "ch3:p7", "text": "three weeks had passed", "anchored_to": "evt_001"}
  ]
}
```

### deviations.json
```json
[
  {
    "id": "dev_001",
    "category": "character",
    "severity": 65,
    "title": "Marcus's eye color changes",
    "description": "Marcus is described as having blue eyes in Chapter 1 but brown eyes in Chapter 8",
    "first_instance": {"file": "chapter1.txt", "location": "p3", "quote": "his piercing blue eyes"},
    "conflicting_instance": {"file": "chapter8.txt", "location": "p22", "quote": "she looked into his warm brown eyes"},
    "related_entities": ["char_001"],
    "possible_explanations": [
      "Could be a deliberate choice (e.g., magical transformation)",
      "Likely a continuity error — no in-text explanation"
    ],
    "annotation": null
  }
]
```

### annotations.json
```json
{
  "version": 1,
  "annotations": [
    {
      "deviation_id": "dev_001",
      "status": "explained",
      "note": "This is actually addressed in the companion short story — Marcus wears colored contacts",
      "timestamp": "2024-01-15T10:30:00Z"
    }
  ]
}
```
