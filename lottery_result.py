from vehical_lottery import SessionInfo


def printLotteryResult(sessionInfo: SessionInfo):
    print('虚拟小客车摇号结果展示')
    print('期号:\t\t%s' % sessionInfo.getId())
    print('描述:\t\t第1组数据，第1期虚拟小客车摇号结果')
    print('开始时间:\t%s' % sessionInfo.getStartTime())
    print('结束时间:\t%s' % sessionInfo.getEndTime())
    print('持续时间:\t%s' % sessionInfo.getDuration())
    print('有效编码总数:\t%s' % sessionInfo.getValidApplictionCodeCount())
    print('中奖总数:\t%s' % sessionInfo.getTotalWins())
    print('随机种子数:\t%s' % sessionInfo.getSeed())
    print()
    print('序号 ---> 摇号基数序号 ----> 申请编码')
    print('1 ----> 6676649 ----> 0486106556966')
    print('2 ----> 14595052 ----> 5422103493799')


# if __name__ == "__main__":
    # printLotteryResult(÷)
