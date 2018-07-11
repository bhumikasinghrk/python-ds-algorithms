# Note: Try to solve this task in-place (with O(1) additional memory), since this is what you'll be asked to do during
# an interview.
#
# You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).
# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]

#rotateImage(a) =
#    [[7, 4, 1],
#     [8, 5, 2],
#     [9, 6, 3]]
def rotateImage90degrees(a):
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



def test_rotateImage90Degrees():
    a = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

    b = [[7, 4, 1],
         [8, 5, 2],
         [9, 6, 3]]

    assert rotateImage90degrees(a) == b

# Solve for rotating by one element
#def rotateImage(a):