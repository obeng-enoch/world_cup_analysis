"""
Reusable award card component for displaying tournament award winners.
"""

from html import escape

import streamlit as st

from dashboard.components.icon import render_icon
from dashboard.theme.colors import ACCENT
from dashboard.theme.icons import AWARD


def award_card(
    award_name: str,
    player_name: str,
    team: str,
    icon: str = AWARD,
    icon_color: str = ACCENT,
) -> None:
    """
    Render a reusable tournament award card.
    """

    icon_html = render_icon(
        icon=icon,
        size=22,
        color=icon_color,
    )

    award_name_html = escape(str(award_name))
    player_name_html = escape(str(player_name))
    team_html = escape(str(team))

    st.markdown(
        f"""
<div class="dashboard-card award-card">
    <div class="award-header">
        {icon_html}
        <div class="award-name">{award_name_html}</div>
    </div>
    <div class="award-winner">{player_name_html}</div>
    <div class="award-team">{team_html}</div>
</div>
""",
        unsafe_allow_html=True,
    )