from typing import List


def pascals_triangle(rows: int) -> List[List[int]]:
    output = []
    if rows <= 0:
        return output

    output.append([1])

    for i in range(1, rows):
        # Create row
        output.append([])
        # Set first 1
        output[i].append(1)

        # Constrain to values withing first and last index of row
        for col in range(1, i):
            # calculate value left value is left 1 col and right value is the same col
            output[i].append(output[i - 1][col - 1] + output[i - 1][col])

        # set last value
        output[i].append(1)
    return output
