"""
Tournament-level analytics endpoints.

These functions expose tournament-wide KPIs and results.
They return either scalar values or DataFrames and never
contain business logic.
"""

from src.analytics.database import get_scalar


# --------------------------------------------------
# Tournament KPIs
# --------------------------------------------------

def get_total_players():
    return get_scalar("tournament_overview/total_players.sql")


def get_total_teams():
    return get_scalar("tournament_overview/total_teams.sql")


def get_total_matches():
    return get_scalar("tournament_overview/total_matches.sql")


def get_total_goals():
    return get_scalar("tournament_overview/total_goals.sql")


# --------------------------------------------------
# Tournament Results
# --------------------------------------------------

def get_world_cup_winner():
    return get_scalar("tournament_overview/world_cup_winner.sql")


def get_runner_up():
    return get_scalar("tournament_overview/runner_up.sql")


def get_third_place():
    return get_scalar("tournament_overview/third_place.sql")