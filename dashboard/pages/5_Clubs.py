import streamlit as st

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

from dashboard.utils.dashboard_data import (
    get_club_summary,
    get_club_charts,
    get_club_tables,
)
from dashboard.theme.icons import CHART, PLAYER, TROPHY
from dashboard.theme.colors import PRIMARY
from dashboard.theme.css import load_css


load_css()

st.title("Clubs")
st.caption(
    "Club representation, value, performance, and tournament impact"
)


# ---------------------------------------------------------
# DATA
# ---------------------------------------------------------

summary = get_club_summary()
charts = get_club_charts()
tables = get_club_tables()


# ---------------------------------------------------------
# CLUB HIGHLIGHTS
# ---------------------------------------------------------

section("Club Highlights")

most_represented = summary["most_represented"]
most_valuable = summary["most_valuable"]
top_contributor = summary["top_contributor"]


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
        icon=PLAYER,
        icon_color=PRIMARY,
    )

with col2:
    leader_card(
        title="Most Valuable Club",
        name=most_valuable["club_team"],
        subtitle=f'{most_valuable["players_sent"]} players sent',
        value=f'€{most_valuable["total_market_value_eur"]:,.0f}',
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
        icon=CHART,
        icon_color=PRIMARY,
    )


# ---------------------------------------------------------
# CLUB PERFORMANCE
# ---------------------------------------------------------

section("Club Performance")

col1, col2 = two_columns()

with col1:
    st.plotly_chart(
        plot_club_goal_contributions_chart(
            charts["goal_contributions"]
        ),
        use_container_width=True,
    )

with col2:
    st.plotly_chart(
        plot_club_minutes_played_chart(
            charts["minutes_played"]
        ),
        use_container_width=True,
    )


# ---------------------------------------------------------
# CLUB LANDSCAPE
# ---------------------------------------------------------

section("Club Landscape")

col1, col2 = two_columns()

with col1:
    st.plotly_chart(
        plot_club_representation_chart(
            charts["most_representation"]
        ),
        use_container_width=True,
    )

with col2:
    st.plotly_chart(
        plot_club_value_chart(
            charts["valuable"]
        ),
        use_container_width=True,
    )


# ---------------------------------------------------------
# CLUB INTELLIGENCE
# ---------------------------------------------------------

section("Club Intelligence")

col1, col2 = two_columns()

with col1:
    st.subheader("Club Discipline")

    st.dataframe(
        tables["discipline"],
        use_container_width=True,
        hide_index=True,
    )

with col2:
    st.subheader("Club Representation in Medal Teams")

    st.dataframe(
        tables["club_medals"],
        use_container_width=True,
        hide_index=True,
    )