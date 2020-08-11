from vehical_lottery import RandomInformation
from vehical_lottery import SessionInfo
from participant_info import ParticipantInfo
import time
import random
import functools


def start_lottery():
    session = SessionInfo(1, '第一期摇号结果', 10000, 2)
    randomInfo = RandomInformation(seed=session.getSeed())
    # 创建参与者
    pool = []
    for i in range(session.getValidApplictionCodeCount()):
        pool.append(ParticipantInfo(i, int(time.time()),
                                    randomInfo.randomApplicationCode(), random.randint(1, 14)))
    # 根据申请嘛排序

    def sortApplicationCode(x, y):
        return -1 if x.getApplicationCode() < y.getApplicationCode() else 1
    pool = sorted(pool, key=functools.cmp_to_key(sortApplicationCode))
    # 分配摇号基数序列
    tempId = 0
    for i in range(1, 15):
        for j in pool:
            if j.getRate() >= i:
                tempId += 1
                j.setAppendLotteryBaseId(tempId)
    # for i in pool:
        # print(i.getLotteryBaseId(), i.getRate())
    # 摇号结果
    resultPool = []
    random.seed(session.getSeed())
    while len(resultPool) < session.getTotalWins():
        randomCode = random.randint(1, tempId)
        for i in pool:
            if randomCode in i.getLotteryBaseId() and randomCode not in resultPool:
                resultPool.append(i)
    for i in resultPool:
        print(i)


if __name__ == "__main__":
    start_lottery()
