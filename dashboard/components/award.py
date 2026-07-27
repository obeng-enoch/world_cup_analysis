import streamlit as st


def award_card(award_name: str, player_name: str, team: str):
    """
    Display a tournament award card.
    """

    with st.container(border=True):
        st.markdown(f"### 🏆 {award_name}")
        st.write(f"**Winner:** {player_name}")
        st.write(f"**Team:** {team}")