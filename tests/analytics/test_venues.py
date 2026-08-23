import pandas as pd

from src.analytics.venues import (
    get_average_stats,
    get_country_hosted,
    get_directory,
    get_elevation_accuracy,
    get_elevation_ranked,
    get_goals_per_venue,
    get_highest_scoring,
    get_stage_distribution,
)


def test_get_average_stats():
    df = get_average_stats()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty


def test_get_country_hosted():
    df = get_country_hosted()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty


def test_get_directory():
    df = get_directory()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty


def test_get_elevation_accuracy():
    df = get_elevation_accuracy()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty


def test_get_elevation_ranked():
    df = get_elevation_ranked()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty


def test_get_goals_per_venue():
    df = get_goals_per_venue()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty


def test_get_highest_scoring():
    df = get_highest_scoring()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty


def test_get_stage_distribution():
    df = get_stage_distribution()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty