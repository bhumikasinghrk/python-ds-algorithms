

def valid_word_abbreviation(word: str, abbr: str) -> bool:
    num = ""
    abbr_index = 0
    word_index = 0
    abbr_length = len(abbr)
    length = len(word)

    while abbr_index < abbr_length:
        if num.startswith("0"):
            return False
        if abbr[abbr_index].isalpha():
            if len(num) != 0:
                word_index += int(num)
                num = ""
            if word_index >= length or word[word_index] != abbr[abbr_index]:
                return False
            word_index += 1
            abbr_index += 1
        else:
            num += abbr[abbr_index]
            abbr_index += 1

    if len(num) > 0:
        return length == word_index + int(num)

    return True
