from pathlib import Path

import pytest

from src.analytics.query_loader import load_query


def test_load_query_returns_sql_content(tmp_path, monkeypatch):
    sql_file = tmp_path / "test_query.sql"
    sql_file.write_text(
        "SELECT * FROM teams;",
        encoding="utf-8",
    )

    monkeypatch.setattr(
        "src.analytics.query_loader.SQL_DIRECTORY",
        tmp_path,
    )

    result = load_query("test_query.sql")

    assert result == "SELECT * FROM teams;"


def test_load_query_raises_error_for_missing_file(tmp_path, monkeypatch):
    monkeypatch.setattr(
        "src.analytics.query_loader.SQL_DIRECTORY",
        tmp_path,
    )

    with pytest.raises(FileNotFoundError):
        load_query("missing_query.sql")