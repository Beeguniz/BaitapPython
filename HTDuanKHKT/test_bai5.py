from unittest.mock import patch, Mock
import requests

def fetch_user():
    response = requests.get("https://api.example.com/user")
    return response.json()


def test_fetch_user():
    mock_response = Mock()
    mock_response.json.return_value = {"name": "John", "age": 30}

    with patch("requests.get", return_value=mock_response) as mock_get:
        result = fetch_user()


        assert result == {"name": "John", "age": 30}


        mock_get.assert_called_once_with("https://api.example.com/user")