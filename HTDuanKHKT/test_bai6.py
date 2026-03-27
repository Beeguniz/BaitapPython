from unittest.mock import patch
from datetime import datetime

def is_weekend():
    today = datetime.now().weekday()
    return today >= 5


def test_friday():
    with patch("__main__.datetime") as mock_datetime:
        mock_datetime.now.return_value.weekday.return_value = 4
        assert is_weekend() == False


def test_saturday():
    with patch("__main__.datetime") as mock_datetime:
        mock_datetime.now.return_value.weekday.return_value = 5
        assert is_weekend() == True