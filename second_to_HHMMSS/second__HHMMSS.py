"""from seconds, get back timing HH::MM::SS"""


def seconds_tp_hhmmss(seconds):
    """transforms seconds delay to HH:MM::SS"""

    return '{:02}:{:02}:{:02}'.format(seconds // 3600,
                                      seconds // 60 % 60,
                                      seconds % 60)
