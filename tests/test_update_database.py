from unittest.mock import patch

from src.update_database import main

def test_main_calls_build_database():
    with patch("src.update_database.build_database") as mock_build_database:
        main()

        mock_build_database.assert_called_once_with