"""Return number of voyels for a lowercase string input"""


def count_voyels(s):
    return len([v for v in s if v in 'aoieu'])


def sum_voyels(s):
    return sum(1 for v in s if v in 'aoieu')


print(count_voyels("j'aime le paneng"))
print(sum_voyels("j'aime le paneng"))
