from dashboard.components.charts import (
    plot_goal_timing_chart,
    plot_match_result_distribution_chart,
    plot_stage_goals_chart,
)
from dashboard.components.leader import leader_card
from dashboard.layout import (
    section,
    three_columns,
    two_columns,
)
from dashboard.theme.css import load_css
from dashboard.utils.dashboard_data import (
    get_match_summary,
    get_match_charts,
    get_match_tables,
    get_goals_per_stage_chart,
)

from dashboard.theme.icons import  FLAME, TROPHY, ZAP
from dashboard.components.headings import section_heading

import streamlit as st


# Load CSS
load_css()


# Load data
summary = get_match_summary()
charts = get_match_charts()
tables = get_match_tables()
goals_by_stage = get_goals_per_stage_chart()


# Match Highlights
with section("Match Highlights"):
    col1, col2, col3 = three_columns()

    with col1:
        highest_scoring = summary["highest_scoring"]
        leader_card(
            "Highest Scoring Match",
            highest_scoring["match"],
            highest_scoring["stage"],
            f'{highest_scoring["total_goals"]} goals',
            FLAME,
        )

    with col2:
        biggest_win = summary["biggest_wins"]

        leader_card(
            "Biggest Win",
            biggest_win["match"],
            biggest_win["stage"],
            f'{biggest_win["goal_difference"]}-goal margin',
            TROPHY,
        )

    with col3:
        biggest_upset = summary["biggest_upsets"]
        leader_card(
            "Biggest Upset",
            biggest_upset["match"],
            biggest_upset["stage"],
            f'{biggest_upset["ranking_gap"]}-place ranking gap',
            ZAP,
        )

# Match Trends
col1, col2, col3 = three_columns()

with col1:
    with st.container(border=True):
        chart_title_col, control_col = st.columns([3, 2])
        with chart_title_col:
            st.caption("Goals Scored in Each Stage")

        with control_col:
            selected_measure = st.segmented_control(
                "Chart measure",
                options=["Total goals", "Goals per match"],
                default="Total goals",
                key="stage_measure",
                label_visibility="collapsed",
            )

        if selected_measure == "Total goals":
            value_column = "total_goals"
            value_label = "Total goals"
        else:
            value_column = "avg_goals_per_match"
            value_label = "Goals per match"

        st.plotly_chart(
            plot_stage_goals_chart(
                goals_by_stage,
                value_column=value_column,
                value_label=value_label,
                height=145,
            ),
            width="stretch",
        )

with col2:
    with st.container(border=True):
        st.caption("Goals Timing")
        st.plotly_chart(
            plot_goal_timing_chart(
                charts["goal_timing"]
            ),
            width="stretch",
        )

with col3:
    with st.container(border=True):
        st.caption("Match Results")
        st.plotly_chart(
            plot_match_result_distribution_chart(
                charts["match_result_distribution"]
            ),
            width="stretch",
        )

# Detailed Match Analysis
col1, col2 = two_columns()

with col1:
    with st.container(border=True):
        st.caption("Match Results")
        st.dataframe(
            tables["match_results"].rename(columns={
                "match": "Scoreline",
                "match_date": "Date",
                "stage": "Stage",
                "stadium_name": "Stadium",
                "city": "City",
            }),
            hide_index=True,
            width="stretch",
            height=180,
        )

with col2:
    with st.container(border=True):
        st.caption("Possession Dominance")
        st.dataframe(
            tables["possession"].rename(columns={
                "match": "Scoreline",
                "possession": "Possession",
                "possession_gap": "Possession Gap",
            }),
            hide_index=True,
            width="stretch",
            height=180,
        )