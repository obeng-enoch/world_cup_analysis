"""
Reusable KPI metric card component.
"""

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

    delta_html = ""

    if delta is not None:
        delta_html = (
            f'<div class="metric-delta">{delta}</div>'
        )

    st.markdown(
        f"""
<div class="dashboard-card metric-card">

    <div class="metric-header">

        {icon_html}

        <div class="metric-title">
            {title}
        </div>

    </div>

    <div class="metric-value">
        {value}
    </div>

    {delta_html}

</div>
""",
        unsafe_allow_html=True,
    )