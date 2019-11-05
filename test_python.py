from math import pi, sqrt, pow, hypot

def test_filter():
    assert list(filter(lambda x: x%2==0, [1, 2, 3, 4, 5])) == [2, 4]
    assert list(filter(lambda x: x!='a' and x!='e', ['a', 'b', 'c', 'd', 'e'])) == ['b', 'c', 'd']

def test_map():
    assert list(map(lambda x: x*2, [1, 2, 3, 4, 5])) == [2, 4, 6, 8, 10]
    assert list(map(lambda x: str(x), [1, 2, 3, 4, 5])) == ['1', '2', '3', '4', '5']

def test_sorted():
    assert sorted([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert sorted([5, 10000, 3, 200, 1]) == [1, 3, 5, 200, 10000]
    assert sorted([1, 2, 3, 4, 5], reverse=True) == [5, 4, 3, 2, 1]

def test_math_pi():
    assert pi == 3.141592653589793

def test_math_sqrt():
    assert sqrt(1) == 1
    assert sqrt(4) == 2
    assert sqrt(16) == 4
    assert sqrt(10000) == 100

def test_math_pow():
    assert pow(1, 20) == 1
    assert pow(2, 2) == 4
    assert pow(2, 9) == 512
    assert pow(8, 3) == 512

def test_math_hypot():
    assert hypot(4, 5) == 6.4031242374328485
    assert hypot(1, 3) == 3.1622776601683795
    assert hypot(13, 15) == 19.849433241279208
