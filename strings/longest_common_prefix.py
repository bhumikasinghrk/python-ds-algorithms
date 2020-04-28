from typing import List


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
