from dashboard.components.charts import (
    plot_goals_by_team_chart,
    plot_best_defense_chart,
    plot_man_of_the_match_teams
)
from dashboard.components.podium import podium_card
from dashboard.layout import (
    section,
    three_columns,
    two_columns,
)
from dashboard.theme.css import load_css
from dashboard.utils.dashboard_data import (
    get_tournament_summary,
    get_team_charts,
    get_team_tables,
)

import streamlit as st

# Load CSS
load_css()

from src.analytics.database import AnalyticsQueryError

# Teams Summary
try:
    summary = get_tournament_summary()
    charts = get_team_charts()
    tables = get_team_tables()
except AnalyticsQueryError:
    st.error("Unable to load teams data right now. Please try again later.")
    st.stop()

with section("Finalists"):
    col1, col2, col3 = three_columns()

    with col1:
        podium_card("Champion", summary["winner"], medal="gold")
    with col2:
        podium_card("Runner-up", summary["runner_up"], medal="silver")
    with col3:
        podium_card("Third place", summary["third_place"], medal="bronze")


    col1, col2, col3 = three_columns()

    with col1:
        with st.container(border=True):
            st.caption("Goals by Team")
            st.plotly_chart(
                plot_goals_by_team_chart(
                    charts["goals_by_team"]
                ),
                width="stretch",
            )

    with col2:
        with st.container(border=True):
            st.caption("Best Defensive Teams")
            st.plotly_chart(
                plot_best_defense_chart(
                    charts["best_defense"]
                ),
                width="stretch",
            )

    with col3:
        with st.container(border=True):
            st.caption("Most MOTM Awards")
            st.plotly_chart(
                plot_man_of_the_match_teams(
                    charts["man_of_the_match_teams"]
                ),
                width="stretch",
            )
    

    col1, col2 = two_columns()

    with col1:
        with st.container(border=True):
            st.caption("Attacking Statistics")
            st.dataframe(
                tables["attacking"].rename(columns={
                    "team": "Country",
                    "matches_played": "Matches Played",
                    "total_shots": "Total Shots",
                    "shots_on_target": "Shots on Target",
                    "shots_per_match": "Shots Per Match",
                    "shots_on_target_per_match": "Shots on Target/Match"
                }),
                hide_index=True,
                width="stretch",
                height=180,
            )

    with col2:
        with st.container(border=True):
            st.caption("Team Discipline")
            st.dataframe(
                tables["discipline_teams"].rename(columns={
                    "team": "Country",
                    "total_yellow_cards": "Yellow Cards",
                    "total_red_cards": "Red Cards",
                    "matches_played": "Matches Played",
                    "cards_per_match": "Cards Per Match"
                }),
                hide_index=True,
                width="stretch",
                height=180,
            )