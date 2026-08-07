from dashboard.components.charts import (
    plot_goals_by_team_chart,
    plot_best_defense_chart,
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

# Load data
summary = get_tournament_summary()
charts = get_team_charts()
tables = get_team_tables()

with section("Finalists"):
    champion_col, runner_up_col, third_place_col = three_columns()

    with champion_col:
        podium_card("Champion", summary["winner"], medal="gold")
    with runner_up_col:
        podium_card("Runner-up", summary["runner_up"], medal="silver")
    with third_place_col:
        podium_card("Third place", summary["third_place"], medal="bronze")


left, right = two_columns()

with left:

    with st.container(border=True):

        st.caption("Goals by Team")

        st.plotly_chart(
            plot_goals_by_team_chart(
                charts["goals_by_team"]
            ),
            width="stretch",
        )

with right:

    with st.container(border=True):

        st.caption("Best Defensive Teams")

        st.plotly_chart(
            plot_best_defense_chart(
                charts["best_defense"]
            ),
            width="stretch",
        )

left, right = two_columns()

with left:
    with st.container(border=True):
        st.caption("Attacking Statistics")

        st.dataframe(
            tables["attacking"],
            hide_index=True,
            width="stretch",
            height=260,
        )

with right:
    with st.container(border=True):
        st.caption("Team Discipline")

        st.dataframe(
            tables["discipline"],
            hide_index=True,
            width="stretch",
            height=260,
        )