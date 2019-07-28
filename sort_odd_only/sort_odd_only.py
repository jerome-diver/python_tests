"""From a int list, sort odd only, don't change even number position"""


def sort_array(arr):
    """Sort odd only"""

    odds = sorted((x for x in arr if x % 2), reverse=True)
    return [x if not x % 2 else odds.pop() for x in arr]
