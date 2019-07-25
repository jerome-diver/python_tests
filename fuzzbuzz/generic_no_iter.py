"""FizzBuzz without iteration"""


def fizzbuzz(fizz, buzz, start_, end_):
    """ Fizz or Buzz or FizzBuzz or n"""

    condition = lambda x, y: (x % y == 0)
    fizz_buzz = lambda x: (condition(x, fizz), condition(x, buzz))
    for i in range(start_, end_ + 1):
        valid = ((not i % fizz), (not i % buzz))
        if valid == (False, False):
            print(i)
        else:
            print(f"{'Fizz' if valid[0] else ''}{'Buzz' if valid[1] else ''}")

fizzbuzz(3,5,1,100)

