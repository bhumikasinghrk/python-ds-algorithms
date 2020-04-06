from math_problems.power_of_three import power_of_three


def test_power_of_three():
    assert power_of_three(9)
    assert power_of_three(1162261467)
    assert not power_of_three(2)
    assert not power_of_three(0)
