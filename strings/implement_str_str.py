

def str_str(haystack: str, needle: str) -> int:
    if not needle:
        return 0

    length_haystack = len(haystack)
    length_needle = len(needle)

    for index in range(length_haystack):
        if haystack[index:index + length_needle] == needle:
            return index
    return -1
