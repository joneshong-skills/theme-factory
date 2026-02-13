[English](README.md) | [繁體中文](README.zh.md)

# theme-factory

A Claude Code skill that provides a curated collection of 10 professional color and typography themes for styling any artifact -- slide decks, documents, reports, HTML landing pages, and more. You can also generate custom themes on-the-fly.

## What It Does

1. Displays the `assets/theme-showcase.pdf` so the user can visually browse all 10 pre-set themes
2. Lets the user pick a theme (or request a custom one)
3. Reads the theme specification from `references/` to get exact hex colors and font pairings
4. Applies the selected theme consistently across the target artifact

## Themes Available

| # | Theme | Vibe |
|---|-------|------|
| 1 | Ocean Depths | Professional, calming maritime |
| 2 | Sunset Boulevard | Warm, vibrant sunset colors |
| 3 | Forest Canopy | Natural, grounded earth tones |
| 4 | Modern Minimalist | Clean, contemporary grayscale |
| 5 | Golden Hour | Rich, warm autumnal palette |
| 6 | Arctic Frost | Cool, crisp winter-inspired |
| 7 | Desert Rose | Soft, sophisticated dusty tones |
| 8 | Tech Innovation | Bold, modern tech aesthetic |
| 9 | Botanical Garden | Fresh, organic garden colors |
| 10 | Midnight Galaxy | Dramatic, cosmic deep tones |

## Prerequisites

- Claude Code with the skill installed at `~/.claude/skills/theme-factory/`

## Installation

```bash
git clone https://github.com/joneshong-skills/theme-factory.git ~/.claude/skills/theme-factory
```

## Usage

Once installed, ask Claude to apply a theme:

- *"Apply the Ocean Depths theme to my slide deck"*
- *"Show me the available themes"*
- *"Create a custom warm pastel theme for my landing page"*
- *"Use the Tech Innovation theme on this report"*

## Project Structure

```
theme-factory/
├── SKILL.md                        # Skill definition and workflow
├── README.md                       # This file
├── README.zh.md                    # Traditional Chinese README
├── LICENSE.txt                     # Apache 2.0 license
├── assets/
│   └── theme-showcase.pdf          # Visual showcase of all 10 themes
├── references/
│   ├── arctic-frost.md             # Theme spec: Arctic Frost
│   ├── botanical-garden.md         # Theme spec: Botanical Garden
│   ├── desert-rose.md              # Theme spec: Desert Rose
│   ├── forest-canopy.md            # Theme spec: Forest Canopy
│   ├── golden-hour.md              # Theme spec: Golden Hour
│   ├── midnight-galaxy.md          # Theme spec: Midnight Galaxy
│   ├── modern-minimalist.md        # Theme spec: Modern Minimalist
│   ├── ocean-depths.md             # Theme spec: Ocean Depths
│   ├── sunset-boulevard.md         # Theme spec: Sunset Boulevard
│   └── tech-innovation.md          # Theme spec: Tech Innovation
└── scripts/                        # (reserved for future automation)
```

## License

Apache 2.0 -- see [LICENSE.txt](LICENSE.txt)
