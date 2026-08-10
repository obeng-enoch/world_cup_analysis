from typing import Optional

import plotly.express as px
import plotly.graph_objects as go

import pandas as pd
from dashboard.theme.constants import CHART_HEIGHT_COMPACT

from dashboard.theme.colors import (
    ACCENT,
    GRID,
    PRIMARY,
    SECONDARY,
    TEXT_PRIMARY,
    TEXT_SECONDARY,
)

DEFAULT_HEIGHT = CHART_HEIGHT_COMPACT
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
    """
    Apply the dashboard styling used by all
    football-specific Plotly charts.
    """

    fig.update_layout(
        template="none",
        height=height,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(
            l=100,
            r=20,
            t=20,
            b=30,
        ),
        font=dict(
            family="'Inter', 'Segoe UI', sans-serif",
            color=TEXT_PRIMARY,
            size=12,
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

def plot_stage_goals_chart(
    data: pd.DataFrame,
    value_column: str,
    value_label: str,
    height: int = 210,
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
        tickfont=dict(color=TEXT_SECONDARY, size=11),
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
        title_font=dict(color=TEXT_SECONDARY, size=11),
        range=[0, data[value_column].max() * 1.20],
    )

    return fig

def plot_goal_contributions_chart(
    data: pd.DataFrame,
    *,
    height: int = 200,
) -> go.Figure:
    """
    Stacked horizontal bar chart showing the Top 5 players
    by total goal contributions (Goals + Assists).
    """

    # ------------------------------------------
    # Prepare Data
    # ------------------------------------------

    chart_data = (
        data.head(5)
        .sort_values("goal_contributions", ascending=True)
        .copy()
    )

    chart_data["player"] = (
        chart_data["player_name"]
        .apply(_wrap_axis_label)
    )

    # ------------------------------------------
    # Build Figure
    # ------------------------------------------

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

    # ------------------------------------------
    # Layout
    # ------------------------------------------

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
        title_font=dict(
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

def plot_goalkeeper_saves_chart(
    data: pd.DataFrame,
    *,
    height: int = 200,
) -> go.Figure:
    """
    Horizontal bar chart showing the Top 5 goalkeepers by saves.
    """

    chart_data = (
        data.head(5)
        .sort_values("saves", ascending=True)
        .copy()
    )

    chart_data["player"] = (
        chart_data["player_name"]
        .apply(_wrap_axis_label)
    )

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=chart_data["saves"],
            y=chart_data["player"],
            orientation="h",
            marker=dict(color=PRIMARY),
            text=chart_data["saves"],
            texttemplate="<b>%{text}</b>",
            textposition="outside",
            cliponaxis=False,
            customdata=chart_data[
                [
                    "team",
                    "clean_sheets",
                    "goals_conceded",
                    "matches_played",
                ]
            ],
            hovertemplate=(
                "<b>%{y}</b><br>"
                "Team: %{customdata[0]}<br>"
                "Saves: <b>%{x}</b><br>"
                "Clean Sheets: %{customdata[1]}<br>"
                "Goals Conceded: %{customdata[2]}<br>"
                "Matches: %{customdata[3]}"
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
        title="Saves",
        showgrid=True,
        gridcolor=GRID,
        zeroline=False,
    )

    fig.update_yaxes(
        showgrid=False,
    )

    return fig

def plot_goals_by_team_chart(df):

    fig = px.bar(
        df,
        x="team",
        y="goals",
        text="goals",
        hover_data={
            "matches_played": True,
            "goals_per_match": True,
            "shots": True,
            "shots_on_target": True,
        },
    )

    fig.update_traces(
        textposition="outside",
        hovertemplate=(
            "<b>%{x}</b><br>"
            "Goals: %{y}<br>"
            "Matches: %{customdata[0]}<br>"
            "Goals per Match: %{customdata[1]}<br>"
            "Shots: %{customdata[2]}<br>"
            "Shots on Target: %{customdata[3]}"
            "<extra></extra>"
        ),
    )

    fig.update_xaxes(
        ticktext=[_wrap_axis_label(x) for x in df["team"]],
        tickvals=df["team"],
    )

    fig.update_layout(
        xaxis_title=None,
        yaxis_title="Goals Scored",
        uniformtext_minsize=10,
        uniformtext_mode="hide",
    )
    
    return _style_dashboard_chart(fig, height=260)

def plot_best_defense_chart(df):

    # Highest clean sheets first
    df=df.sort_values("clean_sheets", ascending=False)

    fig = px.bar(
        df,
        x="team",
        y="clean_sheets",
        text="clean_sheets",
        hover_data={
            "goals_against": True,
            "matches_played": True,
            "goals_conceded_per_match": True,
        },
    )

    fig.update_traces(
        textposition="outside",
        hovertemplate=(
            "<b>%{y}</b><br>"
            "Clean Sheets: %{y}<br>"
            "Goals Against: %{customdata[0]}<br>"
            "Matches: %{customdata[1]}<br>"
            "Goals/Match: %{customdata[2]:.2f}"
            "<extra></extra>"
        ),
    )

    fig.update_xaxes(
        ticktext=[_wrap_axis_label(x) for x in df["team"]],
        tickvals=df["team"],
    )

    fig.update_yaxes(
        range=[0, df["clean_sheets"].max() * 1.20]
    )

    fig.update_layout(
        xaxis_title=None,
        yaxis_title="Clean Sheets",
        uniformtext_minsize=10,
        uniformtext_mode="hide",
    )

    return _style_dashboard_chart(fig, height=260)


def plot_goal_timing_chart(df):
    fig = px.bar(
        df,
        x="time_window",
        y="goals",
        text="goals",
        category_orders={
            "time_window": [
                "0-15",
                "16-30",
                "31-45",
                "46-60",
                "61-75",
                "76-90",
                "90+",
            ]
        },
    )

    fig.update_traces(
        textposition="outside",
        hovertemplate=(
            "<b>%{x} minutes</b><br>"
            "Goals: %{y}<extra></extra>"
        ),
    )

    fig.update_xaxes(
        showgrid=False,
    )

    fig.update_yaxes(
        title_text="Goals Scored",
        showgrid=True,
    )

    return _style_dashboard_chart(fig, height=260)


def plot_match_result_distribution_chart(df):
    total_matches = df["matches"].sum()

    fig = px.pie(
        df,
        names="result_type",
        values="matches",
        hole=0.55,
    )

    fig.update_traces(
        textposition="outside",
        textinfo="percent",
        hovertemplate=(
            "<b>%{label}</b><br>"
            "Matches: %{value}<br>"
            "Share: %{percent}"
            "<extra></extra>"
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
    )

    fig.update_layout(
        height=420,
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.15,
            xanchor="center",
            x=0.5,
        ),
    )

    return _style_dashboard_chart(fig, height=260)

def plot_club_goal_contributions_chart(
    data: pd.DataFrame,
    *,
    height: int = 260,
) -> go.Figure:
    """
    Horizontal bar chart showing the top clubs by
    total goal contributions.
    """

    chart_data = (
        data.head(10)
        .sort_values("goal_contributions", ascending=True)
        .copy()
    )

    chart_data["club"] = (
        chart_data["club_team"]
        .apply(_wrap_axis_label)
    )

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=chart_data["goal_contributions"],
            y=chart_data["club"],
            orientation="h",
            marker=dict(color=PRIMARY),
            text=chart_data["goal_contributions"],
            texttemplate="<b>%{text}</b>",
            textposition="outside",
            cliponaxis=False,
            customdata=chart_data[
                [
                    "goals",
                    "assists",
                    "players_sent",
                ]
            ],
            hovertemplate=(
                "<b>%{y}</b><br>"
                "Goal Contributions: <b>%{x}</b><br>"
                "Goals: %{customdata[0]}<br>"
                "Assists: %{customdata[1]}<br>"
                "Players Sent: %{customdata[2]}"
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
        title="Goal Contributions",
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
    height: int = 260,
) -> go.Figure:
    """
    Horizontal bar chart showing clubs by total minutes played.
    """

    chart_data = (
        data.head(10)
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
            marker=dict(color=ACCENT),
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
        title_font=dict(
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

def plot_club_representation_chart(
    data: pd.DataFrame,
    *,
    height: int = 260,
) -> go.Figure:
    """
    Horizontal bar chart showing clubs with the most
    players represented at the tournament.
    """

    chart_data = (
        data.head(10)
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
        title_font=dict(
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

def plot_venue_goals_chart(df):
    data = df.copy()

    data["venue_label"] = data["stadium_name"].apply(
        _wrap_axis_label
    )

    fig = px.bar(
        data,
        x="avg_goals_per_match",
        y="venue_label",
        orientation="h",
        text="avg_goals_per_match",
        custom_data=[
            "stadium_name",
            "matches_hosted",
            "total_goals",
        ],
    )

    fig.update_traces(
        texttemplate="%{text:.2f}",
        textposition="outside",
        hovertemplate=(
            "<b>%{customdata[0]}</b><br>"
            "Matches: %{customdata[1]}<br>"
            "Total goals: %{customdata[2]}<br>"
            "Avg goals/match: %{x:.2f}"
            "<extra></extra>"
        ),
    )

    fig.update_layout(
        xaxis_title="Average Goals per Match",
        yaxis_title=None,
    )

    return _style_dashboard_chart(fig, height=250)

def plot_venue_match_day_style_chart(df):
    data = df.copy()

    data["venue_label"] = data["stadium_name"].apply(
        _wrap_axis_label
    )

    fig = px.bar(
        data,
        x=[
            "avg_corners",
            "avg_fouls",
            "avg_offsides",
        ],
        y="venue_label",
        orientation="h",
        barmode="group",
        custom_data=["stadium_name"],
    )

    fig.update_traces(
        hovertemplate=(
            "<b>%{customdata[0]}</b><br>"
            "%{fullData.name}: %{x:.2f}"
            "<extra></extra>"
        )
    )

    fig.update_layout(
        xaxis_title="Average per Match",
        yaxis_title=None,
        legend_title=None,
    )

    return _style_dashboard_chart(fig, height=250)

def plot_venue_elevation_effects_chart(df):
    data = df.copy()

    fig = px.bar(
        data,
        x="elevation_band",
        y="avg_goals_per_match",
        text="avg_goals_per_match",
        custom_data=[
            "matches_played",
            "avg_combined_xg",
        ],
    )

    fig.update_traces(
        texttemplate="%{text:.2f}",
        textposition="outside",
        hovertemplate=(
            "<b>%{x}</b><br>"
            "Matches: %{customdata[0]}<br>"
            "Avg goals/match: %{y:.2f}<br>"
            "Avg combined xG: %{customdata[1]:.2f}"
            "<extra></extra>"
        ),
    )

    fig.update_layout(
        xaxis_title="Elevation Band",
        yaxis_title="Average Goals per Match",
    )

    return _style_dashboard_chart(fig, height=250)

def plot_venue_stage_distribution_chart(df):
    data = df.copy()

    data["venue_label"] = data["stadium_name"].apply(
        _wrap_axis_label
    )

    fig = px.bar(
        data,
        x="matches_hosted",
        y="venue_label",
        color="stage",
        orientation="h",
        barmode="stack",
        custom_data=[
            "stadium_name",
            "stage",
        ],
    )

    fig.update_traces(
        hovertemplate=(
            "<b>%{customdata[0]}</b><br>"
            "Stage: %{customdata[1]}<br>"
            "Matches: %{x}"
            "<extra></extra>"
        )
    )

    fig.update_layout(
        xaxis_title="Matches Hosted",
        yaxis_title=None,
        legend_title=None,
    )

    return _style_dashboard_chart(fig, height=250)