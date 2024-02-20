def sum_digits(number: int) -> int:

    number_sum: int = 0
    number: int = abs(number)

    while number != 0:
        remainder = number % 10
        number_sum += remainder
        number //= 10

    return number_sum


def check(x: int, y: int, criteria: int) -> bool:

    return sum_digits(x) + sum_digits(y) <= criteria
