from pathlib import Path
import re

import streamlit as st

from dashboard.theme.colors import TEXT_PRIMARY

ICON_DIRECTORY = (
    Path(__file__).resolve().parents[1]
    / "assets"
    / "icons"
)

@st.cache_data
def load_icon(icon: str) -> str:
    """
    Load an SVG icon from disk
    """
    icon_path = ICON_DIRECTORY / f"{icon}.svg"

    if not icon_path.exists():
        raise FileNotFoundError(
            f"Icon '{icon}' was not found in '{ICON_DIRECTORY}'."
        )

    return icon_path.read_text(encoding="utf-8")
    

def render_icon(
    icon: str,
    size: int = 20,
    color: str = TEXT_PRIMARY,
) -> str:
    """
    Render a Lucide SVG icon with custom size and colour
    """
    svg = load_icon(icon)

    svg = svg.replace(
        'width="24"',
        f'width="{size}"',
        1,
    )

    svg = svg.replace(
        'height="24"',
        f'height="{size}"',
        1,
    )

    svg = svg.replace(
        "currentColor",
        color,
    )

    return svg
