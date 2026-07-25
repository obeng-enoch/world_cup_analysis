from components.metrics import metric_card
from components.podium import podium_card

from utils.dashboard_data import get_tournament_summary
from utils.ui import load_css

import streamlit as st

# --------------------------------------------------
# Load CSS
# --------------------------------------------------

load_css()

# --------------------------------------------------
# Page Title
# --------------------------------------------------

st.header("🏆 Tournament Overview")

st.markdown(
    """
Explore the overall performance of the FIFA World Cup 2026,
including tournament statistics and the final standings.
    """
)

st.divider()

# --------------------------------------------------
# Load Data
# --------------------------------------------------

summary = get_tournament_summary()

st.subheader("Tournament Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    metric_card("Total Teams", summary["teams"])

with col2:
    metric_card("Total Players", f"{summary['players']:,}")

with col3:
    metric_card("Total Matches", summary["matches"])

with col4:
    metric_card("Total Goals", summary["goals"])

st.divider()

st.subheader("Final Standings")

col1, col2, col3 = st.columns(3)

with col1:
    podium_card("🥇 Champion", summary["winner"])

with col2:
    podium_card("🥈 Runner-up", summary["runner_up"])

with col3:
    podium_card("🥉 Third Place", summary["third_place"])

st.divider()

st.info(
    "More tournament insights, charts, and interactive tables "
    "will be added in upcoming iterations."
)