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

from src.analytics.players import (
    get_top_scorers,
    get_hat_tricks,
    get_multi_goal_matches,
    get_penalty_goals,
    get_own_goals,
    get_top_assists,
    get_goal_contributions,
    get_appearances,
    get_starts,
    get_minutes_played,
    get_yellow_cards,
    get_red_cards,
    get_clean_sheets,
    get_saves,
    get_goals_conceded,
)

from src.analytics.teams import (
    get_aggresive_attacking,
    get_defense,
    get_discipline,
    get_highest_scoring_teams,
    get_tournament_finish,
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

def get_player_summary():
    """
    Returns the headline player achievements shown
    in the KPI cards at the top of the Players page.
    """
    top_scorer = get_top_scorers().iloc[0]
    top_assist = get_top_assists().iloc[0]
    top_goalkeeper = get_clean_sheets().iloc[0]

    return {
        "top_scorer": top_scorer,
        "top_assist": top_assist,
        "top_goalkeeper": top_goalkeeper,
    }

def get_scoring_tables():
    """
    Returns all attacking player tables.
    """

    return {
        "top_scorers": get_top_scorers(),
        "top_assists": get_top_assists(),
        "goal_contributions": get_goal_contributions(),
        "penalty_goals": get_penalty_goals(),
        "own_goals": get_own_goals(),
    }

def get_player_charts():
    """
    Returns datasets required by the Players page charts.
    """

    return {
        "goal_contributions": get_goal_contributions(),
        "top_saves": get_saves(),
    }

def get_discipline_tables():
    """
    Returns disciplinary statistics.
    """

    return {
        "yellow_cards": get_yellow_cards(),
        "red_cards": get_red_cards(),
    }

def get_goalkeeping_tables():
    """
    Returns goalkeeper statistics.
    """

    return {
        "clean_sheets": get_clean_sheets(),
        "saves": get_saves(),
        "goals_conceded": get_goals_conceded(),
    }

def get_player_achievements():
    """
    Returns notable player achievements.
    """

    return {
        "hat_tricks": get_hat_tricks(),
        "multi_goal_matches": get_multi_goal_matches(),
    }

def get_team_summary():
    """
    Returns the three headline team highlights for the Teams pages.and
    """

    standings = get_tournament_finish()

    winner = standings.iloc[0]
    runner_up = standings.iloc[1]
    third_place = standings.iloc[2]

    return {
        "winner": winner,
        "runner_up": runner_up,
        "third_place": third_place,
    }

def get_team_charts():
    """
    Returns datasets used by the Teams page charts.
    """

    return {
        "goals_by_team": get_highest_scoring_teams(),
        "best_defense": get_defense(),
    }

def get_team_tables():
    """
    Returns the supporting tables displayed on the Teams page.
    """

    return {
        "attacking": get_aggresive_attacking(),
        "discipline": get_discipline(),
    }

