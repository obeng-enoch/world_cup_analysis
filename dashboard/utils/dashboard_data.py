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
from src.analytics.events import get_event_counts

from src.analytics.players import (
    get_top_scorers,
    get_hat_tricks,
    get_multi_goal_matches,
    get_penalty_goals,
    get_own_goals,
    get_top_assists,
    get_goal_contributions as get_player_goal_contributions,
    get_appearances,
    get_starts,
    get_minutes_played as get_players_minutes_played,
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

from src.analytics.matches import (
    get_highest_scoring as get_match_highest_scoring,
    get_biggest_wins,
    get_biggest_upsets,
    get_goal_timing,
    get_match_results,
    get_match_result_distribution,
    get_possession_dominant,
)

from src.analytics.clubs import (
    get_club_medals,
    get_discipline,
    get_goal_contributions as get_club_goal_contributions,
    get_minutes_played,
    get_most_representation,
    get_valuable,
)

from src.analytics.venues import (
    get_average_stats,
    get_country_hosted,
    get_directory,
    get_elevation_accuracy,
    get_elevation_ranked,
    get_goals_per_venue,
    get_highest_scoring as get_venue_highest_scoring,
    get_stage_distribution,
)

from src.analytics.referees import (
    get_fouls,
    get_matches_officiated,
    get_red_cards,
    get_country_distribution,
    get_card_comparison,
    get_stage_workload,
)

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

def get_tournament_event_counts():
    return get_event_counts()

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
        "goal_contributions": get_player_goal_contributions(),
        "penalty_goals": get_penalty_goals(),
        "own_goals": get_own_goals(),
    }

def get_player_charts():
    """
    Returns datasets required by the Players page charts.
    """

    return {
        "goal_contributions": get_player_goal_contributions(),
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

def get_match_summary():
    """
    Returns datasets used by the Matches page charts.
    """

    return {
        "highest_scoring": get_match_highest_scoring().iloc[0],
        "biggest_wins": get_biggest_wins().iloc[0],
        "biggest_upsets": get_biggest_upsets().iloc[0],
    }

def get_match_charts():
    return {
        "goal_timing": get_goal_timing(),
        "match_result_distribution": get_match_result_distribution(),
    }

def get_match_tables():
    return {
        "match_results": get_match_results(),
        "possession": get_possession_dominant(),
    }

def get_club_summary():
    """
    Returns the headline club achievements shown
    in the Clubs page highlight cards.
    """

    most_represented = get_most_representation().iloc[0]
    most_valuable = get_valuable().iloc[0]
    top_contributor = get_club_goal_contributions().iloc[0]

    return {
        "most_represented": most_represented,
        "most_valuable": most_valuable,
        "top_contributor": top_contributor,
    }


def get_club_charts():
    """
    Returns datasets required by the Clubs page charts.
    """

    return {
        "goal_contributions": get_club_goal_contributions(),
        "minutes_played": get_minutes_played(),
        "most_representation": get_most_representation(),
        "valuable": get_valuable(),
    }


def get_club_tables():
    """
    Returns supporting club analysis tables.
    """

    return {
        "discipline": get_discipline(),
        "club_medals": get_club_medals(),
    }

def get_venue_summary():
    highest_scoring = get_venue_highest_scoring().iloc[0]
    busiest_venue = get_goals_per_venue().sort_values(
        "matches_hosted",
        ascending=False,
    ).iloc[0]
    highest_elevation = get_elevation_ranked().iloc[0]

    return {
        "highest_scoring": highest_scoring,
        "busiest_venue": busiest_venue,
        "highest_elevation": highest_elevation,
    }

def get_venue_charts():
    return {
        "goals_per_venue": get_goals_per_venue(),
        "match_day_style": get_average_stats(),
        "elevation_accuracy": get_elevation_accuracy(),
        "stage_distribution": get_stage_distribution(),
    }

def get_venue_tables():
    return {
        "directory": get_directory(),
        "highest_scoring": get_venue_highest_scoring(),
        "elevation_ranked": get_elevation_ranked(),
        "country_hosted": get_country_hosted(),
    }

def get_referee_summary():
    """
    Returns the headline referee highlights shown
    in the Referees page highlight cards.
    """

    most_used = get_matches_officiated().iloc[0]
    highest_fouls = get_fouls().iloc[0]
    highest_cards = get_card_comparison().iloc[0]

    return {
        "most_used": most_used,
        "highest_fouls": highest_fouls,
        "highest_cards": highest_cards,
    }

def get_referee_charts():
    """
    Returns datasets required by the Referees page charts.
    """

    return {
        "matches_officiated": get_matches_officiated(),
        "country_distribution": get_country_distribution(),
        "card_comparison": get_card_comparison(),
        "fouls": get_fouls(),
    }

def get_referee_tables():
    """
    Returns supporting referee analysis tables.
    """

    return {
        "red_cards": get_red_cards(),
        "stage_workload": get_stage_workload(),
    }