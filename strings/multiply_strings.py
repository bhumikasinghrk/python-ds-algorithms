

def multiply_strings(num1: str, num2: str) -> str:
    def string_to_int(string: str) -> int:
        length = len(string)
        zero = ord('0')
        value = 0

        for index in range(length):
            temp = ord(string[index]) - zero
            value += temp * (10 ** (length - index - 1))
        return value

    return str(string_to_int(num1) * string_to_int(num2))
