"""
FIFA World Cup 2026 — Streamlit dashboard
Run with: streamlit run app.py
"""

import sqlite3
from datetime import datetime

import pandas as pd
import plotly.express as px
import streamlit as st

# ── CONFIG ────────────────────────────────────────────────────────────────
# Adjust this path to match where app.py sits relative to the .db file
DB_PATH = "../data/raw/worldcup/sqlite_fifa_world_cup_2026.db"

st.set_page_config(page_title="World Cup 2026 Dashboard", layout="wide")


# ── DATA LOADING (cached so it doesn't re-query on every click) ───────────
@st.cache_data
def load_data(db_path: str):
    conn = sqlite3.connect(db_path)

    player_stats = pd.read_sql("SELECT * FROM player_stats;", conn)
    squads = pd.read_sql("SELECT * FROM squads_and_players;", conn)
    teams = pd.read_sql("SELECT * FROM teams;", conn)
    matches = pd.read_sql("SELECT * FROM matches;", conn)
    match_events = pd.read_sql("SELECT * FROM match_events;", conn)

    conn.close()
    return player_stats, squads, teams, matches, match_events


player_stats, squads, teams, matches, match_events = load_data(DB_PATH)

# Data freshness — shows the most recent match date in the dataset
latest_match_date = pd.to_datetime(matches["date"]).max()

# ── SIDEBAR ─────────────────────────────────────────────────────────────
st.sidebar.title("Filters")
st.sidebar.caption(
    f"Data current as of: **{latest_match_date.strftime('%b %d, %Y')}**\n\n"
    "This dataset updates on the maintainer's schedule, not live — "
    "run `git pull && git lfs pull` for the newest snapshot."
)

team_options = ["All teams"] + sorted(teams["team_name"].dropna().unique().tolist())
selected_team = st.sidebar.selectbox("Filter by team", team_options)

# ── HEADER + KPIs ───────────────────────────────────────────────────────
st.title("⚽ FIFA World Cup 2026 — Analytics Dashboard")

total_goals = int(player_stats["goals"].sum())
total_matches = matches["match_id"].nunique()
top_scorer_row = player_stats.sort_values("goals", ascending=False).iloc[0]

col1, col2, col3 = st.columns(3)
col1.metric("Total goals scored", total_goals)
col2.metric("Matches played", total_matches)
col3.metric(
    "Top scorer",
    top_scorer_row["player_name"],
    f"{int(top_scorer_row['goals'])} goals",
)

st.divider()

# ── TABS ────────────────────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs(["🥇 Top Scorers", "🏟️ Top Clubs by Goals", "📊 Team Comparison"])

# --- Tab 1: Top scorers ---
with tab1:
    st.subheader("Top 10 goal scorers")

    scorers = player_stats.sort_values("goals", ascending=False).head(10)
    fig = px.bar(
        scorers,
        x="goals",
        y="player_name",
        orientation="h",
        text="goals",
        labels={"player_name": "Player", "goals": "Goals"},
    )
    fig.update_layout(yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(fig, use_container_width=True)

# --- Tab 2: Top clubs by goals contributed ---
with tab2:
    st.subheader("Which clubs contributed the most World Cup goals?")

    goal_events = match_events[match_events["event_type"] == "Goal"]
    goals_with_club = goal_events.merge(
        squads[["player_id", "club_team"]], on="player_id", how="left"
    )
    club_goals = (
        goals_with_club.groupby("club_team")
        .size()
        .reset_index(name="goals")
        .sort_values("goals", ascending=False)
        .head(15)
    )

    fig2 = px.bar(
        club_goals,
        x="goals",
        y="club_team",
        orientation="h",
        text="goals",
        labels={"club_team": "Club", "goals": "Goals contributed"},
    )
    fig2.update_layout(yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(fig2, use_container_width=True)

    st.caption(
        "Counts goals by the club each scorer plays for domestically — "
        "not the national team they scored for."
    )

# --- Tab 3: Team comparison ---
with tab3:
    st.subheader("Team-level comparison")

    team_stats = (
        player_stats.merge(teams[["team_id", "team_name"]], on="team_id", how="left")
        .groupby("team_name")[["goals", "assists"]]
        .sum()
        .reset_index()
    )

    if selected_team != "All teams":
        team_stats = team_stats[team_stats["team_name"] == selected_team]

    st.dataframe(
        team_stats.sort_values("goals", ascending=False),
        use_container_width=True,
        hide_index=True,
    )
