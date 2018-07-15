# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output: 321

def reverse_number(number:int):
    reversed = int(str(abs(number))[::-1])

    if reversed > 2**31 - 1:
        return 0

    if number < 0:
        return -reversed
    return reversed

def test_reverse_number():
    assert reverse_number(123) == 321

print(reverse_number(321))
print(reverse_number(1534236469))