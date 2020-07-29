

def valid_anagram(val1: str, val2: str) -> bool:
    if len(val1) != len(val2):
        return False

    char_counter = {}

    for char in val1:
        if char in char_counter:
            char_counter[char] += 1
        else:
            char_counter[char] = 1

    for char in val2:
        if char in char_counter:
            char_counter[char] -= 1
        else:
            return False

    for result in char_counter.values():
        if result != 0:
            return False
    return True
