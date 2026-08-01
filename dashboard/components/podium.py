"""
Reusable podium card component.
"""

from html import escape

import streamlit as st

from dashboard.theme.colors import MEDALS, TEXT_PRIMARY


def podium_card(
    position: str,
    team: str,
    medal: str | None = None,
) -> None:
    """
    Render a reusable tournament podium card for a tournament finish position.
    medal: one of "gold", "silver", "bronze" or None for no accent.
    """

    position_html = escape(str(position))
    team_html = escape(str(team))

    accent_color = MEDALS.get(medal, TEXT_PRIMARY)

    st.html(
        f"""
<div class="dashboard-card podium-card" style="--medal-color: {accent_color}">
<div class="podium-position">{position_html}</div>
<div class="podium-team">{team_html}</div>
</div>
"""
    )