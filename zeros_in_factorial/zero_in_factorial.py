"""Find zero trailing digits in result of factorial x"""


# too slow
def zeros_1(num):
    """Trailing zeros in !num"""

    return sum(num // 5 ** x for x in range(1, num + 1))


# too slow
def zeros_2(num):

    return num * (5 - (x // 5 ** num)) // 20


# solution
def zero_3(num):

    x = num/5
    return x + zeros_3(x) if x else 0


def zero_4(num)

    return 0 if num < 5 else num/5 + zeros_4(num/5)
