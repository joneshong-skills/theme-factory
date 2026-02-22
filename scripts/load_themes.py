#!/usr/bin/env python3
"""Load and list available themes from the theme catalog.

Usage:
  python3 load_themes.py --list           # List all themes
  python3 load_themes.py --show THEME     # Show theme details
  python3 load_themes.py --css THEME      # Output CSS variables for theme
"""

import argparse
import sys

THEMES = {
    "anthropic": {
        "primary": "#191918",
        "accent": "#DA7756",
        "bg": "#E8E1D5",
        "font": "Copernicus",
        "description": "Anthropic brand — warm parchment with sienna accents",
    },
    "ocean": {
        "primary": "#1a365d",
        "accent": "#3182ce",
        "bg": "#ebf8ff",
        "font": "Inter",
        "description": "Deep navy and sky blue on a cool light background",
    },
    "forest": {
        "primary": "#1a4731",
        "accent": "#38a169",
        "bg": "#f0fff4",
        "font": "Lora",
        "description": "Rich forest green with mint-tinted background",
    },
    "sunset": {
        "primary": "#7b341e",
        "accent": "#ed8936",
        "bg": "#fffaf0",
        "font": "Poppins",
        "description": "Warm amber and burnt orange on a creamy background",
    },
    "midnight": {
        "primary": "#1a202c",
        "accent": "#805ad5",
        "bg": "#2d3748",
        "font": "Rajdhani",
        "description": "Dark slate with vivid purple accents — dark mode",
    },
    "minimal": {
        "primary": "#1a1a1a",
        "accent": "#e53e3e",
        "bg": "#ffffff",
        "font": "Helvetica Neue",
        "description": "Clean black and white with a single red accent",
    },
    "corporate": {
        "primary": "#2c3e50",
        "accent": "#2980b9",
        "bg": "#ecf0f1",
        "font": "Source Sans Pro",
        "description": "Professional navy and blue on a light grey background",
    },
    "creative": {
        "primary": "#2d1b69",
        "accent": "#e040fb",
        "bg": "#fce4ec",
        "font": "Quicksand",
        "description": "Deep indigo with vibrant magenta on a blush background",
    },
    "warm": {
        "primary": "#3e2723",
        "accent": "#ff7043",
        "bg": "#fbe9e7",
        "font": "Merriweather",
        "description": "Deep brown and coral on a peach-tinted background",
    },
    "tech": {
        "primary": "#0d1117",
        "accent": "#58a6ff",
        "bg": "#161b22",
        "font": "JetBrains Mono",
        "description": "GitHub-inspired dark mode with blue accent",
    },
}

# ANSI color helpers
def _ansi_hex(hex_color, text):
    """Approximate ANSI 256-color block for a hex color."""
    try:
        r = int(hex_color[1:3], 16)
        g = int(hex_color[3:5], 16)
        b = int(hex_color[5:7], 16)
        return "\033[38;2;{};{};{}m{}\033[0m".format(r, g, b, text)
    except (ValueError, IndexError):
        return text


def _color_swatch(hex_color):
    """Return a colored block swatch for terminal display."""
    return _ansi_hex(hex_color, "██")


def list_themes():
    """Print a formatted table of all themes with color swatches."""
    header = "{:<12} {:<6} {:<6} {:<6} {:<20} {}".format(
        "Theme", "Primary", "Accent", "Bg", "Font", "Description"
    )
    print(header)
    print("-" * len(header))
    for name, t in sorted(THEMES.items()):
        primary_swatch = _color_swatch(t["primary"])
        accent_swatch = _color_swatch(t["accent"])
        bg_swatch = _color_swatch(t["bg"])
        print("{:<12} {} {:<5} {} {:<5} {} {:<5} {:<20} {}".format(
            name,
            primary_swatch, t["primary"],
            accent_swatch, t["accent"],
            bg_swatch, t["bg"],
            t["font"],
            t.get("description", ""),
        ))


def show_theme(name):
    """Print full details of one theme.

    Args:
        name (str): Theme name (case-insensitive).
    """
    key = name.lower()
    if key not in THEMES:
        print("Error: unknown theme '{}'. Available: {}".format(
            name, ", ".join(sorted(THEMES.keys()))
        ), file=sys.stderr)
        sys.exit(1)

    t = THEMES[key]
    print("=" * 40)
    print("  Theme: {}".format(key.title()))
    print("=" * 40)
    print("  Description : {}".format(t.get("description", "—")))
    print()
    print("  Primary     : {} {}".format(_color_swatch(t["primary"]), t["primary"]))
    print("  Accent      : {} {}".format(_color_swatch(t["accent"]), t["accent"]))
    print("  Background  : {} {}".format(_color_swatch(t["bg"]), t["bg"]))
    print("  Font        : {}".format(t["font"]))
    print()
    print("CSS snippet:")
    print(generate_css(key))


def generate_css(name):
    """Output CSS :root variables for the given theme.

    Args:
        name (str): Theme name (case-insensitive).

    Returns:
        str: CSS :root block string.
    """
    key = name.lower()
    if key not in THEMES:
        print("Error: unknown theme '{}'. Available: {}".format(
            name, ", ".join(sorted(THEMES.keys()))
        ), file=sys.stderr)
        sys.exit(1)

    t = THEMES[key]
    lines = [
        "/* Theme: {} — generated by load_themes.py */".format(key),
        ":root {",
        "  --theme-primary: {};".format(t["primary"]),
        "  --theme-accent: {};".format(t["accent"]),
        "  --theme-bg: {};".format(t["bg"]),
        "  --theme-font: '{}';".format(t["font"]),
        "}",
    ]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Load and list available themes from the theme catalog.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--list", action="store_true", help="List all themes")
    group.add_argument("--show", metavar="THEME", help="Show full details of a theme")
    group.add_argument("--css", metavar="THEME", help="Output CSS variables for a theme")

    args = parser.parse_args()

    if args.list:
        list_themes()
    elif args.show:
        show_theme(args.show)
    elif args.css:
        print(generate_css(args.css))


if __name__ == "__main__":
    main()
