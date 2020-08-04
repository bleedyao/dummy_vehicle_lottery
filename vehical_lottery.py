import random
import time
from decorator import running_time


def start_lottery():
    pass


class RandomInformation:
    def __init__(self):
        self.__registerIds = []
        self.__maxNumber = 10_000

    def randomApplicationCode(self, seed=-1):
        '''随机生产13位数字字符串'''
        tempStr = ''
        if seed > 0:
            random.seed(seed)
        while len(self.__registerIds) < self.__maxNumber - 1:
            tempStr = str(random.randint(1, self.__maxNumber)
                          ).zfill(13)
            if tempStr in self.__registerIds:
                continue
            else:
                self.__registerIds.append(tempStr)
                break
        return tempStr

    @running_time
    def findMe(self):
        temp = ''
        while temp != '0000000006741':
            temp = self.randomApplicationCode()
            print(temp)
        print('find my code: %s' % temp)
        print('registered code length: %d' % (len(self.__registerIds)))

    def idGenerater(self, id=0):
        while True:
            id += 1
            yield id


if __name__ == "__main__":
    RandomInformation().findMe()
