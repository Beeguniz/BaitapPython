def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def test_1():
    assert is_prime(1) == False

def test_2():
    assert is_prime(2) == True

def test_3():
    assert is_prime(3) == True

def test_4():
    assert is_prime(4) == False

def test_17():
    assert is_prime(17) == True

def test_18():
    assert is_prime(18) == False

def test_19():
    assert is_prime(19) == True