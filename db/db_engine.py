from pymongo import MongoClient
from pymongo import InsertOne
from pymongo import UpdateOne
from pymongo import ReplaceOne
import random
import time
import datetime


def timeFormat(timestamp):
    if type(timestamp) != int:
        print('%s is not type of int' % timestamp)
        return timestamp
    return datetime.datetime.fromtimestamp(
        timestamp).strftime("%Y-%m-%d %H:%M:%S")


# 连接mongdb数据库
client = MongoClient('mongodb://localhost:27017')

# 获取数据库db对象 库的名称 lottery
db = client.lottery

# 获取集合对象 表的名称 collection ==>
collection = db.participant

tempArr = []

t0 = time.time()

collection.remove({})

for i in range(3_487_665):
    t = int(time.time())
    a_code = str(random.randint(0, 10_000_000_000_000)).zfill(13)
    # check = collection.find({"a_code": a_code})
    # print("check 1: %s" % a_code)
    # while check.count() > 0:
    #     a_code = str(random.randint(0, 10_000_000_000_000)).zfill(13)
    #     check = collection.find({"a_code": a_code})
    # print("check 2: %s" % a_code)
    tempArr.append(
        InsertOne({
            "_id": i,
            "create_time": t,
            "beijing_time": timeFormat(t),
            "a_code": a_code
        }))
    if i % 2 ** 10 == 2 ** 10 - 1:
        collection.bulk_write(tempArr)
        tempArr = []
if len(tempArr) > 0:
    collection.bulk_write(tempArr)

msg = collection.find()

print('total: %d' % msg.count())


print('duration: %s' % (time.time() - t0))
