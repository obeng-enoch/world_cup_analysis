import streamlit as st

from dashboard.components.charts import (
    plot_venue_goals_chart,
    plot_venue_elevation_effects_chart,
    _short_stadium_name,
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
from dashboard.theme.icons import FLAME, MAP_PIN, MOUNTAIN
from dashboard.theme.colors import PRIMARY
from dashboard.theme.css import load_css

# load css
load_css()


# load data
summary = get_venue_summary()
charts = get_venue_charts()
tables = get_venue_tables()


# VENUE HIGHLIGHTS

highest_scoring = summary["highest_scoring"]
busiest_venue = summary["busiest_venue"]
highest_elevation = summary["highest_elevation"]

with section("Venue Highlights"):
    col1, col2, col3 = three_columns()

    with col1:
        leader_card(
            title="Highest-Scoring Match",
            name=_short_stadium_name(highest_scoring["stadium_name"]),
            subtitle=highest_scoring["scoreline"],
            value=f'{highest_scoring["total_goals"]} goals',
            icon=FLAME,
            icon_color=PRIMARY,
        )

    with col2:
        leader_card(
            title="Busiest Venue",
            name=_short_stadium_name(busiest_venue["stadium_name"]),
            subtitle=busiest_venue["city"],
            value=f'{busiest_venue["matches_hosted"]} matches',
            icon=MAP_PIN,
            icon_color=PRIMARY,
        )

    with col3:
        leader_card(
            title="Highest-Elevation Venue",
            name=_short_stadium_name(highest_elevation["stadium_name"]),
            subtitle=highest_elevation["city"],
            value=f'{highest_elevation["elevation_meters"]:,} m',
            icon=MOUNTAIN,
            icon_color=PRIMARY,
        )


# VENUE PERFORMANCE

left, right = two_columns(ratio=(3, 2))

with left:
    with st.container(border=True):
        st.caption("Venue Performance in Terms of Goals")
        st.plotly_chart(
            plot_venue_goals_chart(charts["goals_per_venue"]),
            width="stretch",
        )

with right:
    with st.container(border=True):
        st.caption("Avg Goals/Match by Each Elevation")
        st.plotly_chart(
            plot_venue_elevation_effects_chart(charts["elevation_accuracy"]),
            width="stretch",
        )


# MATCH-DAY STYLE & STAGE WORKLOAD (tables)

STAGE_ORDER = [
    "Group Stage",
    "Round of 32",
    "Round of 16",
    "Quarter-finals",
    "Semi-finals",
    "Third-place match",
    "Final",
]

col1, col2 = two_columns()

with col1:
    with st.container(border=True):
        st.caption("Average corners, fouls & offsides per stadium")

        style_table = charts["match_day_style"].copy()
        style_table["stadium_name"] = style_table["stadium_name"].apply(_short_stadium_name)
        style_table = style_table.sort_values("avg_corners", ascending=False)
        style_table = style_table.rename(columns={
            "matches_played": "Matches",
            "avg_possession_pct": "Avg Possession",
            "stadium_name": "Stadium",
            "avg_corners": "Avg Corners",
            "avg_fouls": "Avg Fouls",
            "avg_offsides": "Avg Offsides",
        })

        st.dataframe(
            style_table,
            hide_index=True,
            width="stretch",
            height=180,
            column_config={
                "Avg Corners": st.column_config.NumberColumn(format="%.2f"),
                "Avg Fouls": st.column_config.NumberColumn(format="%.2f"),
                "Avg Offsides": st.column_config.NumberColumn(format="%.2f"),
            },
        )

with col2:
    with st.container(border=True):
        st.caption("Venue Directory")
        directory = tables["directory"].copy()
        directory["stadium_name"] = directory["stadium_name"].apply(_short_stadium_name)
        directory = directory.rename(columns={
            "stadium_name": "Stadium",
            "city": "City",
            "country": "Country",
            "capacity": "Capacity",
            "elevation_meters": "Elevation Meters"
        })
        st.dataframe(
            directory,
            hide_index=True,
            width="stretch",
            height=180,
        )


with st.container(border=True):
    st.caption("Matches hosted by stage")

    stage_table = charts["stage_distribution"].copy()
    stage_table["stadium_name"] = stage_table["stadium_name"].apply(_short_stadium_name)

    pivoted = stage_table.pivot_table(
        index="stadium_name",
        columns="stage",
        values="matches_hosted",
        aggfunc="sum",
        fill_value=0,
    )
    pivoted = pivoted.reindex(columns=[s for s in STAGE_ORDER if s in pivoted.columns])
    pivoted["Total"] = pivoted.sum(axis=1)
    pivoted = pivoted.sort_values("Total", ascending=False).reset_index()
    pivoted = pivoted.rename(columns={"stadium_name": "Stadium"})

    st.dataframe(
        pivoted,
        hide_index=True,
        width="stretch",
        height=180,
    )