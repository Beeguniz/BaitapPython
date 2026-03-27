import pytest

def is_strong(password):
    return len(password) >= 8 and any(c.isdigit() for c in password)


@pytest.mark.parametrize("password, expected", [
    ("abc12", False),       # ngắn
    ("abcdefgh", False),    # không có số
    ("abc12345", True),     # hợp lệ
    ("password1", True),    # hợp lệ
    ("12345678", True),     # toàn số vẫn OK
    ("", False),            # rỗng
])
def test_is_strong(password, expected):
    assert is_strong(password) == expected