from dashboard.components.metrics import metric_card
from dashboard.components.podium import podium_card
from dashboard.theme.icons import GOAL, MATCH, WORLD
from dashboard.theme.css import load_css
from dashboard.layout import section, kpi_grid, two_columns, three_columns, chart_row
from dashboard.utils.dashboard_data import (
    get_tournament_summary,
    get_tournament_awards,
    get_tournament_finish_table,
    get_tournament_event_counts,
)

from dashboard.components.charts import plot_event_counts_chart

import streamlit as st

from src.analytics.database import AnalyticsQueryError

# Tournament Summary
try:
    summary = get_tournament_summary()
    standings = get_tournament_finish_table()
    awards = get_tournament_awards()
    events = get_tournament_event_counts()
except AnalyticsQueryError:
    st.error("Unable to load tournament data right now. Please try again later.")
    st.stop()

# Load CSS
load_css()

with section("Finalists"):
    col1, col2, col3 = three_columns()

    with col1:
        podium_card("Champion", summary["winner"], medal="gold")
    with col2:
        podium_card("Runner-up", summary["runner_up"], medal="silver")
    with col3:
        podium_card("Third place", summary["third_place"], medal="bronze")

    col1, col2 = two_columns(ratio=(3, 2))

    with col1:
        with st.container(border=True):
            st.caption("Match events")

            st.plotly_chart(
                plot_event_counts_chart(
                    events,
                    height=210,
                ),
                width="stretch",
            )

    with col2:
        with st.container(border=True):
            st.caption("Tournament awards")

            st.dataframe(
                awards.rename(columns={
                    "player_name": "Player",
                    "award_name": "Award",
                    "team": "Team",
                }),
                hide_index=True,
                height=210,
                width="stretch",
            )

    with st.container (border=True):
        st.caption("Tournament standings")
        st.dataframe(
            standings.drop(columns="finish_rank").rename(columns={
                "team": "Country",
                "confederation": "Confederation",
                "stage_reached": "Stage Reached",
                "tournament_finish": "Tournament Finish",
            }),
            hide_index=True,
            height=180,
            width="stretch",
        )