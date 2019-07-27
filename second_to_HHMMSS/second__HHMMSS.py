"""from seconds, get back timing HH::MM::SS"""


def seconds_tp_hhmmss(seconds):
    """transforms seconds delay to HH:MM::SS"""

    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)

