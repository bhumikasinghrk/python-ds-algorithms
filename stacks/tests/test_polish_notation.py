from stacks.polish_notation import evaluate_rpn


def test_evaluate_reverse_polish_notation():
    assert evaluate_rpn(["2", "1", "+", "3", "*"]) == 9
    assert evaluate_rpn(["4", "13", "5", "/", "+"]) == 6
    assert evaluate_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
