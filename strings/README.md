# Strings

* [Jewels and Stones](#jewels-and-stones)
* [Longest Common Prefix](#longest-common-prefix)
* [Reverse String](#reverse-string)

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