

def crop_string(string: str, new_length: int) -> str:
    length = len(string)
    last_valid_index = 0

    if length <= new_length:
        return string

    for i in range(new_length):
        if string[i] == ' ':
            last_valid_index = i

    return string[:last_valid_index]
