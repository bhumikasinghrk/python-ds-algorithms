from typing import List


def longest_common_prefix_horizontal(strings: List[str]) -> str:
    if not strings or len(strings[0]) == 0:
        return ""

    length = len(strings)
    longest = strings[0]

    for index in range(1, length):
        last_match = -1  # slices empty string if no match
        for char_index, value in enumerate(strings[index]):
            # If word is longer than longest word or characters do not match break and update last match
            if char_index >= len(longest) or longest[char_index] != value:
                break
            last_match = char_index
        # Add 1 to end index since last index in slice is exclusive
        longest = strings[index][0:last_match + 1]
    return longest


def longest_common_prefix_vertical(strings: List[str]) -> str:
    if not strings:
        return ""

    length = len(strings)
    prefix = strings[0]
    prefix_length = len(prefix)

    for index in range(prefix_length):
        for string_index in range(1, length):
            if index > len(prefix) - 1:
                return prefix
            if index > len(strings[string_index]) - 1:
                prefix = prefix[:len(strings[string_index])]
                continue
            if strings[string_index][index] != prefix[index]:
                prefix = strings[string_index][:index]

    return prefix
