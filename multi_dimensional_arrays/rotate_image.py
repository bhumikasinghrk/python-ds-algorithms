# Note: Try to solve this task in-place (with O(1) additional memory), since this is what you'll be asked to do during
# an interview.
#
# You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).
# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]

# rotateImage(a) =
#    [[7, 4, 1],
#     [8, 5, 2],
#     [9, 6, 3]]


def rotate_image_90_degrees(arr: [[int]]) -> [[int]]:
    size = len(arr)
    layer_count = int(size / 2)

    for layer in range(0, layer_count):
        first = layer
        last = size - first - 1

        for element in range(first, last):
            offset = element - first

            top = arr[first][element]
            right_side = arr[element][last]
            bottom = arr[last][last - offset]
            left_side = arr[last - offset][first]

            arr[first][element] = left_side
            arr[element][last] = top
            arr[last][last - offset] = right_side
            arr[last - offset][first] = bottom
    return arr
