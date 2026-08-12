from dashboard.components.metrics import metric_card
from dashboard.components.podium import podium_card
from dashboard.theme.icons import GOAL, MATCH, PLAYER, WORLD
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

# Load CSS
load_css()

# Tournament Summary
summary = get_tournament_summary()
standings = get_tournament_finish_table()
awards = get_tournament_awards()
events = get_tournament_event_counts()

with section("Finalists"):
    champion_col, runner_up_col, third_place_col = three_columns()

    with champion_col:
        podium_card("Champion", summary["winner"], medal="gold")
    with runner_up_col:
        podium_card("Runner-up", summary["runner_up"], medal="silver")
    with third_place_col:
        podium_card("Third place", summary["third_place"], medal="bronze")

event_col, awards_col = two_columns(ratio=(3, 2))

with event_col:
    with st.container(border=True):
        st.caption("Match events")

        st.plotly_chart(
            plot_event_counts_chart(
                events,
                height=210,
            ),
            width="stretch",
        )

with awards_col:
    with st.container(border=True):
        st.caption("Tournament awards")

        st.dataframe(
            awards.rename(columns={
                "player_name": "Player",
                "award_name": "Award",
                "team": "Team",
            }),
            hide_index=True,
            height=255,
            width="stretch",
        )

with section("Tournament standings"):
    st.dataframe(
        standings.drop(columns="finish_rank"),
        hide_index=True,
        height=180,
        width="stretch",
    )