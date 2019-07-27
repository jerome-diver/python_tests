"""FizzBuzz without iteration"""


def fizzbuzz(fizz, buzz, start_, end_):
    """ Fizz or Buzz or FizzBuzz or n"""

    for i in range(start_, end_ + 1):
        answer = i if ((not i % fizz), (not i % buzz))
                else f"{'Fizz' if valid[0] else ''}"
                     f"{'Buzz' if valid[1] else ''}"
        print(answer)


fizzbuzz(3,5,1,100)

