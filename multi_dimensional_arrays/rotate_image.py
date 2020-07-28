

def rotate_image_90_degrees(matrix: [[int]]) -> [[int]]:
    size = len(matrix)
    layer_count = int(size / 2)

    for layer in range(0, layer_count):
        last = size - layer - 1

        for element in range(layer, last):
            offset = element - layer

            top = matrix[layer][element]
            right_side = matrix[element][last]
            bottom = matrix[last][last - offset]
            left_side = matrix[last - offset][layer]

            matrix[layer][element] = left_side
            matrix[element][last] = top
            matrix[last][last - offset] = right_side
            matrix[last - offset][layer] = bottom
    return matrix
