import pandas as pd

from src.analytics.events import get_event_counts


def test_get_event_counts():
    df = get_event_counts()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty