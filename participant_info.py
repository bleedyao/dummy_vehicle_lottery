import datetime
from time_util import timeFormat
import json


class ParticipantInfo:
    def __init__(self, id, applicationDate, applicationCode, rate):
        self.__id = id
        self.__applicationDate = applicationDate
        self.__applicationBeiJingTime = timeFormat(self.__applicationDate)
        self.__applicationCode = applicationCode
        self.__rate = rate
        self.__participantCount = 0
        self.__lotteryBaseId = []

    def __repr__(self):
        map = {'id': self.__id,
               'time': self.__applicationBeiJingTime,
               'code': self.__applicationCode,
               'rate': self.__rate,
               'base_id': self.__lotteryBaseId}
        return json.dumps(map)

    def __str__(self):
        map = {'id': self.__id,
               'time': self.__applicationBeiJingTime,
               'code': self.__applicationCode,
               'rate': self.__rate,
               'base_id': self.__lotteryBaseId}
        return json.dumps(map)

    def getId(self):
        return self.__id

    def getApplicationDate(self):
        return self.__applicationDate

    def getApplicationBeiJingDate(self):
        return self.__applicationBeiJingTime

    def getApplicationCode(self):
        return self.__applicationCode

    def getRate(self):
        return self.__rate

    def getParticipantCount(self):
        return self.__participantCount

    def setAppendLotteryBaseId(self, id):
        if len(self.__lotteryBaseId) < self.__rate:
            if id not in self.__lotteryBaseId:
                self.__lotteryBaseId.append(id)
            else:
                print('%s is exist, ignore this id' % id)
        else:
            print('lottery base id is enough')

    def getLotteryBaseId(self):
        return tuple(self.__lotteryBaseId)
