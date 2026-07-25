import streamlit as st


def metric_card(label: str, value, delta=None):
    """
    Display a single KPI metric card.

    Parameters
    ----------
    label : str
        Metric title.

    value :
        Metric value.

    delta :
        Optional change indicator.
    """
    st.metric(
        label=label,
        value=value,
        delta=delta,
        border=True,
    )