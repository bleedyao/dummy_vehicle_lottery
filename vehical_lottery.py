import random
import time
from decorator import running_time


def start_lottery():
    pass


class RandomInformation:
    def __init__(self, maxNumber=10_000_000_000_000, seed=-1):
        if maxNumber > 10_000_000_000_000:
            maxNumber = 10_000_000_000_000
        elif maxNumber < 0:
            maxNumber = 0
        self.__maxNumber = maxNumber
        self.__applicationCodePool = dict()
        self.__seed = seed
        self.__randomMinNumber = 0
        self.__randomMaxNumber = self.__maxNumber

    def randomApplicationCode(self):
        '''随机生产13位数字字符串'''
        if len(self.__applicationCodePool) >= self.__maxNumber:
            raise Exception('Application code is not enough')
        if self.__seed > 0:
            random.seed(self.__seed)
        temp = None
        while temp in self.__applicationCodePool.keys() or temp == None:
            temp = random.choice(
                range(self.__randomMinNumber, self.__randomMaxNumber))
            if temp <= self.__randomMinNumber and self.__randomMinNumber < self.__randomMaxNumber:
                self.__randomMinNumber += 1
            elif temp >= self.__randomMaxNumber-1 and self.__randomMinNumber < self.__randomMaxNumber:
                self.__randomMaxNumber -= 1
            # print(self.__randomMinNumber, self.__randomMaxNumber)
        else:
            self.__applicationCodePool[temp] = None
            return str(temp).zfill(13)

    def getMaxNumber(self):
        return self.__maxNumber

    def idGenerater(self, id=0):
        while True:
            id += 1
            yield id