# Strings

* [Add Binary](#add-binary)
* [Crop String](#crop-string)
* [First Unique Character](#first-unique-character-in-a-string)
* [Jewels and Stones](#jewels-and-stones)
* [Longest Common Prefix](#longest-common-prefix)
* [Longest Substring Without Duplicates](#longest-substring-without-duplicates)
* [Multiply Strings](#multiply-strings)
* [Pangram](#pangram)
* [Reverse String](#reverse-string)
* [Reverse Words In A Sentence](#reverse-words-in-a-sentence)
* [Reverse Words In A Sentence II](#reverse-words-in-a-sentence-ii)
* [Run Length Encoding](#run-length-encoding)
* [String to Integer](#string-to-integer)
* [String to Integer II](#string-to-integer-ii)
* [Valid Anagram](#valid-anagram)
* [Valid Palindrome](#valid-palindrome)
* [Valid Word Abbreviation](#valid-word-abbreviation)

## Add Binary

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: `"11", "1"`
Output: `"100"`
Example 2:

Input: `"1010", "1011"`
Output: `"10101"`

```python
def add_binary(num1: str, num2: str) -> str:
    length_a = len(num1)
    length_b = len(num2)
    max_length = max(length_a, length_b)
    output = deque()
    carry = 0

    num1 = ("0" * (max_length - length_a)) + num1
    num2 = ("0" * (max_length - length_b)) + num2

    for index in range(max_length - 1, -1, -1):
        if num1[index] == '1':
            carry += 1
        if num2[index] == '1':
            carry += 1

        if carry % 2 == 1:
            output.appendleft("1")
        else:
            output.appendleft("0")

        carry //= 2

    if carry == 1:
        output.appendleft('1')

    return ''.join(output)


def add_binary_with_builtins(num1: str, num2: str) -> str:
    return str(bin(int(num1, 2) + int(num2, 2)))[2:]
```

## Crop String

Crop a string of words separated by spaces. 

Return the longest string possible without; ending with white space and partial words

Input will not start or end with spaces

If rules cannot be met return an empty string

```python

def crop_string(string: str, new_length: int) -> str:
    length = len(string)
    last_valid_index = 0

    if length <= new_length:
        return string

    for i in range(new_length):
        if string[i] == ' ':
            last_valid_index = i

    return string[:last_valid_index]
```

## First Unique Character In A String

Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Example:

Input: `ilovecoding`
Output: `l`

```python
def first_unique_character_in_str(val: str) -> int:
    chars = {}

    for char in val:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    for index, char in enumerate(val):
        if chars[char] == 1:
            return index

    return -1
```

## Implement strStr

Implement `strStr()`.

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack. If needle is empty return 0


```python
def str_str(haystack: str, needle: str) -> int:
    if not needle:
        return 0

    length_haystack = len(haystack)
    length_needle = len(needle)

    for index in range(length_haystack):
        if haystack[index:index + length_needle] == needle:
            return index
    return -1
```

## Jewels and Stones

You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  
Each character in S is a type of stone you have. You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so 
"a" is considered a different type of stone from "A".

Example 1:

Input: `J = "aA"`, `S = "aAAbbbb"`
Output: `3`

```python
def jewels_and_stones(jewels: str, stones: str) -> int:
    stone_count = dict()
    
    for stone in stones:
        if stone in stone_count:
            stone_count[stone] += 1
        else:
            stone_count[stone] = 1

    count = 0
    jewel_set = set(jewels)

    for jewel in jewel_set:
        if jewel in stone_count:
            count += stone_count[jewel]

    return count
```

## Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: `["flower", "flow", "flight"]`
Output: `"fl"`

```python
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


# Slightly more optimal since it can exit earlier
def longest_common_prefix_vertical(strings: List[str]) -> str:
    if not strings:
        return ""

    length = len(strings)
    prefix = strings[0]

    for index in range(len(prefix)):
        for string_index in range(1, length):
            if index > len(prefix) - 1:
                return prefix
            if index > len(strings[string_index]) - 1:
                prefix = prefix[:len(strings[string_index])]
                continue
            if strings[string_index][index] != prefix[index]:
                prefix = strings[string_index][:index]

    return prefix

```

## Longest Substring Without Duplicates

Find the longest substring with unique characters

Example: `abcabedfg` -> `edfg`

```python
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
```

## Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

* The length of both num1 and num2 is < 110.
* Both num1 and num2 contain only digits 0-9.
* Both num1 and num2 do not contain any leading zero, except the number 0 itself.
* You must not use any built-in BigInteger library or convert the inputs to integer directly.

Input: `num1 = "123"`, `num2 = "456"`
Output: `"56088"`

```python
def multiply_strings(num1: str, num2: str) -> str:
    def string_to_int(string: str) -> int:
        length = len(string)
        zero = ord('0')
        value = 0

        for index in range(length):
            temp = ord(string[index]) - zero
            value += temp * (10 ** (length - index - 1))
        return value

    return str(string_to_int(num1) * string_to_int(num2))
```

## Pangram

Determine if a string has all characters a-z. Should handle uppercase, lowercase, whitespace, and special characters.

```python
def pangram(string: str) -> bool:
    alpha_set = set()

    for char in string:
        if char.isalpha():
            alpha_set.add(char.lower())

    return len(alpha_set) == 26
```

## Reverse String

Reverse a string

```python
def reverse_string(string: str) -> str:
    return string[::-1]

def reverse_string_in_place(string: [str]):
    index = 0
    length = len(string)
    middle = length / 2
    while index < middle:
        string[index], string[length - 1 - index] = string[length - 1 - index], string[index]
        index += 1

def reverse_string_with_list_comprehension(string: str) -> str:
    return ''.join([string[i] for i in range(len(string) - 1, -1, -1)])

def reverse_string_with_loop(string: str) -> str:
    reversed_str: List[Optional[str]] = [None] * len(string)
    for index in range(len(string) - 1, -1, -1):
        reversed_str[len(string) - 1 - index] = string[index]
    return ''.join(reversed_str)
```

## Reverse Words In A Sentence

Reverse the words in a sentence.

Input: `The fox is red`
Output: `ehT xof si der`

```python
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
```

## Reverse Words In A Sentence II

Reverse the order of the words in a sentence. Sentence will be an array of characters separated by spaces

Example:

Input: `["a", " ", "b", "o", "y"]`
Output: `["b", "o", "y", " ", "a"]`

```python
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
```

## Run Length Encoding

Perform run length encoding on an input string

Example: `"aaabbcddd"` -> `"a3b2cd3"`

```python
def run_length_encoding(string: str) -> str:
    counter = 0
    current_character = None
    output = []

    for character in string:
        if current_character == character:
            counter += 1
        else:
            if current_character:
                output.append(current_character + str(counter if counter > 1 else ''))
            current_character = character
            counter = 1

    if current_character:
        output.append(current_character + str(counter if counter > 1 else ''))

    return ''.join(output)
```

## String to Integer

Convert a string to an integer. String may include spaces before the number and after the number. String may end in words, these should be ignored.

```python
def string_to_integer(string: str) -> int:
    length = len(string)
    numbers = set(list('1234567890'))
    positive = True
    start_index = -1

    if length < 1:
        return 0

    for index in range(length):
        if string[index] in ' ':
            continue

        if string[index] in '-':
            positive = False
            continue

        if string[index] not in numbers:
            return 0

        if string[index] in numbers:
            start_index = index
            break

    # Handle empty string (no numbers)
    if start_index is -1:
        return 0

    end_index = start_index

    for index in range(start_index, length):
        if string[index] in numbers:
            end_index += 1
        else:
            break

    return int(string[start_index: end_index]) if positive else -int(string[start_index: end_index])
```

## String to Integer II

Convert a number string to an integer. Number may be prefixed by `-` or `+`

Example: 
- `"-34"` -> `-34`
- `"100"` -> `100`

```python
def string_to_integer_ii(string: str) -> int:
    zero = ord('0')
    positive = True
    length = len(string)
    start = 0
    number = 0

    if length < 1:
        return 0

    # Determine Positive / Negative
    if string[0] == '-':
        start = 1
        positive = False
    elif string[0] == '+':
        start = 1

    # Iterate over remaining characters
    for index in range(start, length):
        temp = ord(string[index]) - zero
        number += temp * (10 ** (length - index - 1))

    return number if positive else number * -1
```

## Valid Anagram

Given two strings, write a function to determine if string A is an anagram of B.

Example:

`star, rats` -> `True`

```python
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
```

## Valid Palindrome

A string that is the same forwards and backwards. 2nd solution accounts for punctuation characters

```python
def valid_palindrome_naive(s: str) -> bool:
    return s == s[::-1]


def valid_palindrome(string: str) -> bool:
    length = len(string)

    if length < 2:
        return True

    start = 0
    end = length - 1

    normalized_string = string.lower()

    while start < end:
        if not normalized_string[start].isalnum():
            start += 1
            continue

        if not normalized_string[end].isalnum():
            end -= 1
            continue

        if normalized_string[start] is not normalized_string[end]:
            return False

        start += 1
        end -= 1

    return True
```

## Valid Word Abbreviation

Given a non-empty and an abbreviation, return whether the string matches with the given abbreviation.

A string such as "word" contains only the following valid abbreviations:

`["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]`
Notice that only the above abbreviations are valid abbreviations of the string "word". Any other string is not a valid abbreviation of "word".

Note:
Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.

Example:

Input: `"internationalization"`, `abbr = "i12iz4n"`:
Output: `True`

Input: `word = "apple"`, `abbr = "a2e"`
Output: `False`

```python
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
```