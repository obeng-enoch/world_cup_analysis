from pathlib import Path

import streamlit as st


def load_css():
    """Load the global stylesheet."""
    css_path = (
        Path(__file__).parents[1]
        / "styles"
        / "style.css"
    )

    if css_path.exists():
        with open(css_path) as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True,
            )