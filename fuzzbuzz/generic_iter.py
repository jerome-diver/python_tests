"""FizzBuzz generic with iterator"""


def fizzbuzz(fizz, buzz, start_, end_):
    """Fizz or Buzz or FizzBuzz or i"""

    def iter_fb(fizz, buzz, start_, end_):
        for i in range(start_, end_ + 1):
            fizz_buzz = f"{'Fizz' if (not i % fizz) else ''}"\
                        f"{'Buzz' if (not i % buzz) else''}"
            yield fizz_buzz or str(i)
            
    print('\n'.join(iter_fb(fizz, buzz, start_, end_)))

fizzbuzz(3, 5, 1, 100)
