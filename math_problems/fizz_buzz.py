from typing import List


def fizz_buzz(iterations: int) -> List[str]:
    output = []

    if iterations and iterations < 0:
        return output

    for num in range(1, iterations + 1):
        three = num % 3 == 0
        five = num % 5 == 0
        if three and five:
            output.append('FizzBuzz')
        elif three:
            output.append('Fizz')
        elif five:
            output.append('Buzz')
        else:
            output.append(f'{num}')

    return output
