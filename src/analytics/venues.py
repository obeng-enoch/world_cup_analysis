from src.analytics.database import get_dataframe

def get_average_stats():
    return get_dataframe("venues/average_stats.sql")

def get_country_hosted():
    return get_dataframe("venues/country_hosted.sql")

def get_directory():
    return get_dataframe("venues/directory.sql")

def get_elevation_accuracy():
    return get_dataframe("venues/elevation_accuracy.sql")

def get_elevation_ranked():
    return get_dataframe("venues/elevation_ranked.sql")

def get_goals_per_venue():
    return get_dataframe("venues/goals_per_venue.sql")

def get_highest_scoring():
    return get_dataframe("venues/highest_scoring.sql")

def get_stage_distribution():
    return get_dataframe("venues/stage_distribution.sql")