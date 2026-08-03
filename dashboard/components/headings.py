"""
dashboard/components/headings.py

Section heading component for the FIFA World Cup 2026 Analytics Dashboard.

Renders the title/description pairing used to introduce a page section
(e.g. "Final Standings", "Top 8 finishers"). This lives here — not as
inline `st.markdown()`/`st.caption()` calls in dashboard/layout.py —
so section typography is governed by dashboard/theme like every other
visual element, and layout.py stays purely about *where* things go
rather than *how* they look.

Follows the same pattern as the other components:
    inputs -> escape text -> generate HTML -> st.html()

Requires two CSS classes to exist in dashboard/theme/css.py:
    .section-heading-title        (typography.SECTION_TITLE_SIZE / colors.TEXT_PRIMARY)
    .section-heading-description  (typography tokens / colors.TEXT_SECONDARY)
"""

from __future__ import annotations

import html
from typing import Optional

import streamlit as st

__all__ = ["section_heading"]


def section_heading(title: Optional[str] = None, description: Optional[str] = None) -> None:
    """
    Render a themed section title and optional description.

    No-op if neither `title` nor `description` is given, so callers
    (like `layout.section()`) can invoke this unconditionally.
    """
    if not title and not description:
        return

    parts = []
    if title:
        parts.append(f'<div class="section-heading-title">{html.escape(title)}</div>')
    if description:
        parts.append(f'<div class="section-heading-description">{html.escape(description)}</div>')

    st.html("".join(parts))