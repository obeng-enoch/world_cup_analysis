from src.analytics.database import get_dataframe


def get_conversion_rate():
    return get_dataframe("tactical/conversion_rate.sql")

def get_fouls_to_cards():
    return get_dataframe("tactical/fouls_to_cards.sql")

def get_offsides():
    return get_dataframe("tactical/offsides.sql")

def get_positional_discipline():
    return get_dataframe("tactical/pos_discipline.sql")

def get_possession():
    return get_dataframe("tactical/possession.sql")

def get_shooting():
    return get_dataframe("tactical/shooting.sql")

def get_bench_usage():
    return get_dataframe("tactical/used_bench.sql")