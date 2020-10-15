from typing import List


def pascals_triangle_ii(row_index: int) -> List[int]:
    row = [1]

    # Generate a row by adding numbers right to left  ([i] + [i - 1])
    # then append a closing 1

    for i in range(row_index):
        for j in range(i, 0, -1):
            row[j] = row[j] + row[j - 1]
        row.append(1)

    return row
