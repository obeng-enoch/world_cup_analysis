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

    fig.update_layout(
        template="none",
        height=height,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=58, r=12, t=18, b=58),
        font=dict(
            family="'Inter', 'Segoe UI', sans-serif",
            color=TEXT_PRIMARY,
            size=12,
        ),
        hoverlabel=dict(
            bgcolor="#1B2027",
            bordercolor=PRIMARY,
            font_color=TEXT_PRIMARY,
        ),
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