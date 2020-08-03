# Strings

* [Valid Anagram](#valid-anagram)
* [First Unique Character](#first-unique-character-in-a-string)
* [Jewels and Stones](#jewels-and-stones)
* [Longest Common Prefix](#longest-common-prefix)
* [Reverse String](#reverse-string)
* [Valid Palindrome](#valid-palindrome)

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