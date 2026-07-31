import streamlit as st


def kpi_grid(columns: int = 4):
    """
    Create a KPI row.

    Returns
    -------
    list
        Streamlit columns.
    """
    return st.columns(columns)


def two_column():
    return st.columns(2)


def three_column():
    return st.columns(3)


def four_column():
    return st.columns(4)


def sidebar_main(sidebar_ratio=1, main_ratio=4):
    return st.columns([sidebar_ratio, main_ratio])


def chart_row():
    return st.columns(2)