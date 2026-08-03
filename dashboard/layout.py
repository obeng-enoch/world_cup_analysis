"""
dashboard/layout.py

Reusable layout helpers for the FIFA World Cup 2026 Analytics Dashboard.

This is Phase 2 of the frontend design system rollout. It replaces
scattered, page-level `st.columns()` calls with a small set of named,
semantic layout primitives that every page can share.

Design rules (consistent with the rest of the theme/component system):
- No SQL, no analytics-layer calls, no business logic lives here.
  This module only arranges things on screen.
- No colours, spacing, or typography choices are hard-coded here.
  Vertical rhythm comes from a CSS class (`.section-gap`) defined in
  `dashboard/theme/css.py`, and section titles are rendered by
  `dashboard.components.headings.section_heading`, not by this module.

Two calling conventions live side by side in this file, intentionally:
- `columns()`, `two_columns()`, `three_columns()` are low-level
  primitives that RETURN Streamlit containers, the same way
  `st.columns()` itself does. Use these when a section needs more
  than one component stacked in the same column, or any layout
  Streamlit's native context-manager style handles better.
- `kpi_grid()` and `chart_row()` are high-level convenience helpers
  that RENDER immediately. They take *renderers* — zero-arg callables
  like `lambda: metric_card(...)` — because their whole job is
  "put one thing per slot, repeatedly," where the renderer pattern
  is more concise than juggling containers by hand.

This mirrors Streamlit's own inconsistency (`st.columns()` returns,
`st.metric()` renders) rather than fighting it, so pick the style that
matches what a given section of a page actually needs.

Typical usage inside a page:

    from dashboard.layout import section, kpi_grid, two_columns, chart_row
    from dashboard.components.metric_card import metric_card
    from dashboard.components.charts import plot_bar_chart

    with section("Tournament Overview"):
        kpi_grid([
            lambda: metric_card(label="Matches Played", value=48),
            lambda: metric_card(label="Goals Scored", value=132),
            lambda: metric_card(label="Avg Goals / Match", value=2.75),
            lambda: metric_card(label="Teams", value=32),
        ])

    with section("Final Standings", "Top 8 finishers"):
        left, right = two_columns(ratio=(2, 1))
        with left:
            render_standings_table(df_standings)
            st.caption("Updated after every match day")
        with right:
            render_awards_panel(df_awards)

    with section("Goals by Stage", "Match Outcomes"):
        chart_row([
            lambda: st.plotly_chart(plot_bar_chart(df_goals_by_stage), use_container_width=True),
            lambda: st.plotly_chart(plot_pie_chart(df_outcomes), use_container_width=True),
        ])
"""

from __future__ import annotations

from typing import Callable, Optional, Sequence, Tuple, Union

import streamlit as st

from dashboard.components.headings import section_heading

__all__ = [
    "columns",
    "two_columns",
    "three_columns",
    "kpi_grid",
    "chart_row",
    "section",
]

# A renderer is any zero-arg callable that renders something into the
# current Streamlit context (a component call, a chart call, etc.)
Renderer = Callable[[], None]


# Low-level primitive: returns containers, like st.columns() does

def columns(
    ratio: Union[int, Sequence[float]] = 2,
    gap: str = "small",
):
    """
    Return `n` Streamlit containers sized per `ratio`.

    `ratio` is either an int (that many equal-width columns) or a
    sequence of relative widths, e.g. `(2, 1)` for a column twice as
    wide as its neighbour — same semantics as `st.columns()`.

    This is the primitive that `two_columns()` and `three_columns()`
    are built on; reach for it directly when you need more than three
    columns, or non-uniform counts driven by data.

    Example:
        left, right = columns(ratio=(2, 1))
        with left:
            render_standings_table(df)
        with right:
            render_awards_panel(df)
    """
    return st.columns(ratio, gap=gap)


def two_columns(ratio: Tuple[float, float] = (1, 1)):
    """Convenience wrapper: `columns()` for the common two-column case."""
    return columns(list(ratio))


def three_columns(ratio: Tuple[float, float, float] = (1, 1, 1)):
    """Convenience wrapper: `columns()` for the common three-column case."""
    return columns(list(ratio))


# High-level convenience helpers: render immediately, renderer-based
# 

def _render_renderers(
    renderers: Sequence[Renderer],
    ratios: Optional[Sequence[float]] = None,
) -> None:
    """Internal: place each renderer into its own container from columns()."""
    if not renderers:
        return
    cols = columns(list(ratios) if ratios else len(renderers))
    for col, render in zip(cols, renderers):
        with col:
            render()


def kpi_grid(renderers: Sequence[Renderer], per_row: int = 4) -> None:
    """
    Lay out KPI / metric cards in a responsive grid.

    Renders `renderers` (typically closures around `metric_card(...)`)
    in rows of `per_row` columns each. If the count isn't a multiple
    of `per_row`, the final row is simply shorter rather than padded
    with empty columns.
    """
    renderers = list(renderers)
    for start in range(0, len(renderers), per_row):
        row = renderers[start:start + per_row]
        _render_renderers(row)
    _section_gap()


def chart_row(
    charts: Sequence[Renderer],
    ratios: Optional[Sequence[float]] = None,
) -> None:
    """
    Render one or more charts side by side in a themed row.

    Unlike `kpi_grid`, this does not wrap to multiple rows — pass
    exactly as many renderers as should share one horizontal band
    (typically 1-3). Use for pairs like "Goals by Stage" / "Match
    Outcomes" or "Goals by Team" / "Tournament Insights".

    Kept as a named, renderer-based helper rather than asking pages
    to call `columns()` + a loop by hand — purely for readability at
    the call site.
    """
    _render_renderers(list(charts), ratios=ratios)
    _section_gap()


def _section_gap() -> None:
    """Consistent vertical spacing between layout blocks.

    Uses a CSS class (`.section-gap`) from dashboard/theme/css.py
    rather than an inline style, so spacing stays theme-controlled.
    """
    st.markdown("<div class='section-gap'></div>", unsafe_allow_html=True)

# Section wrapper

class _Section:
    """Context manager backing `section()` — see that function's docstring."""

    def __init__(self, title: Optional[str], description: Optional[str]):
        self.title = title
        self.description = description

    def __enter__(self) -> "_Section":
        section_heading(self.title, self.description)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        _section_gap()
        return False


def section(title: Optional[str] = None, description: Optional[str] = None) -> _Section:
    """
    Context manager that wraps a block of page content with a
    consistent section header and top/bottom margin.

    Title/description rendering is delegated to
    `dashboard.components.headings.section_heading` — layout.py only
    decides *where* the heading goes, not how it looks.

    Example:
        with section("Tournament Overview"):
            kpi_grid([...])

        with section("Final Standings", "Top 8 finishers"):
            left, right = two_columns(ratio=(2, 1))
            ...
    """
    return _Section(title, description)