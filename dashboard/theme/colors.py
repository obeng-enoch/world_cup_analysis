"""
dashboard/theme/colors.py

Central colour palette for the FIFA World Cup Analytics Dashboard.

Every UI component, Plotly chart and CSS rule should reference these
constants instead of hard-coding colour values.
"""

# Primary Brand Colours
PRIMARY = "#0057B8"        # FIFA-inspired blue
SECONDARY = "#0B1F3A"      # Deep navy
ACCENT = "#D4AF37"         # Gold

# Status Colours
SUCCESS = "#2E8B57"
WARNING = "#E67E22"
ERROR = "#C0392B"
INFO = "#3498DB"

# Neutral Colours
WHITE = "#FFFFFF"
BLACK = "#000000"

BACKGROUND = "#F5F7FA"
SURFACE = "#FFFFFF"

TEXT_PRIMARY = "#1F2937"
TEXT_SECONDARY = "#6B7280"

BORDER = "#D9E2EC"

GRID = "#E5E7EB"
CHART_LINE = PRIMARY

HOVER = "#EEF4FF"
HOVER_DARK = "#123A6B"
ACTIVE = "#00458F"

CARD_SHADOW = "rgba(0,0,0,0.08)"

TEXT_MUTED = "#6B7280"
TEXT_INVERSE = "#FFFFFF"

CHART_SEQUENCE = [
    PRIMARY,
    ACCENT,
    SUCCESS,
    SECONDARY,
    ERROR,
]

# Award-tier colors
GOLD = "#D4AF37"
SILVER = "#A8AAAD"
BRONZE = "#B08D57"


STATUS = {
    "success": SUCCESS,
    "warning": WARNING,
    "error": ERROR,
}
 
MEDALS = {
    "gold": GOLD,
    "silver": SILVER,
    "bronze": BRONZE,
}