"""
Reusable KPI metric card component.
"""

from html import escape

import streamlit as st

from dashboard.components.icon import render_icon
from dashboard.theme.colors import PRIMARY


def metric_card(
    title: str,
    value,
    icon: str,
    delta: str | None = None,
    icon_color: str = PRIMARY,
) -> None:
    """
    Render a reusable KPI metric card.
    """

    icon_html = render_icon(
        icon=icon,
        size=22,
        color=icon_color,
    )

    title_html = escape(str(title))
    value_html = escape(str(value))
    delta_html = ""

    if delta is not None:
        delta_html = (
            f'<div class="metric-delta">{escape(str(delta))}</div>'
        )

    # Use Streamlit's dedicated HTML element. st.markdown is a Markdown
    # renderer first, so a call that is not HTML-enabled displays these tags
    # literally instead of rendering the card.
    st.markdown(
        f"""<div class="dashboard-card metric-card">
<div class="metric-header">
{icon_html}
<div class="metric-title">{title_html}</div>
</div>
<div class="metric-value">{value_html}</div>
{delta_html}
</div>""",
        unsafe_allow_html=True,
    )