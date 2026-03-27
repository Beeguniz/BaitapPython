import pytest

def clean_input(s):
    return s.strip().lower().replace(" ", "_")


@pytest.mark.parametrize("input_str, expected", [
    ("  hello  ", "hello"),             # trim
    ("HELLO", "hello"),                 # lowercase
    ("hello world", "hello_world"),     # space → _
    ("hello   world", "hello___world"), # nhiều space
    ("  HELLO WORLD  ", "hello_world"), # full combo
])
def test_clean_input(input_str, expected):
    assert clean_input(input_str) == expected