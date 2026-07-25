from pathlib import Path

import streamlit as st

from components.metrics import metric_card
from utils.dashboard_data import get_homepage_metrics
from utils.ui import load_css

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

from config import (
    APP_TITLE,
    APP_ICON,
    LAYOUT,
    SIDEBAR_STATE,
)

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout=LAYOUT,
    initial_sidebar_state=SIDEBAR_STATE,
)


# --------------------------------------------------
# Load Global CSS
# --------------------------------------------------
load_css()


# --------------------------------------------------
# Home Page
# --------------------------------------------------
st.header("FIFA World Cup 2026 Analytics Dashboard")

st.markdown(
    """
Welcome to the FIFA World Cup 2026 Analytics Dashboard.

This project provides interactive insights into the tournament using
Python, SQLite, SQL, Pandas, Streamlit, and Plotly.
    """
)

st.divider()

# --------------------------------------------------
# Dashboard Data
# --------------------------------------------------
metrics = get_homepage_metrics()

# --------------------------------------------------
# Tournament Snapshot
# --------------------------------------------------
st.subheader("Tournament Snapshot")

col1, col2, col3, col4 = st.columns(4)

with col1:
    metric_card("Total Teams", metrics["teams"])

with col2:
    metric_card("Total Players", f"{metrics['players']:,}")

with col3:
    metric_card("Total Matches", metrics["matches"])

with col4:
    metric_card("Total Goals", metrics["goals"])
st.divider()

# --------------------------------------------------
# Explore
# --------------------------------------------------
st.subheader("Explore")

st.markdown(
    """
Use the **sidebar** to explore:

- Tournament Overview
- Players
- Teams
- Matches
- Venues
- Referees
- Events
- Awards
"""
)

st.success("⬅ Select a page from the sidebar to begin exploring the tournament.")