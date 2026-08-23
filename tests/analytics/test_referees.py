import pandas as pd

from src.analytics.referees import (
    get_fouls,
    get_matches_officiated,
    get_red_cards,
    get_country_distribution,
    get_card_comparison,
    get_stage_workload,
)


def test_get_fouls():
    df = get_fouls()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty


def test_get_matches_officiated():
    df = get_matches_officiated()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty


def test_get_red_cards():
    df = get_red_cards()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty


def test_get_country_distribution():
    df = get_country_distribution()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty


def test_get_card_comparison():
    df = get_card_comparison()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty


def test_get_stage_workload():
    df = get_stage_workload()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty