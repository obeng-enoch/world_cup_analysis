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
)

from dashboard.theme.typography import (
    FONT_FAMILY,
    CARD_TITLE,
    METRIC_VALUE,
    METRIC_DELTA_SIZE,
)

CSS = f"""
<style>

/* Global */

html,
body,
[class*="css"] {{

    font-family: {FONT_FAMILY};

}}


/* Dashboard Card */

.dashboard-card {{

    background: {SURFACE};

    border: {BORDER_WIDTH}px solid {BORDER};

    border-radius: {CARD_RADIUS}px;

    box-shadow: {CARD_SHADOW};

    padding: {CARD_PADDING}px;

    transition:
        transform {ANIMATION_DURATION}ms ease,
        box-shadow {ANIMATION_DURATION}ms ease;

}}


.dashboard-card:hover {{

    transform: translateY(-2px);

    box-shadow: {CARD_SHADOW_HOVER};

}}


/* Metric Card */

.metric-card {{

    display: flex;

    flex-direction: column;

    justify-content: space-between;

    height: {KPI_HEIGHT}px;

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

</style>
"""


def load_css() -> None:
    """
    Inject the global dashboard stylesheet.
    """
    st.markdown(
        CSS,
        unsafe_allow_html=True,
    )