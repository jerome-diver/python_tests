"""Return sum of 3 or 5 multiples of number:
    n =10 ==> sum(3,5,6,9) = 23"""


def sum_of_multiples_3or5(number: int) -> list:
    """Sum of all multiples of 3 or 5 for number"""

    return sum(i for i in range(1, number + 1) if ((not i % 3) or (not i % 5)))


print("for 10 ==>", sum_of_multiples_3or5(10))
