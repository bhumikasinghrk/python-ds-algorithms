# Matrices

* [Diagonal Traverse](#diagonal-traverse)
* [Rotate Image 90 Degrees Clockwise](#rotate-image-90-degrees-clockwise)
* [Spiral Matrix](#spiral-matrix)

## Diagonal Traverse

Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order.

Input:
```
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
```
Output: `1, 2, 4, 7, 5, 3, 6, 8, 9`

```python
def diagonal_traverse(matrix: List[List[int]]) -> List[int]:
    result = []
    temp = []  # to reverse odd rows

    if not matrix or not matrix[0]:
        return result

    height, length = len(matrix), len(matrix[0])
    diagonals = range(height + length - 1)

    for diagonal in diagonals:
        row = 0 if diagonal < length else diagonal - length + 1
        col = diagonal if diagonal < length else length - 1

        while row < height and col > -1:
            temp.append(matrix[row][col])
            row += 1
            col -= 1

        if diagonal % 2 == 0:
            result.extend(temp[::-1])
        else:
            result.extend(temp)
        temp.clear()

    return result
```


## Rotate Image 90 Degrees Clockwise

Note: Try to solve this task in-place (with O(1) additional memory), since this is what you'll be asked to do during
an interview.

You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

Input:
```
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
```

Output:
```
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]
```     

```python
def rotate_image_90_degrees(a: [[int]]) -> [[int]]:
    size = len(a)
    layer_count = int(size / 2)

    for layer in range(0, layer_count):
        first = layer
        last = size - first - 1

        for element in range(first, last):
            offset = element - first

            top = a[first][element]
            right_side = a[element][last]
            bottom = a[last][last - offset]
            left_side = a[last - offset][first]

            a[first][element] = left_side
            a[element][last] = top
            a[last][last - offset] = right_side
            a[last - offset][first] = bottom
    return a
```

## Spiral Matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
```
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
```
Output: `[1,2,3,6,9,8,7,4,5]`

```python
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
```
