"""Match password with:
_6 chars or more
_alphanumeric only
_allmost one lowercase char
_allmost one uppercase char
_allmost one numeric char"""


REGEX = r'^(?=.*[a-z])'\
         '(?=.*[A-Z])'\
         '(?=.*\d)'\
         '[^\W_]{6,}$'
