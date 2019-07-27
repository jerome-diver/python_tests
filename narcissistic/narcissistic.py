"""find if numberrcissistic:
    1634 => 1^4  + 6^4 + 3^4 + 4^4 = 1634 ?"""


def narcissistic( value ):
    """find Narcissistic number"""

    return value == sum(int(x)**len(str(value)) for x in str(value))

