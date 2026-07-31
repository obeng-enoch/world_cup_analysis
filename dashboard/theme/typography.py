"""
Typography definitions used throughout the dashboard.
"""

FONT_FAMILY = "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif"
FONT_FAMILY_NUMERIC = "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif"

# Font sizes
PAGE_TITLE_SIZE = 32
PAGE_DESCRIPTION_SIZE = 15
SECTION_TITLE_SIZE = 20

CARD_TITLE_SIZE = 14
CARD_SUBTITLE_SIZE = 12

METRIC_VALUE_SIZE = 30
METRIC_DELTA_SIZE = 13

LABEL_SIZE = 13
BODY_SIZE = 14
CAPTION_SIZE = 12
TOOLTIP_SIZE = 12

# Font Weights
WEIGHT_REGULAR = 400
WEIGHT_MEDIUM = 500
WEIGHT_SEMIBOLD = 600
WEIGHT_BOLD = 700

# Line heights
LINE_HEIGHT_TIGHT = 1.2
LINE_HEIGHT_NORMAL = 1.5
LINE_HEIGHT_LOOSE = 1.7

# Semantics groupings

PAGE_TITLE = {
    "size": PAGE_TITLE_SIZE,
    "weight": WEIGHT_BOLD,
    "line_height": LINE_HEIGHT_TIGHT,
}

SECTION_TITLE = {
    "size": SECTION_TITLE_SIZE,
    "weight": WEIGHT_SEMIBOLD,
    "line_height": LINE_HEIGHT_TIGHT,
}
 
CARD_TITLE = {
    "size": CARD_TITLE_SIZE,
    "weight": WEIGHT_MEDIUM,
    "line_height": LINE_HEIGHT_NORMAL,
}
 
METRIC_VALUE = {
    "size": METRIC_VALUE_SIZE,
    "weight": WEIGHT_BOLD,
    "line_height": LINE_HEIGHT_TIGHT,
}
 
BODY = {
    "size": BODY_SIZE,
    "weight": WEIGHT_REGULAR,
    "line_height": LINE_HEIGHT_NORMAL,
}
 
CAPTION = {
    "size": CAPTION_SIZE,
    "weight": WEIGHT_REGULAR,
    "line_height": LINE_HEIGHT_NORMAL,
}