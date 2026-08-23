from dashboard.components.charts import (
    plot_club_goal_contributions_chart,
    plot_club_minutes_played_chart,
    plot_club_representation_chart,
    plot_club_value_chart,
)
from dashboard.components.leader import leader_card
from dashboard.layout import (
    section,
    three_columns,
    two_columns,
)

from dashboard.theme.css import load_css

from dashboard.utils.dashboard_data import (
    get_club_summary,
    get_club_charts,
    get_club_tables,
)
from dashboard.theme.icons import USERS, TROPHY, TRENDING_UP
from dashboard.theme.colors import PRIMARY

import streamlit as st

# load css
load_css()

from src.analytics.database import AnalyticsQueryError

# Clubs Summary
try:
    summary = get_club_summary()
    charts = get_club_charts()
    tables = get_club_tables()
except AnalyticsQueryError:
    st.error("Unable to load clubs data right now. Please try again later.")
    st.stop()

most_represented = summary["most_represented"]
man_of_the_match_clubs = summary["man_of_the_match_clubs"]
top_contributor = summary["top_contributor"]

with section("Club Highlights"):
    col1, col2, col3 = three_columns()

    with col1:
        leader_card(
            title="Most Represented Club",
            name=most_represented["club_team"],
            subtitle=(
                f'{most_represented["countries_represented"]} '
                "countries represented"
            ),
            value=f'{most_represented["players_sent"]} players',
            icon=USERS,
            icon_color=PRIMARY,
        )

    with col2:
        leader_card(
            title="Club Whose Players Won Most MOTM Awards",
            name=man_of_the_match_clubs["club_team"],
            subtitle=f'{man_of_the_match_clubs["winning_players"]} award-winning players',
            value=f'{man_of_the_match_clubs["man_of_the_match_awards"]} MOTM awards',
            icon=TROPHY,
            icon_color=PRIMARY,
        )

    with col3:
        leader_card(
            title="Top Club Contributors",
            name=top_contributor["club_team"],
            subtitle=(
                f'{top_contributor["goals"]} goals + '
                f'{top_contributor["assists"]} assists'
            ),
            value=f'{top_contributor["goal_contributions"]} contributions',
            icon=TRENDING_UP,
            icon_color=PRIMARY,
        )


    # CLUB PERFORMANCE
    col1, col2, col3 = three_columns()

    with col1:
        with st.container(border=True):
            st.caption("Club Representation")
            st.plotly_chart(
                plot_club_representation_chart(
                    charts["most_representation"]
                ),
                width="stretch",
            )

    with col2:
        with st.container(border=True):
            st.caption("Clubs Whose Players have had most minutes")
            st.plotly_chart(
                plot_club_minutes_played_chart(
                    charts["minutes_played"]
                ),
                width="stretch",
            )

    with col3:
        with st.container(border=True):
            st.caption("Club Performance")
            st.plotly_chart(
                plot_club_goal_contributions_chart(
                    charts["goal_contributions"]
                ),
                width="stretch",
            )




    # CLUB INTELLIGENCE
    col1, col2 = two_columns()

    with col1:
        with st.container(border=True):
            st.caption("Club Discipline")
            st.dataframe(
                tables["discipline"].rename(columns={
                    "club_team": "Club",
                    "players_sent": "Players Sent",
                    "total_yellow_cards": "Yellow Cards",
                    "total_red_cards": "Red Cards",
                }),
                hide_index=True,
                width="stretch",
                height=180,
            )

    with col2:
        with st.container(border=True):
            st.caption("Club Representation in Medal Teams")
            st.dataframe(
                tables["club_medals"].rename(columns={
                    "club_team": "Club",
                    "gold": "Gold",
                    "silver": "Silver",
                    "bronze": "Bronze",
                    "total_medals": "Total Medals"
                }),
                hide_index=True,
                width="stretch",
                height=180,
            )