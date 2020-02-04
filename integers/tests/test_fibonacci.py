from integers.fibonacci import fibonacci, fibonacci2, fibonacci3, fibonacci_sequence


def test_fibonacci():
    assert fibonacci(6) == 8
    assert fibonacci(0) == 0


def test_fibonacci2():
    assert fibonacci2(6) == 8
    assert fibonacci2(0) == 0


def test_fibonacci3():
    assert fibonacci3(6) == 8
    assert fibonacci3(0) == 0


def test_fibonacci_sequence():
    assert list(fibonacci_sequence(6)) == [0, 1, 1, 2, 3, 5, 8]
    assert list(fibonacci_sequence(0)) == [0]
