import pandas as pd

from src.analytics.tactical import (
    get_conversion_rate,
    get_fouls_to_cards,
    get_offsides,
    get_positional_discipline,
    get_possession,
    get_shooting,
    get_bench_usage,
)


def test_get_conversion_rate():
    df = get_conversion_rate()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty


def test_get_fouls_to_cards():
    df = get_fouls_to_cards()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty


def test_get_offsides():
    df = get_offsides()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty


def test_get_positional_discipline():
    df = get_positional_discipline()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty


def test_get_possession():
    df = get_possession()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty


def test_get_shooting():
    df = get_shooting()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty


def test_get_bench_usage():
    df = get_bench_usage()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty