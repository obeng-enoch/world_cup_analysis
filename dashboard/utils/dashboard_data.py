from src.analytics.tournament import (
    get_total_teams,
    get_total_players,
    get_total_matches,
    get_total_goals,
    get_world_cup_winner,
    get_runner_up,
    get_third_place,
    get_goals_per_stage,
)

from src.analytics.awards import get_awards
from src.analytics.teams import get_tournament_finish


def get_homepage_metrics():
    """
    Return all metrics required by the dashboard home page.
    """
    return {
        "teams": get_total_teams(),
        "players": get_total_players(),
        "matches": get_total_matches(),
        "goals": get_total_goals(),
    }

def get_tournament_summary():
    return {
        "teams": get_total_teams(),
        "players": get_total_players(),
        "matches": get_total_matches(),
        "goals": get_total_goals(),
        "winner": get_world_cup_winner(),
        "runner_up": get_runner_up(),
        "third_place": get_third_place(),
    }

def get_tournament_awards():
    return get_awards()

def get_tournament_finish_table():
    return get_tournament_finish()

def get_goals_per_stage_chart():
    return get_goals_per_stage()