
import datetime


def timeFormat(timestamp):
    if type(timestamp) != int:
        print('%s is not type of int' % timestamp)
        return timestamp
    return datetime.datetime.fromtimestamp(
        timestamp).strftime("%Y-%m-%d %H:%M:%S")


def hmsTransfor(seconds):
    if type(seconds) != int:
        print('%s is not type of int' % seconds)
        return seconds
    elif seconds < 0:
        print('%s must be positive' % seconds)
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "%02d小时:%02d分:%02d秒" % (h, m, s)
