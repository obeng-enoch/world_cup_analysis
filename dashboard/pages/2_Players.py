from dashboard.components.charts import (
    plot_goal_contributions_chart,
    plot_goalkeeper_saves_chart,
)
from dashboard.components.leader import leader_card
from dashboard.layout import (
    section,
    three_columns,
    two_columns,
)
from dashboard.theme.css import load_css
from dashboard.theme.icons import GOAL, PLAYER

from dashboard.utils.dashboard_data import (
    get_player_summary,
    get_player_charts,
    get_scoring_tables,
    get_player_achievements,
    get_discipline_tables,
    get_goalkeeping_tables,
)

import streamlit as st

# Load CSS
load_css()

# --------------------------------------------------
# Load Data
# --------------------------------------------------

summary = get_player_summary()
charts = get_player_charts()
scoring = get_scoring_tables()
achievements = get_player_achievements()
discipline = get_discipline_tables()
goalkeeping = get_goalkeeping_tables()

# --------------------------------------------------
# Top Performers
# --------------------------------------------------

with section("Top performers"):

    col1, col2, col3 = three_columns()

    with col1:
        scorer = summary["top_scorer"]

        leader_card(
            title="Top Scorer",
            name=scorer["player_name"],
            subtitle=scorer["team"],
            value=f'{scorer["goals"]} Goals',
            icon=GOAL,
        )

    with col2:
        assist = summary["top_assist"]

        leader_card(
            title="Top Assist Provider",
            name=assist["player_name"],
            subtitle=assist["team"],
            value=f'{assist["assists"]} Assists',
            icon=PLAYER,
        )

    with col3:
        goalkeeper = summary["top_goalkeeper"]

        leader_card(
            title="Best Goalkeeper",
            name=goalkeeper["player_name"],
            subtitle=goalkeeper["team"],
            value=f'{goalkeeper["clean_sheets"]} Clean Sheets',
            icon=PLAYER,   # Replace with a goalkeeper/shield icon if you have one.
        )

# --------------------------------------------------
# Goal Contributions Chart
# --------------------------------------------------
left, right = two_columns()

with left:
    with st.container(border=True):
        st.caption("Top 5 Goal Contributions")

        st.plotly_chart(
            plot_goal_contributions_chart(
                charts["goal_contributions"]
            ),
            width="stretch",
        )

with right:
    with st.container(border=True):
        st.caption("Top 5 Keepers With Most Saves")

        st.plotly_chart(
            plot_goalkeeper_saves_chart(
                charts["top_saves"]
            ),
            width="stretch"
        )
# --------------------------------------------------
# Scoring Tables
# --------------------------------------------------

left, right = two_columns()

with left:

    with st.container(border=True):

        st.caption("Top Scorers")

        st.dataframe(
            scoring["top_scorers"],
            hide_index=True,
            width="stretch",
            height=260,
        )

with right:

    with st.container(border=True):

        st.caption("Top Assists")

        st.dataframe(
            scoring["top_assists"],
            hide_index=True,
            width="stretch",
            height=260,
        )

# --------------------------------------------------
# Achievements
# --------------------------------------------------

left, right = two_columns()

with left:

    with st.container(border=True):

        st.caption("Hat Tricks")

        st.dataframe(
            achievements["hat_tricks"],
            hide_index=True,
            width="stretch",
            height=220,
        )

with right:

    with st.container(border=True):

        st.caption("Total Cards")

        st.dataframe(
            discipline["yellow_cards"],
            hide_index=True,
            width="stretch",
            height=220,
        )