import streamlit as st

from dashboard.components.charts import (
    plot_referee_matches_chart,
    plot_referee_fouls_chart,
    plot_referee_card_comparison_chart,
    plot_referee_stage_workload_chart,
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
from dashboard.theme.icons import CHART, TROPHY
from dashboard.theme.colors import PRIMARY
from dashboard.theme.css import load_css

load_css()

# ---------------------------------------------------------
# PAGE HEADER
# ---------------------------------------------------------

st.title("Referees")
st.caption(
    "Referee workload, foul patterns, card issuance, "
    "and tournament-stage assignments"
)

# ---------------------------------------------------------
# DATA
# ---------------------------------------------------------

summary = get_referee_summary()
charts = get_referee_charts()
tables = get_referee_tables()

# ---------------------------------------------------------
# REFEREE HIGHLIGHTS
# ---------------------------------------------------------

section("Referee Highlights")

most_used = summary["most_used"]
highest_fouls = summary["highest_fouls"]
highest_cards = summary["highest_cards"]

col1, col2, col3 = three_columns()

with col1:
    leader_card(
        title="Most Matches Officiated",
        name=most_used["referee"],
        subtitle=most_used["country"],
        value=f'{most_used["matches_officiated"]} matches',
        icon=TROPHY,
        icon_color=PRIMARY,
    )

with col2:
    leader_card(
        title="Highest Average Fouls",
        name=highest_fouls["referee"],
        subtitle=highest_fouls["country"],
        value=f'{highest_fouls["avg_fouls_per_match"]:.2f} fouls/match',
        icon=CHART,
        icon_color=PRIMARY,
    )

with col3:
    leader_card(
        title="Highest Cards per Game",
        name=highest_cards["referee"],
        subtitle=highest_cards["country"],
        value=f'{highest_cards["actual_avg_cards_per_game"]:.2f} cards/match',
        icon=CHART,
        icon_color=PRIMARY,
    )

# ---------------------------------------------------------
# REFEREE WORKLOAD
# ---------------------------------------------------------

section("Referee Workload")

col1, col2 = two_columns()

with col1:
    st.plotly_chart(
        plot_referee_matches_chart(
            charts["matches_officiated"]
        ),
        use_container_width=True,
    )

with col2:
    st.plotly_chart(
        plot_referee_fouls_chart(
            charts["fouls"]
        ),
        use_container_width=True,
    )

# ---------------------------------------------------------
# OFFICIATING STYLE
# ---------------------------------------------------------

section("Officiating Style")

st.plotly_chart(
    plot_referee_card_comparison_chart(
        charts["card_comparison"]
    ),
    use_container_width=True,
)

# ---------------------------------------------------------
# TOURNAMENT WORKLOAD
# ---------------------------------------------------------

section("Tournament Workload")

st.plotly_chart(
    plot_referee_stage_workload_chart(
        tables["stage_workload"]
    ),
    use_container_width=True,
)

# ---------------------------------------------------------
# RED-CARD INCIDENTS
# ---------------------------------------------------------

section("Red-Card Incidents")

st.dataframe(
    tables["red_cards"],
    use_container_width=True,
    hide_index=True,
)