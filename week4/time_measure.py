import contextlib
import timeit
from time import sleep


@contextlib.contextmanager
def time_measure_of(f):
    try:
        yield timeit.Timer('f()', globals=locals()).timeit(number=1)
    finally:
        pass


def foo():
    sleep(3)


if __name__ == '__main__':
    with time_measure_of(foo) as t:
        print(t)
