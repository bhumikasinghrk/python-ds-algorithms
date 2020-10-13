from typing import List


def reverse_words_ii(sentence: List[str]):
    def reverse(string: List[str], left: int, right: int):
        while left < right:
            string[left], string[right] = string[right], string[left]
            left += 1
            right -= 1

    length = len(sentence)
    reverse(sentence, 0, length - 1)
    left_index = None

    for index in range(length):
        if left_index is None and sentence[index] != " ":
            left_index = index
        if sentence[index] == " ":
            reverse(sentence, left_index, index - 1)
            left_index = None

    if left_index is not None:
        reverse(sentence, left_index, length - 1)
