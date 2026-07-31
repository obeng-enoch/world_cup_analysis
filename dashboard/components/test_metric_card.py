import streamlit as st

from dashboard.theme.css import load_css
from dashboard.components.metrics import metric_card

from dashboard.theme.icons import (
    GOAL,
    TROPHY,
    PLAYER,
    MATCH,
)

load_css()

st.title("Metric Card Test")

cols = st.columns(4)

with cols[0]:
    metric_card(
        title="Goals",
        value=308,
        icon=GOAL,
    )

with cols[1]:
    metric_card(
        title="Champion",
        value="Spain",
        icon=TROPHY,
    )

with cols[2]:
    metric_card(
        title="Players",
        value=1248,
        icon=PLAYER,
    )

with cols[3]:
    metric_card(
        title="Matches",
        value=104,
        icon=MATCH,
    )