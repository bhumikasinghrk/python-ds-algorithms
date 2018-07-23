from multi_dimensional_arrays.rotate_image import rotate_image_90_degrees


def test_rotate_image_90_degrees():
    a = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

    b = [[7, 4, 1],
         [8, 5, 2],
         [9, 6, 3]]

    assert rotate_image_90_degrees(a) == b
