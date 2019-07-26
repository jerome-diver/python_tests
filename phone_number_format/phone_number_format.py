"""from [0,1,2,3,4,5,6,7,8,9] format phone number: (012) 345-6789"""


def phone_number_format(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


print("[0,1,2,3,4,5,6,7,8,9] ==>", phone_number_format([0,1,2,3,4,5,6,7,8,9]))
