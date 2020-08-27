from typing import List


def reverse_words(sentence: str) -> str:
    sentence_array = list(sentence)
    length = len(sentence)
    left = 0

    if length < 2:
        return sentence

    def reverse(array: List[str], start: int, end: int):
        left_index = start
        right_index = end

        while left_index < right_index:
            array[left_index], array[right_index] = array[right_index], array[left_index]
            left_index += 1
            right_index -= 1

    for index in range(1, length):
        if sentence_array[index - 1] == ' ':
            reverse(sentence_array, left, index - 2)
            left = index

    # reverse last word, or sentence if one word
    reverse(sentence_array, left, length - 1)

    return ''.join(sentence_array)
