# Note: Write a solution that only iterates over the string once and uses O(1) additional memory, since this is what you
# would be asked to do during a real interview.
#
# Given a string s, find and return the first instance of a non-repeating character in it.
# If there is no such character, return '_'.


def first_not_repeating_character(string: str) -> str:
    length = len(string)
    index = 0
    while index < length:
        if string[index] not in string[:index] and string[index] not in string[index + 1:]:
            return string[index]
        index += 1
    return '_'


def first_not_repeating_character_set(string: str) -> str:
    checked_characters = set()  # skip characters we've already checked.
    for char in string:
        if char not in checked_characters and string.index(char) == string.rindex(char):
            return char
        checked_characters.add(char)
    return '_'
