

def run_length_encoding(string: str) -> str:
    counter = 0
    current_character = None
    output = []

    for character in string:
        if current_character == character:
            counter += 1
        else:
            if current_character:
                output.append(current_character + str(counter if counter > 1 else ''))
            current_character = character
            counter = 1

    if current_character:
        output.append(current_character + str(counter if counter > 1 else ''))

    return ''.join(output)
