

def string_to_integer_ii(string: str) -> int:
    zero = ord('0')
    positive = True
    length = len(string)
    start = 0
    number = 0

    if length < 1:
        return 0

    # Determine Positive / Negative
    if string[0] == '-':
        start = 1
        positive = False
    elif string[0] == '+':
        start = 1

    # Iterate over remaining characters
    for index in range(start, length):
        temp = ord(string[index]) - zero
        number += temp * (10 ** (length - index - 1))

    return number if positive else number * -1
