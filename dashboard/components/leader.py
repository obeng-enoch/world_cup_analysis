"""
Reusable leader/highlight card component.
"""

from html import escape

import streamlit as st

from dashboard.components.icon import render_icon
from dashboard.theme.colors import PRIMARY


def leader_card(
    title: str,
    name: str,
    subtitle: str,
    value: str,
    icon: str,
    icon_color: str = PRIMARY,
) -> None:
    """
    Render a reusable leader/highlight card.

    Parameters
    ----------
    title:
        Card heading (e.g. "Top Scorer")

    name:
        Main highlighted entity (player, team, venue...)

    subtitle:
        Secondary information (country, club, location...)

    value:
        Statistic or achievement to emphasize.

    icon:
        Lucide icon name.

    icon_color:
        SVG icon colour.
    """

    icon_html = render_icon(
        icon=icon,
        size=22,
        color=icon_color,
    )

    st.markdown(
        f"""<div class="dashboard-card leader-card">
<div class="leader-header">
{icon_html}
<div class="leader-title">{escape(str(title))}</div>
</div>
<div class="leader-name">
    {escape(str(name))}
</div>
<div class="leader-subtitle">
    {escape(str(subtitle))}
</div>
<div class="leader-value">
    {escape(str(value))}
</div>
</div>
""",
        unsafe_allow_html=True,
    )