from typing import Optional

import plotly.express as px
import plotly.graph_objects as go

import pandas as pd
import re
from dashboard.theme.constants import (
    CHART_HEIGHT_THREE_COLUMN,
    CHART_HEIGHT_TWO_COLUMN,
)

from dashboard.theme.colors import (
    ACCENT,
    GRID,
    PRIMARY,
    SECONDARY,
    TEXT_PRIMARY,
    TEXT_SECONDARY,
)

DEFAULT_HEIGHT = CHART_HEIGHT_THREE_COLUMN

DEFAULT_TEMPLATE = "plotly_white"

def _wrap_axis_label(label: str, max_words_per_line: int = 2) -> str:
    """
    Wrap long axis labels onto multiple lines.

    Plotly supports HTML line breaks (<br>) in axis labels,
    which improves readability without truncating names.
    """

    words = str(label).split()

    if len(words) <= max_words_per_line:
        return label

    lines = []

    for i in range(0, len(words), max_words_per_line):
        lines.append(" ".join(words[i:i + max_words_per_line]))

    return "<br>".join(lines)

def _short_stadium_name(name: str) -> str:
    """Extract the parenthetical stadium name for compact display
    (e.g. 'Monterrey Stadium (Estadio BBVA)' -> 'Estadio BBVA'),
    falling back to the full name if there's no parenthetical."""
    match = re.search(r"\(([^)]+)\)", name)
    return match.group(1) if match else name

def _style_chart(
    fig: go.Figure,
    *,
    title: Optional[str] = None,
    height: int = DEFAULT_HEIGHT,
    show_legend: bool = False,
) -> go.Figure:
    """Apply a consistent style to all dashboard charts."""

    fig.update_layout(
        template=DEFAULT_TEMPLATE,
        title=title,
        height=height,
        showlegend=show_legend,
        margin=dict(l=20, r=20, t=60, b=20),
        title_x=0.02,
        legend_title_text="",
        hovermode="x unified"
    )

    return fig

def _style_dashboard_chart(
    fig: go.Figure,
    *,
    height: int,
    show_legend: bool = True,
) -> go.Figure:
    fig.update_layout(
        template="none",
        height=height,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(
            l=12,
            r=12,
            t=28 if show_legend else 20,
            b=28,
        ),
        font=dict(
            family="'Inter', 'Segoe UI', sans-serif",
            color=TEXT_PRIMARY,
            size=11,
        ),
        showlegend=show_legend,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
        ),
        hoverlabel=dict(
            bgcolor="#1B2027",
            bordercolor=PRIMARY,
            font_color=TEXT_PRIMARY,
        ),
    )
    fig.update_xaxes(automargin=True)
    fig.update_yaxes(automargin=True)

    return fig

def plot_bar_chart(
    data: pd.DataFrame,
    *,
    x: str,
    y: str,
    title: str,
    x_title: Optional[str] = None,
    y_title: Optional[str] = None,
    show_values: bool = True,
    height: int = DEFAULT_HEIGHT,
) -> go.Figure:

    fig = px.bar(
        data,
        x=x,
        y=y,
        title=title,
    )

    fig.update_xaxes(title=x_title)
    fig.update_yaxes(title=y_title)

    if show_values:
        fig.update_traces(texttemplate="%{y}", textposition="outside")

    return _style_chart(
        fig,
        title=title,
        height=height,
    )


def plot_horizontal_bar_chart(
    data: pd.DataFrame,
    *,
    x: str,
    y: str,
    title: str,
    x_title: Optional[str] = None,
    y_title: Optional[str] = None,
    show_values: bool = True,
    height: int = DEFAULT_HEIGHT,
) -> go.Figure:

    fig = px.bar(
        data,
        x=x,
        y=y,
        orientation="h",
        title=title,
    )

    fig.update_xaxes(title=x_title)
    fig.update_yaxes(title=y_title)

    if show_values:
        fig.update_traces(texttemplate="%{x}", textposition="outside")

    return _style_chart(
        fig,
        title=title,
        height=height,
    )

def plot_line_chart(
    data: pd.DataFrame,
    *,
    x: str,
    y: str,
    title: str,
    x_title: Optional[str] = None,
    y_title: Optional[str] = None,
    height: int = DEFAULT_HEIGHT,
) -> go.Figure:
    """
    Create a line chart.
    """

    fig = px.line(
        data,
        x=x,
        y=y,
        title=title,
        markers=True,
    )

    fig.update_xaxes(title=x_title)
    fig.update_yaxes(title=y_title)

    return _style_chart(
        fig,
        title=title,
        height=height,
    )

def plot_pie_chart(
    data: pd.DataFrame,
    *,
    names: str,
    values: str,
    title: str,
    height: int = DEFAULT_HEIGHT,
) -> go.Figure:
    """
    Create a pie chart.
    """

    fig = px.pie(
        data,
        names=names,
        values=values,
        title=title,
    )

    fig.update_traces(textinfo="percent+label")

    return _style_chart(
        fig,
        title=title,
        height=height,
        show_legend=True,
    )

def plot_event_counts_chart(
    data: pd.DataFrame,
    height: int = CHART_HEIGHT_TWO_COLUMN,
) -> go.Figure:
    """Interactive event frequency chart for the tournament overview"""

    chart_data = data.sort_values(
        "avg_events_per_match",
        ascending=True,
    )

    fig = px.bar(
        chart_data,
        x="avg_events_per_match",
        y="event_type",
        orientation="h",
        custom_data=["total_events"],
    )

    fig.update_traces(
        marker=dict(
            color=PRIMARY,
            line=dict(width=0),
        ),
        hovertemplate=(
            "<b>%{y}</b><br>"
            "Average per match: <b>%{x:.2f}</b><br>"
            "Total events: %{customdata[0]}<extra></extra>"
        ),
    )

    _style_dashboard_chart(
        fig,
        height=height,
        show_legend=False,
    )

    fig.update_xaxes(
        title="Average events per match",
        title_standoff=10,
        showgrid=True,
        gridcolor=GRID,
        zeroline=False,
        showline=False,
        automargin=True,
        nticks=5,
        tickformat=".1f",
        tickfont=dict(
            color=TEXT_SECONDARY,
            size=11,
        ),
  
    )

    fig.update_yaxes(
        title=None,
        showgrid=False,
        zeroline=False,
        showline=False,
        automargin=True,
        tickfont=dict(
            color=TEXT_SECONDARY,
            size=11,
        ),
    )

    return fig

def plot_stage_goals_chart(
    data: pd.DataFrame,
    value_column: str,
    value_label: str,
    height: int = CHART_HEIGHT_THREE_COLUMN,
) -> go.Figure:
    """Interactive goals-by-stage chart for the tournament overview."""

    bar_colors = [
        ACCENT if stage == "Final" else PRIMARY
        for stage in data["stage"]
    ]

    fig = go.Figure(
        go.Bar(
            x=data["stage"],
            y=data[value_column],
            marker=dict(
                color=bar_colors,
                line=dict(width=0),
            ),
            text=data[value_column],
            texttemplate="<b>%{text}</b>",
            textposition="outside",
            textfont=dict(color=TEXT_PRIMARY, size=12),
            customdata=data[["matches_played", "avg_goals_per_match"]],
            hovertemplate=(
                "<b>%{x}</b><br>"
                f"{value_label}: <b>%{{y}}</b><br>"
                "Matches played: %{customdata[0]}<br>"
                "Goals per match: %{customdata[1]}"
                "<extra></extra>"
            ),
            cliponaxis=False,
        )
    )

    _style_dashboard_chart(
        fig,
        height=height,
        show_legend=False,
    )

    stage_labels = {
        "Group Stage": "Group<br>stage",
        "Round of 32": "Round of<br>32",
        "Round of 16": "Round of<br>16",
        "Quarter-finals": "Quarter-<br>finals",
        "Semi-finals": "Semi-<br>finals",
        "Third-place match": "Third-place<br>match",
        "Final": "Final",
    }

    fig.update_xaxes(
        showgrid=False,
        showline=False,
        tickmode="array",
        tickvals=data["stage"].tolist(),
        ticktext=[
            stage_labels.get(stage, stage)
            for stage in data["stage"]
        ],
        tickangle=0,
        automargin=True,
        tickfont=dict(color=TEXT_SECONDARY, size=9),
    )

    fig.update_yaxes(
        title=value_label,
        title_standoff=10,
        showgrid=True,
        gridcolor=GRID,
        zeroline=False,
        showline=False,
        automargin=True,
        nticks=5,
        tickformat=",",
        tickfont=dict(color=TEXT_SECONDARY, size=11),
        range=[0, data[value_column].max() * 1.20],
    )

    return fig

def plot_goal_timing_chart(
    data: pd.DataFrame,
    height: int = CHART_HEIGHT_THREE_COLUMN,
) -> go.Figure:
    """Interactive goal-timing distribution chart."""

    time_order = [
        "0-15",
        "16-30",
        "31-45",
        "46-60",
        "61-75",
        "76-90",
        "90+",
    ]

    chart_data = data.copy()
    chart_data["time_window"] = pd.Categorical(
        chart_data["time_window"],
        categories=time_order,
        ordered=True,
    )
    chart_data = chart_data.sort_values("time_window")

    fig = go.Figure(
        go.Bar(
            x=chart_data["time_window"],
            y=chart_data["goals"],
            marker=dict(
                color=PRIMARY,
                line=dict(width=0),
            ),
            text=chart_data["goals"],
            texttemplate="<b>%{text}</b>",
            textposition="outside",
            textfont=dict(color=TEXT_PRIMARY, size=12),
            hovertemplate=(
                "<b>%{x} minutes</b><br>"
                "Goals: <b>%{y}</b><extra></extra>"
            ),
            cliponaxis=False,
        )
    )

    _style_dashboard_chart(
        fig,
        height=height,
        show_legend=False,
    )

    fig.update_xaxes(
        title="Minutes Range",
        showgrid=False,
        showline=False,
        automargin=True,
        tickfont=dict(color=TEXT_SECONDARY, size=11),

    )

    fig.update_yaxes(
        title="Goals Scored",
        showgrid=True,
        gridcolor=GRID,
        zeroline=False,
        showline=False,
        automargin=True,
        nticks=5,
        tickformat=",",
        tickfont=dict(color=TEXT_SECONDARY, size=11),
        range=[0, chart_data["goals"].max() * 1.20],
    )

    return fig

def plot_match_result_distribution_chart(
    data: pd.DataFrame,
    height: int = CHART_HEIGHT_THREE_COLUMN,
) -> go.Figure:
    """Interactive match-result distribution donut chart."""

    total_matches = data["matches"].sum()

    fig = px.pie(
        data,
        names="result_type",
        values="matches",
        hole=0.65,
        color_discrete_sequence=[PRIMARY, ACCENT, "#2E7D32", "#C62828"],
    )

    fig.update_traces(
        textposition="outside",
        textinfo="percent",
        textfont=dict(color=TEXT_PRIMARY, size=11),
        hovertemplate=(
            "<b>%{label}</b><br>"
            "Matches: <b>%{value}</b><br>"
            "Share: %{percent}<extra></extra>"
        ),
    )

    fig.add_annotation(
        text=(
            f"<b>{total_matches}</b>"
            "<br><span style='font-size:12px'>Matches</span>"
        ),
        x=0.5,
        y=0.5,
        showarrow=False,
        font=dict(color=TEXT_PRIMARY),
    )

    _style_dashboard_chart(
        fig,
        height=height,
        show_legend=True,
    )



    fig.update_layout(
        margin=dict(t=1, b=10),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.25,
            xanchor="center",
            x=0.5,
            font=dict(color=TEXT_SECONDARY, size=11),
        ),
    )

    return fig

def plot_goals_by_team_chart(
    data: pd.DataFrame,
    height: int = CHART_HEIGHT_THREE_COLUMN,
) -> go.Figure:
    """Interactive goals-by-team chart for the teams overview."""

    chart_data = data.sort_values("goals", ascending=False)

    fig = go.Figure(
        go.Bar(
            x=chart_data["team"],
            y=chart_data["goals"],
            marker=dict(
                color=PRIMARY,
                line=dict(width=0),
            ),
            text=chart_data["goals"],
            texttemplate="<b>%{text}</b>",
            textposition="outside",
            textfont=dict(color=TEXT_PRIMARY, size=12),
            customdata=chart_data[
                ["matches_played", "goals_per_match", "shots", "shots_on_target"]
            ],
            hovertemplate=(
                "<b>%{x}</b><br>"
                "Goals: <b>%{y}</b><br>"
                "Matches played: %{customdata[0]}<br>"
                "Goals per match: %{customdata[1]}<br>"
                "Shots: %{customdata[2]}<br>"
                "Shots on target: %{customdata[3]}"
                "<extra></extra>"
            ),
            cliponaxis=False,
        )
    )

    _style_dashboard_chart(
        fig,
        height=height,
        show_legend=False,
    )

    fig.update_xaxes(
        title="Team",
        showgrid=False,
        showline=False,
        tickmode="array",
        tickvals=chart_data["team"].tolist(),
        ticktext=[_wrap_axis_label(team) for team in chart_data["team"]],
        automargin=True,
        tickfont=dict(color=TEXT_SECONDARY, size=11),
    )

    fig.update_yaxes(
        title="Goals scored",
        title_standoff=10,
        showgrid=True,
        gridcolor=GRID,
        zeroline=False,
        showline=False,
        automargin=True,
        nticks=5,
        tickformat=",",
        tickfont=dict(color=TEXT_SECONDARY, size=11),
        range=[0, chart_data["goals"].max() * 1.20],
    )

    return fig

def plot_best_defense_chart(
    data: pd.DataFrame,
    height: int = CHART_HEIGHT_THREE_COLUMN,
) -> go.Figure:
    """Interactive best-defense (clean sheets) chart for the teams overview."""

    chart_data = data.sort_values("clean_sheets", ascending=False)

    fig = go.Figure(
        go.Bar(
            x=chart_data["team"],
            y=chart_data["clean_sheets"],
            marker=dict(
                color=PRIMARY,
                line=dict(width=0),
            ),
            text=chart_data["clean_sheets"],
            texttemplate="<b>%{text}</b>",
            textposition="outside",
            textfont=dict(color=TEXT_PRIMARY, size=12),
            customdata=chart_data[
                ["goals_against", "matches_played", "goals_conceded_per_match"]
            ],
            hovertemplate=(
                "<b>%{x}</b><br>"
                "Clean sheets: <b>%{y}</b><br>"
                "Goals against: %{customdata[0]}<br>"
                "Matches played: %{customdata[1]}<br>"
                "Goals conceded per match: %{customdata[2]:.2f}"
                "<extra></extra>"
            ),
            cliponaxis=False,
        )
    )

    _style_dashboard_chart(
        fig,
        height=height,
        show_legend=False,
    )

    fig.update_xaxes(
        title="Team",
        showgrid=False,
        showline=False,
        tickmode="array",
        tickvals=chart_data["team"].tolist(),
        ticktext=[_wrap_axis_label(team) for team in chart_data["team"]],
        automargin=True,
        tickfont=dict(color=TEXT_SECONDARY, size=11),
    )

    fig.update_yaxes(
        title="Clean sheets",
        title_standoff=10,
        showgrid=True,
        gridcolor=GRID,
        zeroline=False,
        showline=False,
        automargin=True,
        nticks=5,
        tickformat=",",
        tickfont=dict(color=TEXT_SECONDARY, size=11),
        range=[0, chart_data["clean_sheets"].max() * 1.20],
    )

    return fig

def plot_man_of_the_match_teams(
    data: pd.DataFrame,
    height: int = CHART_HEIGHT_THREE_COLUMN,
) -> go.Figure:
    """Interactive performance (MOTM Awards) chart for the teams overview."""

    chart_data = data.sort_values("man_of_the_match_awards", ascending=False)

    fig = go.Figure(
        go.Bar(
            x=chart_data["team"],
            y=chart_data["man_of_the_match_awards"],
            marker=dict(
                color=PRIMARY,
                line=dict(width=0),
            ),
            text=chart_data["man_of_the_match_awards"],
            texttemplate="<b>%{text}</b>",
            textposition="outside",
            textfont=dict(color=TEXT_PRIMARY, size=12),
            customdata=chart_data[
                ["winning_players"]
            ],
            hovertemplate=(
                "<b>%{x}</b><br>"
                "Man of the Match awards: <b>%{y}</b><br>"
                "Award-winning players: %{customdata[0]}<br>"
                "<extra></extra>"
            ),
            cliponaxis=False,
        )
    )

    _style_dashboard_chart(
        fig,
        height=height,
        show_legend=False,
    )

    fig.update_xaxes(
        title="Team",
        showgrid=False,
        showline=False,
        tickmode="array",
        tickvals=chart_data["team"].tolist(),
        ticktext=[_wrap_axis_label(team) for team in chart_data["team"]],
        automargin=True,
        tickfont=dict(color=TEXT_SECONDARY, size=11),
    )

    fig.update_yaxes(
        title="MOTM Awards",
        title_standoff=10,
        showgrid=True,
        gridcolor=GRID,
        zeroline=False,
        showline=False,
        automargin=True,
        nticks=5,
        tickformat=",",
        tickfont=dict(color=TEXT_SECONDARY, size=11),
        range=[0, chart_data["man_of_the_match_awards"].max() * 1.20],
    )

    return fig

def plot_goal_contributions_chart(
    data: pd.DataFrame,
    *,
    height: int = CHART_HEIGHT_THREE_COLUMN,
) -> go.Figure:
    """
    Stacked horizontal bar chart showing the Top 5 players
    by total goal contributions (Goals + Assists).
    """

    
    # Prepare Data
    chart_data = (
        data.head(5)
        .sort_values("goal_contributions", ascending=True)
        .copy()
    )

    chart_data["player"] = (
        chart_data["player_name"]
        .apply(_wrap_axis_label)
    )

    # Build Figure
    fig = go.Figure()

    # Goals
    fig.add_trace(
        go.Bar(
            x=chart_data["goals"],
            y=chart_data["player"],
            orientation="h",
            name="Goals",
            marker=dict(color=PRIMARY),
            customdata=chart_data[
                [
                    "assists",
                    "goal_contributions",
                    "matches_played",
                    "minutes_played",
                ]
            ],
            hovertemplate=(
                "<b>%{y}</b><br>"
                "Team: %{customdata[0]}<br>"
                "Goals: <b>%{x}</b><br>"
                "Assists: %{customdata[0]}<br>"
                "Goal Contributions: %{customdata[1]}<br>"
                "Matches: %{customdata[2]}<br>"
                "Minutes: %{customdata[3]}"
                "<extra></extra>"
            ),
        )
    )

    # Assists
    fig.add_trace(
        go.Bar(
            x=chart_data["assists"],
            y=chart_data["player"],
            orientation="h",
            name="Assists",
            marker=dict(color=ACCENT),
            customdata=chart_data[
                [
                    "goals",
                    "goal_contributions",
                    "matches_played",
                    "minutes_played",
                ]
            ],
            hovertemplate=(
                "<b>%{y}</b><br>"
                "Assists: <b>%{x}</b><br>"
                "Goals: %{customdata[0]}<br>"
                "Goal Contributions: %{customdata[1]}<br>"
                "Matches: %{customdata[2]}<br>"
                "Minutes: %{customdata[3]}"
                "<extra></extra>"
            ),
        )
    )

    # Layout
    _style_dashboard_chart(
        fig,
        height=height,
        show_legend=True,
    )

    fig.update_layout(
        barmode="stack",
    )

    fig.update_xaxes(
        title="Goal Contributions",
        showgrid=True,
        gridcolor=GRID,
        zeroline=False,
        showline=False,
        tickfont=dict(
            color=TEXT_SECONDARY,
            size=11,
        ),
   
    )

    fig.update_yaxes(
        showgrid=False,
        tickfont=dict(
            color=TEXT_PRIMARY,
            size=10,
        ),
    )

    return fig

def plot_man_of_the_match_players(
    data: pd.DataFrame,
    height: int = CHART_HEIGHT_THREE_COLUMN,
) -> go.Figure:
    """Horizontal bar chart showing the top 5 MOMT Awards winners."""

    chart_data = (
        data.head(5)
        .sort_values("man_of_the_match_awards", ascending=True)
        .copy()
    )

    chart_data["player"] = chart_data["player_name"].apply(_wrap_axis_label)

    fig = go.Figure(
        go.Bar(
            x=chart_data["man_of_the_match_awards"],
            y=chart_data["player"],
            orientation="h",
            marker=dict(
                color=PRIMARY,
                line=dict(width=0),
            ),
            text=chart_data["man_of_the_match_awards"],
            texttemplate="<b>%{text}</b>",
            textposition="outside",
            textfont=dict(color=TEXT_PRIMARY, size=12),
            customdata=chart_data[
                ["player"]
            ],
            hovertemplate=(
                "<b>%{y}</b><br>"
                "Team: %{customdata[0]}<br>"
                "<extra></extra>"
            ),
            cliponaxis=False,
        )
    )

    _style_dashboard_chart(
        fig,
        height=height,
        show_legend=False,
    )

    fig.update_xaxes(
        title="MOTM Awards",
        title_standoff=10,
        showgrid=True,
        gridcolor=GRID,
        zeroline=False,
        showline=False,
        automargin=True,
        nticks=5,
        tickformat=",",
        tickfont=dict(color=TEXT_SECONDARY, size=11),
    )

    fig.update_yaxes(
        title=None,
        showgrid=False,
        zeroline=False,
        showline=False,
        automargin=True,
        tickfont=dict(color=TEXT_PRIMARY, size=11),
    )

    return fig

def plot_goalkeeper_saves_chart(
    data: pd.DataFrame,
    height: int = CHART_HEIGHT_THREE_COLUMN,
) -> go.Figure:
    """Horizontal bar chart showing the top 5 goalkeepers by saves."""

    chart_data = (
        data.head(5)
        .sort_values("saves", ascending=True)
        .copy()
    )

    chart_data["player"] = chart_data["player_name"].apply(_wrap_axis_label)

    fig = go.Figure(
        go.Bar(
            x=chart_data["saves"],
            y=chart_data["player"],
            orientation="h",
            marker=dict(
                color=PRIMARY,
                line=dict(width=0),
            ),
            text=chart_data["saves"],
            texttemplate="<b>%{text}</b>",
            textposition="outside",
            textfont=dict(color=TEXT_PRIMARY, size=12),
            customdata=chart_data[
                ["team", "clean_sheets", "goals_conceded", "matches_played"]
            ],
            hovertemplate=(
                "<b>%{y}</b><br>"
                "Team: %{customdata[0]}<br>"
                "Saves: <b>%{x}</b><br>"
                "Clean sheets: %{customdata[1]}<br>"
                "Goals conceded: %{customdata[2]}<br>"
                "Matches played: %{customdata[3]}"
                "<extra></extra>"
            ),
            cliponaxis=False,
        )
    )

    _style_dashboard_chart(
        fig,
        height=height,
        show_legend=False,
    )

    fig.update_xaxes(
        title="Saves",
        title_standoff=10,
        showgrid=True,
        gridcolor=GRID,
        zeroline=False,
        showline=False,
        automargin=True,
        nticks=5,
        tickformat=",",
        tickfont=dict(color=TEXT_SECONDARY, size=11),
    )

    fig.update_yaxes(
        title=None,
        showgrid=False,
        zeroline=False,
        showline=False,
        automargin=True,
        tickfont=dict(color=TEXT_PRIMARY, size=11),
    )

    return fig

def plot_club_representation_chart(
    data: pd.DataFrame,
    *,
    height: int = CHART_HEIGHT_THREE_COLUMN,
) -> go.Figure:
    """
    Horizontal bar chart showing clubs with the most
    players represented at the tournament.
    """

    chart_data = (
        data.head(5)
        .sort_values("players_sent", ascending=True)
        .copy()
    )

    chart_data["club"] = (
        chart_data["club_team"]
        .apply(_wrap_axis_label)
    )

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=chart_data["players_sent"],
            y=chart_data["club"],
            orientation="h",
            marker=dict(color=PRIMARY),
            text=chart_data["players_sent"],
            texttemplate="<b>%{text}</b>",
            textposition="outside",
            cliponaxis=False,
            customdata=chart_data["countries_represented"],
            hovertemplate=(
                "<b>%{y}</b><br>"
                "Players Represented: <b>%{x}</b><br>"
                "Countries Represented: %{customdata}"
                "<extra></extra>"
            ),
        )
    )

    _style_dashboard_chart(
        fig,
        height=height,
        show_legend=False,
    )

    fig.update_xaxes(
        title="Players Represented",
        showgrid=True,
        gridcolor=GRID,
        zeroline=False,
        showline=False,
        tickfont=dict(
            color=TEXT_SECONDARY,
            size=11,
        ),
    )

    fig.update_yaxes(
        showgrid=False,
        tickfont=dict(
            color=TEXT_PRIMARY,
            size=11,
        ),
    )

    return fig

def plot_club_minutes_played_chart(
    data: pd.DataFrame,
    *,
    height: int = CHART_HEIGHT_THREE_COLUMN,
) -> go.Figure:
    """
    Horizontal bar chart showing clubs by total minutes played.
    """

    chart_data = (
        data.head(5)
        .sort_values("total_minutes_played", ascending=True)
        .copy()
    )

    chart_data["club"] = (
        chart_data["club_team"]
        .apply(_wrap_axis_label)
    )

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=chart_data["total_minutes_played"],
            y=chart_data["club"],
            orientation="h",
            marker=dict(color=PRIMARY),
            text=chart_data["total_minutes_played"],
            texttemplate="<b>%{text}</b>",
            textposition="outside",
            cliponaxis=False,
            customdata=chart_data[
                [
                    "players_sent",
                    "avg_minutes_per_player",
                ]
            ],
            hovertemplate=(
                "<b>%{y}</b><br>"
                "Total Minutes: <b>%{x:,.0f}</b><br>"
                "Players Sent: %{customdata[0]}<br>"
                "Average Minutes / Player: %{customdata[1]:,.2f}"
                "<extra></extra>"
            ),
        )
    )

    _style_dashboard_chart(
        fig,
        height=height,
        show_legend=False,
    )

    fig.update_xaxes(
        title="Minutes Played",
        showgrid=True,
        gridcolor=GRID,
        zeroline=False,
        showline=False,
        tickfont=dict(
            color=TEXT_SECONDARY,
            size=11,
        ),
    )

    fig.update_yaxes(
        showgrid=False,
        tickfont=dict(
            color=TEXT_PRIMARY,
            size=11,
        ),
    )

    return fig

def plot_club_goal_contributions_chart(
    data: pd.DataFrame,
    height: int = CHART_HEIGHT_THREE_COLUMN,
) -> go.Figure:
    """Horizontal bar chart showing the top clubs by total goal contributions."""

    chart_data = (
        data.head(5)
        .sort_values("goal_contributions", ascending=True)
        .copy()
    )

    chart_data["club"] = chart_data["club_team"].apply(_wrap_axis_label)

    fig = go.Figure(
        go.Bar(
            x=chart_data["goal_contributions"],
            y=chart_data["club"],
            orientation="h",
            marker=dict(
                color=PRIMARY,
                line=dict(width=0),
            ),
            text=chart_data["goal_contributions"],
            texttemplate="<b>%{text}</b>",
            textposition="outside",
            textfont=dict(color=TEXT_PRIMARY, size=12),
            customdata=chart_data[["goals", "assists", "players_sent"]],
            hovertemplate=(
                "<b>%{y}</b><br>"
                "Goal contributions: <b>%{x}</b><br>"
                "Goals: %{customdata[0]}<br>"
                "Assists: %{customdata[1]}<br>"
                "Players sent: %{customdata[2]}"
                "<extra></extra>"
            ),
            cliponaxis=False,
        )
    )

    _style_dashboard_chart(
        fig,
        height=height,
        show_legend=False,
    )

    fig.update_xaxes(
        title="Goal contributions",
        title_standoff=10,
        showgrid=True,
        gridcolor=GRID,
        zeroline=False,
        showline=False,
        automargin=True,
        nticks=5,
        tickformat=",",
        tickfont=dict(color=TEXT_SECONDARY, size=11),
    )

    fig.update_yaxes(
        title=None,
        showgrid=False,
        zeroline=False,
        showline=False,
        automargin=True,
        tickfont=dict(color=TEXT_PRIMARY, size=11),
    )

    return fig


def plot_club_value_chart(
    data: pd.DataFrame,
    *,
    height: int = 260,
) -> go.Figure:
    """
    Horizontal bar chart showing clubs by total squad
    market value represented at the tournament.
    """

    chart_data = (
        data.head(10)
        .sort_values("total_market_value_eur", ascending=True)
        .copy()
    )

    chart_data["club"] = (
        chart_data["club_team"]
        .apply(_wrap_axis_label)
    )

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=chart_data["total_market_value_eur"],
            y=chart_data["club"],
            orientation="h",
            marker=dict(color=ACCENT),
            text=chart_data["total_market_value_eur"],
            texttemplate="€%{text:,.0s}",
            textposition="outside",
            cliponaxis=False,
            customdata=chart_data[
                [
                    "players_sent",
                    "avg_market_value_eur",
                ]
            ],
            hovertemplate=(
                "<b>%{y}</b><br>"
                "Total Market Value: "
                "<b>€%{x:,.0f}</b><br>"
                "Players Sent: %{customdata[0]}<br>"
                "Average Player Value: "
                "€%{customdata[1]:,.0f}"
                "<extra></extra>"
            ),
        )
    )

    _style_dashboard_chart(
        fig,
        height=height,
        show_legend=False,
    )

    fig.update_xaxes(
        title="Market Value (€)",
        showgrid=True,
        gridcolor=GRID,
        zeroline=False,
        showline=False,
        tickfont=dict(
            color=TEXT_SECONDARY,
            size=11,
        ),
        title_font=dict(
            color=TEXT_SECONDARY,
            size=11,
        ),
        tickformat="~s",
    )

    fig.update_yaxes(
        showgrid=False,
        tickfont=dict(
            color=TEXT_PRIMARY,
            size=11,
        ),
    )

    return fig

def plot_venue_goals_chart(
    data: pd.DataFrame,
    height: int = CHART_HEIGHT_TWO_COLUMN,
) -> go.Figure:
    """Horizontal bar chart showing venues by average goals per match."""

    chart_data = data.sort_values("avg_goals_per_match", ascending=True).copy()
    chart_data["venue_label"] = chart_data["stadium_name"].apply(
        lambda name: _wrap_axis_label(_short_stadium_name(name))
    )

    fig = go.Figure(
        go.Bar(
            x=chart_data["avg_goals_per_match"],
            y=chart_data["venue_label"],
            orientation="h",
            marker=dict(color=PRIMARY, line=dict(width=0)),
            text=chart_data["avg_goals_per_match"],
            texttemplate="<b>%{text:.2f}</b>",
            textposition="outside",
            textfont=dict(color=TEXT_PRIMARY, size=12),
            customdata=chart_data[["stadium_name", "matches_hosted", "total_goals"]],
            hovertemplate=(
                "<b>%{customdata[0]}</b><br>"
                "Matches: %{customdata[1]}<br>"
                "Total goals: %{customdata[2]}<br>"
                "Avg goals/match: <b>%{x:.2f}</b>"
                "<extra></extra>"
            ),
            cliponaxis=False,
        )
    )

    _style_dashboard_chart(fig, height=height, show_legend=False)

    fig.update_xaxes(
        title="Average goals per match",
        title_standoff=10,
        showgrid=True,
        gridcolor=GRID,
        zeroline=False,
        showline=False,
        automargin=True,
        nticks=5,
        tickfont=dict(color=TEXT_SECONDARY, size=11),
    )
    fig.update_yaxes(
        title=None,
        showgrid=False,
        zeroline=False,
        showline=False,
        automargin=True,
        tickfont=dict(color=TEXT_PRIMARY, size=11),
    )

    return fig

def plot_venue_elevation_effects_chart(
    data: pd.DataFrame,
    height: int = CHART_HEIGHT_TWO_COLUMN,
) -> go.Figure:
    """Vertical bar chart showing average goals per match by elevation band."""

    chart_data = data.copy()

    fig = go.Figure(
        go.Bar(
            x=chart_data["elevation_band"],
            y=chart_data["avg_goals_per_match"],
            marker=dict(color=PRIMARY, line=dict(width=0)),
            text=chart_data["avg_goals_per_match"],
            texttemplate="<b>%{text:.2f}</b>",
            textposition="outside",
            textfont=dict(color=TEXT_PRIMARY, size=12),
            customdata=chart_data[["matches_played", "avg_combined_xg"]],
            hovertemplate=(
                "<b>%{x}</b><br>"
                "Matches: %{customdata[0]}<br>"
                "Avg goals/match: <b>%{y:.2f}</b><br>"
                "Avg combined xG: %{customdata[1]:.2f}"
                "<extra></extra>"
            ),
            cliponaxis=False,
        )
    )

    _style_dashboard_chart(fig, height=height, show_legend=False)

    fig.update_xaxes(
        title=None,
        showgrid=False,
        showline=False,
        automargin=True,
        tickfont=dict(color=TEXT_SECONDARY, size=11),
    )
    fig.update_yaxes(
        title="Average goals per match",
        title_standoff=10,
        showgrid=True,
        gridcolor=GRID,
        zeroline=False,
        showline=False,
        automargin=True,
        nticks=5,
        tickfont=dict(color=TEXT_SECONDARY, size=11),
        range=[0, chart_data["avg_goals_per_match"].max() * 1.20],
    )

    return fig

def plot_referee_matches_chart(
    data: pd.DataFrame,
    height: int = CHART_HEIGHT_THREE_COLUMN,
) -> go.Figure:
    """Horizontal bar chart of the top 8 referees by matches officiated."""

    chart_data = (
        data.sort_values("matches_officiated", ascending=False)
        .head(5)
        .sort_values("matches_officiated", ascending=True)
        .copy()
    )
    chart_data["referee_label"] = chart_data["referee"].apply(_wrap_axis_label)

    fig = go.Figure(
        go.Bar(
            x=chart_data["matches_officiated"],
            y=chart_data["referee_label"],
            orientation="h",
            marker=dict(color=PRIMARY, line=dict(width=0)),
            text=chart_data["matches_officiated"],
            texttemplate="<b>%{text}</b>",
            textposition="outside",
            textfont=dict(color=TEXT_PRIMARY, size=12),
            customdata=chart_data[["referee", "country", "pre_tournament_avg_cards"]],
            hovertemplate=(
                "<b>%{customdata[0]}</b><br>"
                "Country: %{customdata[1]}<br>"
                "Matches officiated: <b>%{x}</b><br>"
                "Pre-tournament avg cards: %{customdata[2]:.1f}"
                "<extra></extra>"
            ),
            cliponaxis=False,
        )
    )

    _style_dashboard_chart(fig, height=height, show_legend=False)

    fig.update_xaxes(
        title="Matches officiated",
        title_standoff=10,
        showgrid=True,
        gridcolor=GRID,
        zeroline=False,
        showline=False,
        automargin=True,
        nticks=5,
        tickformat=",",
        tickfont=dict(color=TEXT_SECONDARY, size=11),
    )
    fig.update_yaxes(
        title=None,
        showgrid=False,
        zeroline=False,
        showline=False,
        automargin=True,
        tickfont=dict(color=TEXT_PRIMARY, size=11),
    )

    return fig

def plot_referee_fouls_chart(
    data: pd.DataFrame,
    height: int = CHART_HEIGHT_THREE_COLUMN,
) -> go.Figure:
    """Horizontal bar chart of referees by average fouls per match."""

    eligible = data[data["matches_officiated"] >= 4]

    chart_data = (
        eligible.sort_values("avg_fouls_per_match", ascending=False)
        .head(5)
        .sort_values("avg_fouls_per_match", ascending = True)
        .copy()
    )
    chart_data["referee_label"] = chart_data["referee"].apply(_wrap_axis_label)

    fig = go.Figure(
        go.Bar(
            x=chart_data["avg_fouls_per_match"],
            y=chart_data["referee_label"],
            orientation="h",
            marker=dict(color=PRIMARY, line=dict(width=0)),
            text=chart_data["avg_fouls_per_match"],
            texttemplate="<b>%{text:.1f}</b>",
            textposition="outside",
            textfont=dict(color=TEXT_PRIMARY, size=12),
            customdata=chart_data[["referee", "country", "matches_officiated"]],
            hovertemplate=(
                "<b>%{customdata[0]}</b><br>"
                "Country: %{customdata[1]}<br>"
                "Matches officiated: %{customdata[2]}<br>"
                "Avg fouls/match: <b>%{x:.1f}</b>"
                "<extra></extra>"
            ),
            cliponaxis=False,
        )
    )

    _style_dashboard_chart(fig, height=height, show_legend=False)

    fig.update_xaxes(
        title="Average fouls per match",
        title_standoff=10,
        showgrid=True,
        gridcolor=GRID,
        zeroline=False,
        showline=False,
        automargin=True,
        nticks=5,
        tickfont=dict(color=TEXT_SECONDARY, size=11),
    )
    fig.update_yaxes(
        title=None,
        showgrid=False,
        zeroline=False,
        showline=False,
        automargin=True,
        tickfont=dict(color=TEXT_PRIMARY, size=11),
    )

    return fig

def plot_referee_card_comparison_chart(
    data: pd.DataFrame,
    height: int = CHART_HEIGHT_THREE_COLUMN,
) -> go.Figure:
    """Horizontal bar of the top 5 referees by average cards per game,
    limited to referees who officiated 4+ matches so the ranking
    reflects a meaningful sample rather than a single-game outlier."""

    eligible = data[data["matches_officiated"] >= 4]

    chart_data = (
        eligible.sort_values("actual_avg_cards_per_game", ascending=False)
        .head(5)
        .sort_values("actual_avg_cards_per_game", ascending=True)
        .copy()
    )
    chart_data["referee_label"] = chart_data["referee"].apply(_wrap_axis_label)

    fig = go.Figure(
        go.Bar(
            x=chart_data["actual_avg_cards_per_game"],
            y=chart_data["referee_label"],
            orientation="h",
            marker=dict(color=PRIMARY, line=dict(width=0)),
            text=chart_data["actual_avg_cards_per_game"],
            texttemplate="<b>%{text:.1f}</b>",
            textposition="outside",
            textfont=dict(color=TEXT_PRIMARY, size=12),
            customdata=chart_data[
                ["referee", "country", "matches_officiated", "yellow_cards", "red_cards"]
            ],
            hovertemplate=(
                "<b>%{customdata[0]}</b><br>"
                "Country: %{customdata[1]}<br>"
                "Matches officiated: %{customdata[2]}<br>"
                "Yellow cards: %{customdata[3]}<br>"
                "Red cards: %{customdata[4]}<br>"
                "Avg cards/match: <b>%{x:.1f}</b>"
                "<extra></extra>"
            ),
            cliponaxis=False,
        )
    )

    _style_dashboard_chart(fig, height=height, show_legend=False)

    fig.update_xaxes(
        title="Average cards per match",
        title_standoff=10,
        showgrid=True,
        gridcolor=GRID,
        zeroline=False,
        showline=False,
        automargin=True,
        nticks=5,
        tickfont=dict(color=TEXT_SECONDARY, size=11),
    )
    fig.update_yaxes(
        title=None,
        showgrid=False,
        zeroline=False,
        showline=False,
        automargin=True,
        tickfont=dict(color=TEXT_PRIMARY, size=11),
    )

    return fig

def plot_referee_stage_workload_chart(
    data: pd.DataFrame,
    height: int = 300,
) -> go.Figure:
    """Stacked bar of stage-by-stage workload for the 8 busiest
    referees who officiated more than one match."""

    totals = (
        data.groupby("referee")["matches_officiated"]
        .sum()
        .reset_index(name="total_matches")
    )
    eligible = totals[totals["total_matches"] >= 2]
    top_referees = eligible.sort_values("total_matches", ascending=False).head(8)["referee"]

    chart_data = data[data["referee"].isin(top_referees)].copy()
    order = (
        chart_data.groupby("referee")["matches_officiated"]
        .sum()
        .sort_values(ascending=True)
        .index
    )
    chart_data["referee_label"] = chart_data["referee"].apply(_wrap_axis_label)
    label_order = [_wrap_axis_label(r) for r in order]

    fig = px.bar(
        chart_data,
        x="matches_officiated",
        y="referee_label",
        color="stage",
        orientation="h",
        barmode="stack",
        category_orders={"referee_label": label_order},
        custom_data=["referee", "stage"],
    )

    fig.update_traces(
        hovertemplate=(
            "<b>%{customdata[0]}</b><br>"
            "Stage: %{customdata[1]}<br>"
            "Matches: <b>%{x}</b><extra></extra>"
        ),
        marker_line_width=0,
    )

    _style_dashboard_chart(fig, height=height, show_legend=True)

    fig.update_layout(legend_title=None)

    fig.update_xaxes(
        title="Matches officiated",
        title_standoff=10,
        showgrid=True,
        gridcolor=GRID,
        zeroline=False,
        showline=False,
        automargin=True,
        nticks=5,
        tickformat=",",
        tickfont=dict(color=TEXT_SECONDARY, size=11),
        title_font=dict(color=TEXT_SECONDARY, size=11),
    )
    fig.update_yaxes(
        title=None,
        showgrid=False,
        zeroline=False,
        showline=False,
        automargin=True,
        tickfont=dict(color=TEXT_PRIMARY, size=11),
    )

    return fig