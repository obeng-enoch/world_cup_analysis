import streamlit as st

from dashboard.components.icon import render_icon
from dashboard.theme.colors import TEXT_PRIMARY
from dashboard.theme.icons import (
    TROPHY,
    PLAYER,
    GOAL,
    MATCH,
    VENUE,
    AWARD,
    CHART,
)

st.set_page_config(page_title="Icon Test", layout="wide")

st.title("Lucide Icon System Test")

icons = [
    ("trophy", TROPHY),
    ("users", PLAYER),
    ("target", GOAL),
    ("calendar-days", MATCH),
    ("map-pin", VENUE),
    ("award", AWARD),
    ("chart-column", CHART),
]

cols = st.columns(4)

for i, (label, icon) in enumerate(icons):
    with cols[i % 4]:
        st.markdown(
            render_icon(
                icon=icon,
                size=48,
            ),
            unsafe_allow_html=True,
        )
        st.caption(label)