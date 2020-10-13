from typing import List


def reverse_words(sentence: str) -> str:
    def reverse(array: List[str], left: int, right: int):
        while left < right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

    length = len(sentence)
    sentence_array = list(sentence)
    left_index = 0

    for index in range(length):
        if sentence_array[index] == ' ':
            reverse(sentence_array, left_index, index - 1)
            left_index = index + 1

    # reverse last word, or sentence if one word
    reverse(sentence_array, left_index, length - 1)

    return ''.join(sentence_array)
