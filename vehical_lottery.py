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
        self.__applicationCodePool = dict()

    @running_time
    def randomApplicationCode(self, seed=-1):
        '''随机生产13位数字字符串'''
        if len(self.__applicationCodePool) >= self.__maxNumber:
            raise Exception('Application code is not enough')
        if seed > 0:
            random.seed(seed)
        tempStr = str(random.choice(range(self.__maxNumber))).zfill(13)
        while tempStr in self.__applicationCodePool:
            self.__applicationCodePool[tempStr] = self.__applicationCodePool[tempStr] + 1
            tempStr = str(random.choice(range(self.__maxNumber))).zfill(13)
        else:
            self.__applicationCodePool[tempStr] = 1
            return tempStr

    @running_time
    def __findMe(self):
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
    RandomInformation().__findMe()
