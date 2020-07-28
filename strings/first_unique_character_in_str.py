

def first_unique_character_in_str(val: str) -> int:
    chars = {}

    for char in val:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    for index, char in enumerate(val):
        if chars[char] == 1:
            return index

    return -1
