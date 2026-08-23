from pathlib import Path

import streamlit as st

from dashboard.components.metrics import metric_card
from dashboard.theme.icons import GOAL, MATCH, USERS, WORLD
from dashboard.utils.dashboard_data import get_homepage_metrics
from dashboard.theme.css import load_css
from src.analytics.database import AnalyticsQueryError

# Page Configuration

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

# Load Global CSS
load_css()


# Home Page
st.header("FIFA World Cup 2026 Analytics Dashboard")

st.markdown(
    """
Welcome to the FIFA World Cup 2026 Analytics Dashboard.

This project provides interactive insights into the tournament using
Python, SQLite, SQL, Pandas, Streamlit, and Plotly.
    """
)

# Dashboard Data
try:
    metrics = get_homepage_metrics()
except AnalyticsQueryError:
    st.error("Unable to load dashboard data right now. Please try again later.")
    st.stop()

# Tournament Snapshot
st.subheader("Tournament Snapshot")

col1, col2, col3, col4 = st.columns(4)

with col1:
    metric_card("Total Teams", metrics["teams"], icon=WORLD)

with col2:
    metric_card("Total Players", f"{metrics['players']:,}", icon=USERS)

with col3:
    metric_card("Total Matches", metrics["matches"], icon=MATCH)

with col4:
    metric_card("Total Goals", metrics["goals"], icon=GOAL)

# Explore
st.subheader("Explore")

st.markdown(
    """
Use the **sidebar** to explore:

- Tournament Overview
- Matches
- Teams
- Players
- Clubs
- Referees
- Venues
"""
)

st.success("⬅ Select a page from the sidebar to begin exploring the tournament.")
