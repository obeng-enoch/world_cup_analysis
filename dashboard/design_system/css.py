import streamlit as st


def load_css():
    """
    Inject the dashboard's global CSS.
    """

    st.markdown(
        """
        <style>

        .block-container{
            padding-top:2rem;
            padding-bottom:2rem;
            padding-left:2rem;
            padding-right:2rem;
            max-width:1600px;
        }

        div[data-testid="stMetric"]{
            border-radius:14px;
            padding:16px;
        }

        .element-container{
            margin-bottom:1rem;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )