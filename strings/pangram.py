

def pangram(string: str) -> bool:
    alpha_set = set()

    for char in string:
        if char.isalpha():
            alpha_set.add(char.lower())

    return len(alpha_set) == 26
