from typing import List


def spiral_matrix(matrix: List[List[int]]) -> List[int]:
    if not matrix or not matrix[0]:
        return []

    output = []
    srow = 0
    scol = 0
    opprow = len(matrix) - 1
    oppcol = len(matrix[0]) - 1

    while srow <= opprow and scol <= oppcol:
        # Loop through top row, Offset opposite column for 0 based indexing
        for col in range(scol, oppcol + 1):
            output.append(matrix[srow][col])

        # Offset first row since the value was added in the loop above
        # Offset opposite row to account for 0 based indexing
        for row in range(srow + 1, opprow + 1):
            output.append(matrix[row][oppcol])

        # Shortcut for matrices that are just rows, columns
        if srow < opprow and scol < oppcol:
            # note: reversed ranges are offset by one on the end
            # Iterate backwards across bottom row
            for col in range(oppcol - 1, scol, -1):
                output.append(matrix[opprow][col])

            # Iterate up left side
            # Do not offset range since first value was apart of the first row
            for row in range(opprow, srow, -1):
                output.append(matrix[row][scol])

        # Move start position in by 1 and end position in by 1
        srow += 1
        scol += 1
        opprow -= 1
        oppcol -= 1

    return output
