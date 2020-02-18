

def decode_string(value: str) -> str:
    stack = []
    for char in value:
        if char != ']':
            stack.append(char)
        else:
            temp_string, num = '', ''
            while stack and stack[-1] != '[':
                temp_string = stack.pop() + temp_string

            stack.pop()
            while stack and stack[-1].isdigit():
                num = stack.pop() + num

            num = int(num)
            stack.append(temp_string * num)

    return ''.join(stack)
