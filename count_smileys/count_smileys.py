"""Count vaid smileys from array of smileys"""


def count_smileys(arr):
    """Valid smiley sum"""

    enm = ((':', ';'), ('-', '~'), (')', 'D'))
    return sum(((x[0] in enm[0]) and
                (x[-1] in enm[-1]) and
                (x[1] in enm[1] if len(x) == 3 else 1))
               for x in arr)


"""Best practice"""

from re import findall


def count_smileys_nest(arr):
    """Count valid smileys"""

    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))
