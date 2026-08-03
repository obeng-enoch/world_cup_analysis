from dashboard.components.metrics import metric_card
from dashboard.components.podium import podium_card
from dashboard.theme.icons import GOAL, MATCH, PLAYER, WORLD
from dashboard.components.charts import plot_stage_goals_chart
from dashboard.theme.css import load_css
from dashboard.layout import section, kpi_grid, two_columns, three_columns, chart_row

from dashboard.utils.dashboard_data import (
    get_tournament_summary,
    get_tournament_awards,
    get_tournament_finish_table,
    get_goals_per_stage_chart,
)

import streamlit as st

# Load CSS
load_css()

# Tournament Summary
summary = get_tournament_summary()
standings = get_tournament_finish_table()
awards = get_tournament_awards()
goals_by_stage = get_goals_per_stage_chart()

with section("Finalists"):
    champion_col, runner_up_col, third_place_col = three_columns()

    with champion_col:
        podium_card("Champion", summary["winner"], medal="gold")
    with runner_up_col:
        podium_card("Runner-up", summary["runner_up"], medal="silver")
    with third_place_col:
        podium_card("Third place", summary["third_place"], medal="bronze")

chart_col, awards_col = two_columns(ratio=(3, 2))

with chart_col:
    with st.container(border=True):
        chart_title_col, control_col = st.columns([3, 2])

        with chart_title_col:
            st.caption("Tournament scoring by stage")

        with control_col:
            selected_measure = st.segmented_control(
                "Chart measure",
                options=["Total goals", "Goals per match"],
                default="Total goals",
                key="stage_measure",
                label_visibility="collapsed",
            )

        if selected_measure == "Total goals":
            value_column = "total_goals"
            value_label = "Total goals"
        else:
            value_column = "avg_goals_per_match"
            value_label = "Goals per match"

        st.plotly_chart(
            plot_stage_goals_chart(
                goals_by_stage,
                value_column=value_column,
                value_label=value_label,
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
            height=210,
            width="stretch",
        )

with section("Tournament standings"):
    st.dataframe(
        standings.drop(columns="finish_rank"),
        hide_index=True,
        height=180,
        width="stretch",
    )