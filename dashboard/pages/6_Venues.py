import streamlit as st

from dashboard.components.charts import (
    plot_venue_goals_chart,
    plot_venue_match_day_style_chart,
    plot_venue_elevation_effects_chart,
    plot_venue_stage_distribution_chart,
)
from dashboard.components.leader import leader_card
from dashboard.layout import (
    section,
    three_columns,
    two_columns,
)
from dashboard.utils.dashboard_data import (
    get_venue_summary,
    get_venue_charts,
    get_venue_tables,
)
from dashboard.theme.icons import CHART, TROPHY, VENUE
from dashboard.theme.colors import PRIMARY
from dashboard.theme.css import load_css


load_css()


# ---------------------------------------------------------
# PAGE HEADER
# ---------------------------------------------------------

st.title("Venues")
st.caption(
    "Venue capacity, match load, scoring patterns, elevation, "
    "and tournament activity"
)


# ---------------------------------------------------------
# DATA
# ---------------------------------------------------------

summary = get_venue_summary()
charts = get_venue_charts()
tables = get_venue_tables()


# ---------------------------------------------------------
# VENUE HIGHLIGHTS
# ---------------------------------------------------------

section("Venue Highlights")

highest_scoring = summary["highest_scoring"]
busiest_venue = summary["busiest_venue"]
highest_elevation = summary["highest_elevation"]


col1, col2, col3 = three_columns()

with col1:
    leader_card(
        title="Highest-Scoring Match",
        name=highest_scoring["stadium_name"],
        subtitle=highest_scoring["scoreline"],
        value=f'{highest_scoring["total_goals"]} goals',
        icon=CHART,
        icon_color=PRIMARY,
    )

with col2:
    leader_card(
        title="Busiest Venue",
        name=busiest_venue["stadium_name"],
        subtitle=busiest_venue["city"],
        value=f'{busiest_venue["matches_hosted"]} matches',
        icon=VENUE,
        icon_color=PRIMARY,
    )

with col3:
    leader_card(
        title="Highest-Elevation Venue",
        name=highest_elevation["stadium_name"],
        subtitle=highest_elevation["city"],
        value=f'{highest_elevation["elevation_meters"]:,} m',
        icon=TROPHY,
        icon_color=PRIMARY,
    )


# ---------------------------------------------------------
# VENUE PERFORMANCE
# ---------------------------------------------------------

section("Venue Performance")

col1, col2 = two_columns()

with col1:
    st.plotly_chart(
        plot_venue_goals_chart(
            charts["goals_per_venue"]
        ),
        use_container_width=True,
    )

with col2:
    st.plotly_chart(
        plot_venue_match_day_style_chart(
            charts["match_day_style"]
        ),
        use_container_width=True,
    )


# ---------------------------------------------------------
# ELEVATION & TOURNAMENT LOAD
# ---------------------------------------------------------

section("Elevation & Tournament Load")

col1, col2 = two_columns()

with col1:
    st.plotly_chart(
        plot_venue_elevation_effects_chart(
            charts["elevation_accuracy"]
        ),
        use_container_width=True,
    )

with col2:
    st.plotly_chart(
        plot_venue_stage_distribution_chart(
            charts["stage_distribution"]
        ),
        use_container_width=True,
    )


# ---------------------------------------------------------
# VENUE DIRECTORY
# ---------------------------------------------------------

section("Venue Directory")

st.dataframe(
    tables["directory"],
    use_container_width=True,
    hide_index=True,
)


# ---------------------------------------------------------
# VENUE DETAILS
# ---------------------------------------------------------

section("Venue Details")

col1, col2 = two_columns()

with col1:
    st.subheader("Highest-Scoring Matches")

    st.dataframe(
        tables["highest_scoring"],
        use_container_width=True,
        hide_index=True,
    )

with col2:
    st.subheader("Venue Elevation Ranking")

    st.dataframe(
        tables["elevation_ranked"],
        use_container_width=True,
        hide_index=True,
    )