"""
Global dashboard stylesheet.

This module injects the application's global CSS.

Responsibilities
----------------
- Dashboard cards
- Metric cards
- Typography styling
- Hover effects
- Shared layout classes

Do NOT hard-code colours, spacing or typography.
Everything should come from the theme modules.
"""

import streamlit as st

from dashboard.theme.colors import (
    SURFACE,
    BORDER,
    TEXT_PRIMARY,
    TEXT_SECONDARY,
    HOVER,
)

from dashboard.theme.constants import (
    CARD_RADIUS,
    BORDER_WIDTH,
    CARD_SHADOW,
    CARD_SHADOW_HOVER,
    KPI_HEIGHT,
    ANIMATION_DURATION,
)

from dashboard.theme.spacing import (
    CARD_PADDING,
    ICON_TEXT_GAP,
    SECTION_MARGIN,
    PAGE_TOP_PADDING
)

from dashboard.theme.typography import (
    FONT_FAMILY,
    CARD_TITLE,
    METRIC_VALUE,
    METRIC_DELTA_SIZE,
    SECTION_TITLE,
    BODY,
)

CSS = f"""
<style>

/* Global */

html,
body,
[class*="css"] {{

    font-family: {FONT_FAMILY};

}}

/* Page container */

.block-container {{

    padding-top:3.5rem;
    padding-bottom:2rem;

}}

/* Show Streamlit's floating header/toolbar */

header[data-testid="stHeader"] {{
    display: block;
}}

/* Dashboard Card */

.dashboard-card {{
    background: linear-gradient(145deg, #181C22 0%, #12151A 100%);
    border: 1px solid #252A31;
    border-radius: 10px;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.24);
    padding: 8px;
    transition: transform 150ms ease, border-color 150ms ease,
        box-shadow 150ms ease;
}}

.dashboard-card:hover {{
    transform: translateY(-2px);
    border-color: #FF7A00;
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.35);
}}


/* Metric Card */

.metric-card {{
    position: relative;
    overflow: hidden;
}}

.metric-card::after {{
    content: "";
    position: absolute;
    right: -24px;
    bottom: -42px;
    width: 110px;
    height: 110px;
    border-radius: 50%;
    background: rgba(255, 122, 0, 0.08);
}}


/* Metric Header */

.metric-header {{

    display: flex;

    align-items: center;

    gap: {ICON_TEXT_GAP}px;

}}


/* Metric Title */

.metric-title {{

    color: {TEXT_SECONDARY};

    font-size: {CARD_TITLE["size"]}px;

    font-weight: {CARD_TITLE["weight"]};

}}


/* Metric Value */

.metric-value {{

    color: {TEXT_PRIMARY};

    font-size: {METRIC_VALUE["size"]}px;

    font-weight: {METRIC_VALUE["weight"]};

}}


/* Metric Delta */

.metric-delta {{

    color: {TEXT_SECONDARY};

    font-size: {METRIC_DELTA_SIZE}px;

}}

/* Podium Card */

.podium-card {{

    display: flex;

    flex-direction: column;

    justify-content: center;

    align-items: center;

    text-align: center;

    border-top: 4px solid var(--medal-color, {BORDER});

}}


/* Podium Position */

.podium-position {{

    color: {TEXT_SECONDARY};

    font-size: {CARD_TITLE["size"]}px;

    font-weight: {CARD_TITLE["weight"]};

}}

/* Podium Team */

.podium-team {{

    color: {TEXT_PRIMARY};

    font-size: {METRIC_VALUE["size"]}px;

    font-weight: {METRIC_VALUE["weight"]};
    
    margin-top: {ICON_TEXT_GAP}px;

}}

/* Award Card */

.award-card {{

    display: flex;

    flex-direction: column;

}}


/* Award Header */

.award-header {{

    display: flex;

    align-items: center;

    gap: {ICON_TEXT_GAP}px;

}}


/* Award Name */

.award-name {{

    color: {TEXT_SECONDARY};

    font-size: {CARD_TITLE["size"]}px;

    font-weight: {CARD_TITLE["weight"]};

}}


/* Award Winner */

.award-winner {{

    color: {TEXT_PRIMARY};

    font-size: {METRIC_VALUE["size"]}px;

    font-weight: {METRIC_VALUE["weight"]};

    margin-top: {ICON_TEXT_GAP}px;

}}


/* Award Team */

.award-team {{

    color: {TEXT_SECONDARY};

    font-size: {METRIC_DELTA_SIZE}px;

    margin-top: 2px;

}}

/* Leader Card */

.leader-card {{

    display: flex;

    flex-direction: column;

}}


/* Leader Header */

.leader-header {{

    display: flex;

    align-items: center;

    gap: {ICON_TEXT_GAP}px;

}}


/* Leader Title */

.leader-title {{

    color: {TEXT_SECONDARY};

    font-size: {CARD_TITLE["size"]}px;

    font-weight: {CARD_TITLE["weight"]};

}}


/* Leader Name */

.leader-name {{

    color: {TEXT_PRIMARY};

    font-size: {METRIC_VALUE["size"]}px;

    font-weight: {METRIC_VALUE["weight"]};

    margin-top: {ICON_TEXT_GAP}px;

}}


/* Leader Subtitle */

.leader-subtitle {{

    color: {TEXT_SECONDARY};

    font-size: {BODY["size"]}px;

    font-weight: {BODY["weight"]};

    margin-top: 2px;

}}


/* Leader Value */

.leader-value {{

    color: {TEXT_PRIMARY};

    font-size: {METRIC_DELTA_SIZE}px;

    font-weight: 600;

    margin-top: {ICON_TEXT_GAP}px;

}}

/* Section Heading (used by dashboard/components/headings.py) */

.section-heading-title {{

    color: {TEXT_PRIMARY};

    font-size: {SECTION_TITLE["size"]}px;

    font-weight: {SECTION_TITLE["weight"]};

    line-height: {SECTION_TITLE["line_height"]};

}}


.section-heading-description {{

    color: {TEXT_SECONDARY};

    font-size: {BODY["size"]}px;

    font-weight: {BODY["weight"]};

    line-height: {BODY["line_height"]};

    margin-top: 2px;

}}


/* Layout spacing (used by dashboard/layout.py) */

.section-gap {{

    margin-top: {SECTION_MARGIN}px;

}}

</style>
"""


def load_css() -> None:
    """
    Inject the global dashboard stylesheet.
    """
    st.html(CSS)