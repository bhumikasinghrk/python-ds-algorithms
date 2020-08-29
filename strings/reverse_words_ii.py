from typing import List


def reverse_words_ii(sentence: List[str]):
    def reverse(string: List[str], start_index: int, end_index: int):
        left = start_index
        right = end_index
        while left < right:
            string[left], string[right] = string[right], string[left]
            left += 1
            right -= 1

    length = len(sentence)
    reverse(sentence, 0, length - 1)
    start = None

    for index in range(length - 1):
        if start is None and sentence[index] != " ":
            start = index
        if sentence[index + 1] == " ":
            reverse(sentence, start, index)
            start = None

    if start is not None:
        reverse(sentence, start, length - 1)
