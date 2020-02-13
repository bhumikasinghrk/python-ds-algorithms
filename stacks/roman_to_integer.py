ROMAN_NUMERALS = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def roman_to_integer(roman: str) -> int:
    number = 0
    accumulator = []

    for index in range(len(roman) - 1, -1, -1):
        if accumulator and ROMAN_NUMERALS[accumulator[-1]] > ROMAN_NUMERALS[roman[index]]:
            number += ROMAN_NUMERALS[accumulator.pop()] - ROMAN_NUMERALS[roman[index]]
        else:
            accumulator.append(roman[index])
    while accumulator:
        number += ROMAN_NUMERALS[accumulator.pop()]

    return number
