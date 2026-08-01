from dashboard.components.metrics import metric_card
from dashboard.components.podium import podium_card
from dashboard.components.award import award_card
from dashboard.theme.icons import GOAL, MATCH, PLAYER, WORLD
from dashboard.components.charts import plot_bar_chart

from dashboard.utils.dashboard_data import (
    get_tournament_summary,
    get_tournament_awards,
    get_tournament_finish_table,
)

from dashboard.utils.dashboard_data import get_goals_per_stage_chart
from dashboard.theme.css import load_css

import streamlit as st

# Load CSS
load_css()

# Page Title

st.header("🏆 Tournament Overview")

st.markdown(
    """
Explore the overall performance of the FIFA World Cup 2026,
including tournament statistics and the final standings.
    """
)

st.divider()

# Load Data

summary = get_tournament_summary()
standings = get_tournament_finish_table()
awards = get_tournament_awards()
goals_by_stage = get_goals_per_stage_chart()

st.subheader("Tournament Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    metric_card("Total Teams", summary["teams"], icon=WORLD)

with col2:
    metric_card("Total Players", f"{summary['players']:,}", icon=PLAYER)

with col3:
    metric_card("Total Matches", summary["matches"], icon=MATCH)

with col4:
    metric_card("Total Goals", summary["goals"], icon=GOAL)

st.divider()

st.subheader("Final Standings")

col1, col2, col3 = st.columns(3)

with col1:
    podium_card(" Champion", summary["winner"], medal="gold")

with col2:
    podium_card(" Runner-up", summary["runner_up"], medal="silver")

with col3:
    podium_card(" Third Place", summary["third_place"], medal="bronze")

st.subheader("Goals by Tournament Stage")

fig = plot_bar_chart(
    goals_by_stage,
    x="stage",
    y="total_goals",
    title="Goals Scored by Tournament Stage",
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("## Tournament Standings")

st.dataframe(
    standings,
    use_container_width=True,
    hide_index=True,
)

st.divider()

st.subheader("Tournament Awards")

for _, award in awards.iterrows():
    award_card(
        award_name=award["award_name"],
        player_name=award["player_name"],
        team=award["team"],
    )
