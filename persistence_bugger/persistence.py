"""search persistence number which is occurence
of unit product possible:
    999 => 9 *9*9 = 729 (1)
    729 => 7*2*9 = 126 (2=
    126 => 1*2*6 = 12 (3)
    12 => 1*2 (4)
    4 is the unique unit
    persistence is 4"""


from operator import mul
from functools import reduce


def persistence(number):
    """Find persistencei number"""

    return 0 if number < 10 else persistence(
        reduce(mul, [int(i) for i in str(number)], 1))+1


print("999 =>", persistence(999))


persist = lambda n,c=0: persist(reduce(lambda x,y:int(x)*int(y),str(n)),c+1) if n >=10 else c


print("999 =>", persist(999))
