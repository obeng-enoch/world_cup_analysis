import pandas as pd

from src.analytics.awards import (
    get_awards,
    get_man_of_the_match_players,
    get_man_of_the_match_teams,
    get_man_of_the_match_clubs,
)


def test_get_awards():
    df = get_awards()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty


def test_get_man_of_the_match_players():
    df = get_man_of_the_match_players()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty


def test_get_man_of_the_match_teams():
    df = get_man_of_the_match_teams()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty


def test_get_man_of_the_match_clubs():
    df = get_man_of_the_match_clubs()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty