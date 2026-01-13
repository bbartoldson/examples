# Visual Layout Comparison (ASCII Mockups)

These ASCII diagrams show the structure of each version to help you choose without compiling.

## ORIGINAL (Current)
```
┌────────────────────────────────────────────────────┐
│ Chemistry: Reaction Cascade             Medium     │
├────────────────────────────────────────────────────┤
│                                                    │
│ [Mol-1] [Mol-2] [Mol-3] [Mol-4] [Mol-5]          │
│    \       /      |  \     /       |              │
│     [Mol-3]       |   [Mol-5]─────┤              │
│                   |                |              │
│ [Mol-6] [Mol-7] [Mol-8]           |              │
│    \       /       |               |              │
│     [Mol-8]────────┴───────────►[Output]         │
│                                                    │
└────────────────────────────────────────────────────┘

❌ Issues: Cramped, unclear flow, hard to read
```

---

## VERSION 1: Hierarchical (Top-to-Bottom)
```
┌────────────────────────────────────────────────────┐
│ Chemistry: Reaction Cascade             Medium     │
├────────────────────────────────────────────────────┤
│                  ┌─── INPUTS ────┐                │
│                                                    │
│     [Mol-1]  [Mol-2]  [Mol-4]  [Mol-6]  [Mol-7]  │
│         \      /          |         \      /       │
│          \    /           |          \    /        │
│                                                    │
│        [Mol-3]            |         [Mol-8]       │
│           \               |           /            │
│            \              |          /             │
│             \             |         /              │
│              \           /         /               │
│               \         /         /                │
│                                                    │
│                  [Mol-5]                          │
│                     |                              │
│                     |                              │
│                     ▼                              │
│                                                    │
│                 [OUTPUT]                          │
│                                                    │
└────────────────────────────────────────────────────┘

✓ Clear hierarchy, easy to follow top-to-bottom
```

---

## VERSION 2: Left-to-Right Flow (RECOMMENDED)
```
┌────────────────────────────────────────────────────┐
│ Chemistry: Reaction Cascade             Medium     │
├────────────────────────────────────────────────────┤
│                                                    │
│  [Mol-1] ──┐                                      │
│            ├──► [Mol-3] ──┐                       │
│  [Mol-2] ──┘               │                      │
│                            ├──► [Mol-5]           │
│  [Mol-4] ──────────────────┘       │              │
│                                     │              │
│                                     ├─►[OUTPUT]   │
│  [Mol-6] ──┐                        │              │
│            ├──► [Mol-8] ────────────┤              │
│  [Mol-7] ──┘       └────────────────┘              │
│                                                    │
│  Light ──────────────────────────────► Dark       │
│  (inputs)                          (output)        │
│                                                    │
└────────────────────────────────────────────────────┘

✓ Traditional flowchart, clear progression, good spacing
```

---

## VERSION 3: Grouped Reactions
```
┌────────────────────────────────────────────────────┐
│ Chemistry: Reaction Cascade             Medium     │
├────────────────────────────────────────────────────┤
│                                                    │
│  ╔═══ Stage 1 ═══╗     ╔═ Stage 2 ══╗   Final    │
│                                                    │
│  ┌── Rxn A ──┐         ┌── Rxn C ──┐             │
│  │ [M-1] ──┐ │         │            │             │
│  │         ├►[M-3]──┐  │ [M-4] ──┐  │             │
│  │ [M-2] ──┘ │      │  │         ├►[M-5]──┐      │
│  └───────────┘      │  │         │  │     │       │
│                     └──┤         │  │     │       │
│  ┌── Rxn B ──┐        └─────────┘  │     │       │
│  │ [M-6] ──┐ │                      │     │       │
│  │         ├►[M-8]───────────────────┼────┤       │
│  │ [M-7] ──┘ │  └───────────────────┘     │       │
│  └───────────┘                            │       │
│                                            ▼       │
│                                        [OUTPUT]   │
│                                                    │
└────────────────────────────────────────────────────┘

✓ Great for understanding parallel reactions, pedagogical
```

---

## VERSION 4: Modern Streamlined
```
┌────────────────────────────────────────────────────┐
│ Chemistry: Reaction Cascade             Medium     │
├────────────────────────────────────────────────────┤
│                                        🧪 (faint)  │
│  [M-1] ─●─┐          combine                      │
│           ├──► [M-3] ─●─┐                         │
│  [M-2] ─●─┘             │    combine               │
│                         ├──► [M-5] ──► [OUTPUT]  │
│  [M-4] ────────────●────┘         ▲       ▲        │
│                                   │       │        │
│                    combine        │       │        │
│  [M-6] ─●─┐                       │       │        │
│           ├──► [M-8] ─────────────┘       │        │
│  [M-7] ─●─┘      └─────────────────────────┘        │
│                                                    │
│  Shadows + merge points (●) on white background   │
│                                                    │
└────────────────────────────────────────────────────┘

✓ Clean, modern, minimal, with visual depth
```

---

## Quick Decision Guide

**Want traditional academic look?** → Version 2

**Want modern/striking design?** → Version 4

**Teaching a class?** → Version 3

**Presenting a synthesis plan?** → Version 1

**In a hurry?** → Version 2 (safest choice)

---

## Color Coding (All Versions)

- **Lightest**: Starting materials/inputs
- **Medium**: Intermediate products
- **Darkest**: Final output

This creates a visual flow showing the progression through the reaction cascade.

---

## Technical Details

| Aspect | Original | Improved |
|--------|----------|----------|
| Node spacing | 0.6 cm | 0.8-1.4 cm |
| Font size | scriptsize | footnotesize/small |
| Color range | teal!15-50 | teal!8-55 |
| Arrow style | basic | styled with modern tips |
| Background opacity | 0.08 | 0.04-0.06 |
| Node sizing | inconsistent | minimum sizes set |

---

All versions maintain the exact same information and relationships - only the visual presentation differs!
