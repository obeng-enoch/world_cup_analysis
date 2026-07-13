from src.build_database import build_database

def main() -> None:
    """Run the World Cup ETL pipeline."""

    build_database()

if __name__ == "__main__":
    main()
