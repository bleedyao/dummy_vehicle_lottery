import functools
import time
from time_util import hmsTransfor


def running_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        temp = func(*args, **kwargs)
        end = time.time()
        print('run time: %s' % (end-start))
        return temp
    return wrapper


def delay_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        temp = func(*args, **kwargs)
        end = time.time()
        print('delay time: %s' % (end-start))
        return temp
    return wrapper


@running_time
def __test():
    print('test')


if __name__ == "__main__":
    __test()
