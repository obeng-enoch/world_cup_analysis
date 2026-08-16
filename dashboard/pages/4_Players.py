from dashboard.components.charts import (
    plot_goal_contributions_chart,
    plot_goalkeeper_saves_chart,
    plot_man_of_the_match_players,
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


# Load Data
summary = get_player_summary()
charts = get_player_charts()
scoring = get_scoring_tables()
achievements = get_player_achievements()
discipline = get_discipline_tables()
goalkeeping = get_goalkeeping_tables()

view = st.segmented_control(
    "Player analysis view",
    ["Overview", "Additional analysis"],
    default="Overview",
    key="players_view",
    label_visibility="collapsed",
)

# Top Performers
if view == "Overview":

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
            man_of_the_match_awards = summary["most_man_of_the_match_players"]
            leader_card(
                title="Player with most man of the match",
                name=man_of_the_match_awards["player_name"],
                subtitle=man_of_the_match_awards["team"],
                value=f'{man_of_the_match_awards["man_of_the_match_awards"]} MOTM Awards',
                icon=PLAYER,
            )

        with col3:
            goalkeeper = summary["top_goalkeeper"]
            leader_card(
                title="Best Goalkeeper",
                name=goalkeeper["player_name"],
                subtitle=goalkeeper["team"],
                value=f'{goalkeeper["clean_sheets"]} Clean Sheets',
                icon=PLAYER,
            )


    # Goal Contributions Chart
        left, middle, right = three_columns()
        with left:
            with st.container(border=True):
                st.caption("Top 5 Goal Contributions")
                st.plotly_chart(
                    plot_goal_contributions_chart(
                        charts["goal_contributions"]
                    ),
                    width="stretch",
                )
        with middle:
                with st.container(border=True):
                    st.caption("Top 5 MOMT Awards")
                    st.plotly_chart(
                        plot_man_of_the_match_players(
                            charts["man_of_the_match_players"]
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

        # Scoring Tables
        left, right = two_columns()

        with left:
            with st.container(border=True):
                st.caption("Top Scorers")
                st.dataframe(
                    scoring["top_scorers"],
                    hide_index=True,
                    width="stretch",
                    height=180,
                )

        with right:
            with st.container(border=True):
                st.caption("Top Assists")
                st.dataframe(
                    scoring["top_assists"],
                    hide_index=True,
                    width="stretch",
                    height=180,
                )

        # Achievements
else:
        left, right = two_columns()

        with left:
            with st.container(border=True):
                st.caption("Hat Tricks")
                st.dataframe(
                    achievements["hat_tricks"],
                    hide_index=True,
                    width="stretch",
                    height=180,
                )

        with right:
            with st.container(border=True):
                st.caption("Players with the most Man of the Match awards")
                st.dataframe(
                    achievements["man_of_the_match"],
                    hide_index=True,
                    width="stretch",
                    height=180,
                )

        with st.container(border=True):
            st.caption("Total Cards")
            st.dataframe(
                discipline["yellow_cards"],
                hide_index=True,
                width="stretch",
                height=280,
            )