import streamlit as st

def podium_card(position: str, team: str):
    st.markdown(f"### {position}")
    st.write(team)