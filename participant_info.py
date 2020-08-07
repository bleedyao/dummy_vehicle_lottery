import datetime


class ParticipantInfo:
    def __init__(self, id, applicationDate, applicationCode, rate):
        self.__id = id
        self.__applicationDate = applicationDate
        self.__applicationBeiJingTime = datetime.datetime.fromtimestamp(
            self.__applicationDate).strftime("%Y-%m-%d %H:%M:%S")
        self.__applicationCode = applicationCode
        self.__rate = rate
        self.__participantCount = 0

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
