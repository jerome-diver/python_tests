""" mask with # but all last 4"""


def maskify(cc):
    return "#" * (len(cc) - 4) + cc[-4:]


def maskify_2(cc):
    return cc[-4:].rjust(len(cc), "#")
