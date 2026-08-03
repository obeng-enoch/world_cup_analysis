"""
dashboard/theme/colors.py

Central colour palette for the FIFA World Cup Analytics Dashboard.

Every UI component, Plotly chart and CSS rule should reference these
constants instead of hard-coding colour values.
"""

# Primary Brand Colours
PRIMARY = "#FF7A00"        # main orange
SECONDARY = "#0B0D10"      # page background
ACCENT = "#FFB000"         # gold highlight

# Status Colours
SUCCESS = "#22C55E"
WARNING = "#F59E0B"
ERROR = "#F43F5E"
INFO = "#34BDF8"

# Neutral Colours
WHITE = "#F4F7FB"
BLACK = "#000000"

BACKGROUND = "#0B0D10"
SURFACE = "#14171C"

TEXT_PRIMARY = "#F4F7FB"
TEXT_SECONDARY = "#9CA3AF"

BORDER = "#252A31"
GRID = "#252A31"
CHART_LINE = PRIMARY

HOVER = "#1B2027"
HOVER_DARK = "#242B35"
ACTIVE = "#E86700"

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