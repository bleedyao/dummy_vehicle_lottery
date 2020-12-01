import random
import time
from decorator import running_time


class SessionInfo:
    def __init__(self, id=0, descript='', validCount=0, totalWins=0):
        self.__id = id
        self.__descript = descript
        self.__startTime = 0
        self.__endTime = 0
        self.__duration = 0
        self.__validApplictionCodeCount = validCount
        # 总中奖人数（中签总数）
        self.__totalWins = totalWins
        self.__seed = random.randint(0, 999_999)

    def getId(self):
        return self.__id

    def getDescript(self):
        return self.__descript

    def setStartTime(self, second):
        if type(second) != int or second < 0:
            second = 0
        self.__startTime = second

    def getStartTime(self):
        return self.__startTime

    def setEndTime(self, second):
        if type(second) != int or second < self.__startTime:
            second = self.__startTime
        self.__endTime = second

    def getEndTime(self):
        return self.__endTime

    def getDuration(self):
        return self.__endTime - self.__startTime

    def getValidApplictionCodeCount(self):
        return self.__validApplictionCodeCount

    def getTotalWins(self):
        return self.__totalWins

    def getSeed(self):
        return self.__seed


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


@running_time
def testArr():
    arr = []
    for i in range(19_580_861):
        arr.append(random.randint(0, 10_000_000_000_000))
    len(arr)


if __name__ == "__main__":
    testArr()
