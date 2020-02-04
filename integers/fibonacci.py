from functools import lru_cache
from typing import Dict, Generator


def fibonacci(number: int, memo: Dict[int, int] = None) -> int:
    """
    Generate the fibonacci number for n
    Uses a dictionary to store previously computed values

    0, 1, 1, 2, 3, 5, 8, 13, .... 0 = 0 , 1 = 1, 3 = 2, etc
    :param number: iteration of the Fibonacci sequence
    :param memo: memoization store, will be cached since it is mutable
    :return: Fibonacci number
    """

    if not memo:
        memo = {0: 0, 1: 1}

    if number not in memo:
        memo[number] = fibonacci(number - 1, memo) + fibonacci(number - 2, memo)

    return memo[number]


@lru_cache(maxsize=None)
def fibonacci2(number: int) -> int:
    """
    Generate the fibonacci number for n
    Utilizes caching to mimic literal memoization, has lower recursive limit...

    0, 1, 1, 2, 3, 5, 8, 13, .... 0 = 0 , 1 = 1, 3 = 2, etc
    :param number: iteration of the Fibonacci sequence
    :return: Fibonacci number
    """
    if number < 2:
        return number
    return fibonacci2(number - 1) + fibonacci2(number - 2)


def fibonacci3(number: int) -> int:
    """
    Generate the fibonacci number for n
    iterative approach, no recursion constraints

    0, 1, 1, 2, 3, 5, 8, 13, .... 0 = 0 , 1 = 1, 3 = 2, etc
    :param number: iteration of the Fibonacci sequence
    :return: Fibonacci number
    """

    if number == 0:
        return 0
    last_nbr: int = 0
    next_nbr: int = 1

    for _ in range(1, number):
        last_nbr, next_nbr = next_nbr, last_nbr + next_nbr

    return next_nbr


def fibonacci_sequence(number: int) -> Generator[int, None, None]:
    """
    Generate the fibonacci number for n
    Utilizes a generator

    0, 1, 1, 2, 3, 5, 8, 13, .... 0 = 0 , 1 = 1, 3 = 2, etc
    :param number: iteration of the Fibonacci sequence
    :return: Fibonacci number Generator
    """

    yield 0
    if number > 0:
        yield 1

    last_nbr: int = 0
    next_nbr: int = 1

    for _ in range(1, number):
        last_nbr, next_nbr = next_nbr, last_nbr + next_nbr
        yield next_nbr
