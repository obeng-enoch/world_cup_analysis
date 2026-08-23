import streamlit as st

from dashboard.components.charts import (
    plot_referee_matches_chart,
    plot_referee_fouls_chart,
    plot_referee_card_comparison_chart,
)
from dashboard.components.leader import leader_card
from dashboard.layout import (
    section,
    three_columns,
    two_columns,
)
from dashboard.utils.dashboard_data import (
    get_referee_summary,
    get_referee_charts,
    get_referee_tables,
)
from dashboard.theme.icons import FLAG, ALERT_TRIANGLE, CREDIT_CARD
from dashboard.theme.colors import PRIMARY
from dashboard.theme.css import load_css

load_css()

from src.analytics.database import AnalyticsQueryError

# Clubs Summary
try:
    summary = get_referee_summary()
    charts = get_referee_charts()
    tables = get_referee_tables()
except AnalyticsQueryError:
    st.error("Unable to load referee data right now. Please try again later.")
    st.stop()

most_used = summary["most_used"]
highest_fouls = summary["highest_fouls"]
highest_cards = summary["highest_cards"]

with section("Referee Highlights"):
    col1, col2, col3 = three_columns()

    with col1:
        leader_card(
            title="Most Matches Officiated",
            name=most_used["referee"],
            subtitle=most_used["country"],
            value=f'{most_used["matches_officiated"]} matches',
            icon=FLAG,
            icon_color=PRIMARY,
        )

    with col2:
        leader_card(
            title="Highest Average Fouls",
            name=highest_fouls["referee"],
            subtitle=highest_fouls["country"],
            value=f'{int(highest_fouls["avg_fouls_per_match"])} fouls/match',
            icon=ALERT_TRIANGLE,
            icon_color=PRIMARY,
        )

    with col3:
        leader_card(
            title="Highest Cards per Game",
            name=highest_cards["referee"],
            subtitle=highest_cards["country"],
            value=f'{int(highest_cards["actual_avg_cards_per_game"])} cards/match',
            icon=CREDIT_CARD,
            icon_color=PRIMARY,
        )

    col1, col2, col3 = three_columns()

    with col1:
        with st.container(border=True):
            st.caption("Referee Workload")
            st.plotly_chart(
                plot_referee_matches_chart(
                    charts["matches_officiated"]
                ),
                width="stretch",
            )

    with col2:
        with st.container(border=True):
            st.caption("Fouls per match")
            st.plotly_chart(
                plot_referee_fouls_chart(
                    charts["fouls"]
                ),
                width="stretch",
            )

    with col3:
        with st.container(border=True):
            st.caption("Officiating Style")
            st.plotly_chart(
                plot_referee_card_comparison_chart(
                    charts["card_comparison"]
                ),
                width="stretch",
            )
    col1, col2 = two_columns()
    with col1:
        with st.container(border=True):
            st.caption("Tournament Workload")
            st.dataframe(
                tables["stage_workload"].rename(columns={
                    "referee": "Referee",
                    "stage": "Stage",
                    "matches_officiated": "Matches Officiated" 
                }),
                hide_index=True,
                width="stretch",
                height=180,
            )

    with col2:
        with st.container(border=True):
            st.caption("Red-Card Incidents")
            st.dataframe(
                tables["red_cards"].rename(columns={
                    "referee": "Referee",
                    "country": "Country",
                    "match": "Match",
                    "carded_team": "Carded Team",
                    "player_name": "Player Carded",
                    "minute": "Minute"
                }),
                hide_index=True,
                width="stretch",
                height=180,
            )