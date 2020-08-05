import random
import time
from decorator import running_time


def start_lottery():
    pass


class RandomInformation:
    def __init__(self, maxNumber=10_000_000_000_000):
        if maxNumber > 10_000_000_000_000:
            maxNumber = 10_000_000_000_000
        elif maxNumber < 0:
            maxNumber = 0
        self.__maxNumber = maxNumber
        self.__applicationCodePool = [str(i).zfill(13)
                                      for i in range(1, self.__maxNumber + 1)]

    def randomApplicationCode(self, seed=-1):
        '''随机生产13位数字字符串'''
        if len(self.__applicationCodePool) > 0:
            if seed > 0:
                random.seed(seed)
            return self.__applicationCodePool.pop(random.randint(0, len(self.__applicationCodePool) - 1))
        else:
            raise Exception('Application code is not enough')

    @running_time
    def findMe(self):
        temp = ''
        while temp != '0000000006741':
            temp = self.randomApplicationCode()
            print(temp)
        print('find my code: %s' % temp)
        print('registered code length: %d' % (len(self.__applicationCodePool)))

    def idGenerater(self, id=0):
        while True:
            id += 1
            yield id


if __name__ == "__main__":
    RandomInformation().findMe()
