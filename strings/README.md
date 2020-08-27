# Strings

* [Crop String](#crop-string)
* [First Unique Character](#first-unique-character-in-a-string)
* [Jewels and Stones](#jewels-and-stones)
* [Longest Common Prefix](#longest-common-prefix)
* [Multiply Strings](#multiply-strings)
* [Pangram](#pangram)
* [Reverse String](#reverse-string)
* [Run Length Encoding](#run-length-encoding)
* [String to Integer](#string-to-integer)
* [String to Integer II](#string-to-integer-ii)
* [Valid Anagram](#valid-anagram)
* [Valid Palindrome](#valid-palindrome)

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
def longest_common_prefix(strings: List[str]) -> str:
    if not strings or len(strings[0]) == 0:
        return ""

    longest = len(strings[0])
    current = 0

    while current < longest:
        for i in range(1, len(strings)):
            if len(strings[i]) == 0:
                return ""

            if len(strings[i]) < longest:
                longest = len(strings[i])
                if current > longest:
                    return strings[0][0:longest]

            if strings[0][current] != strings[i][current]:
                return strings[0][0:current]

        current += 1

    return strings[0][0:longest]
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
