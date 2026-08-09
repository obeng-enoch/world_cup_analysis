import pandas as pd

from src.analytics.clubs import (
    get_club_medals,
    get_discipline,
    get_goal_contributions,
    get_minutes_played,
    get_most_representation,
    get_valuable,
)


def validate_dataframe(name: str, df: pd.DataFrame) -> None:
    print("\n" + "=" * 80)
    print(f"{name.upper()}")
    print("=" * 80)

    # Basic shape
    print(f"\nShape: {df.shape}")

    # Column names
    print("\nColumns:")
    print(df.columns.tolist())

    # First five records
    print("\nFirst 5 records:")
    print(df.head())

    # Data types
    print("\nData types:")
    print(df.dtypes)

    # Null values
    print("\nNull values:")
    print(df.isnull().sum())

    # Duplicate rows
    print("\nDuplicate rows:")
    print(df.duplicated().sum())

    # Numeric summary
    numeric_columns = df.select_dtypes(include="number").columns

    if len(numeric_columns) > 0:
        print("\nNumeric summary:")
        print(df[numeric_columns].describe())

    # Ranking order
    print("\nFirst 10 rows:")
    print(df.head(10).to_string(index=False))


def main():
    datasets = {
        "Club Medals": get_club_medals(),
        "Club Discipline": get_discipline(),
        "Club Goal Contributions": get_goal_contributions(),
        "Club Minutes Played": get_minutes_played(),
        "Most Represented Clubs": get_most_representation(),
        "Most Valuable Clubs": get_valuable(),
    }

    for name, df in datasets.items():
        validate_dataframe(name, df)


if __name__ == "__main__":
    main()
