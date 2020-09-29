

def longest_substring_without_duplicates(string: str) -> int:
    length = len(string)
    if length <= 1:
        return length
    left_index = 0
    right_index = 0
    longest = 0

    unique = set()

    while right_index < length and left_index < length:
        if string[right_index] not in unique:
            unique.add(string[right_index])
            right_index += 1
            longest = max(longest, right_index - left_index)
        else:
            unique.remove(string[left_index])
            left_index += 1
    return longest
