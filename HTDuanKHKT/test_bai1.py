def calculate_tax(income):
    if income < 5000:
        return 0
    elif income < 10000:
        return income * 0.1
    else:
        return income * 0.2


def test_income_less_than_5000():
    assert calculate_tax(4000) == 0


def test_income_7000():
    assert calculate_tax(7000) == 700


def test_income_12000():
    assert calculate_tax(12000) == 2400