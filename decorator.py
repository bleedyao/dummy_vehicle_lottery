import functools
import time


def running_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        temp = func(*args, **kwargs)
        end = time.time()
        print('run total time: %f' % (end-start))
        return temp
    return wrapper


@running_time
def __test():
    print('test')


if __name__ == "__main__":
    __test()
