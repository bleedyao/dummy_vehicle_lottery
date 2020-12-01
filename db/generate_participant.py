from pymongo import MongoClient
from pymongo import InsertOne
import datetime
import time
import random 
import functools

def timeFormat(timestamp):
    if type(timestamp) != int:
        print('%s is not type of int' % timestamp)
        return timestamp
    return datetime.datetime.fromtimestamp(
        timestamp).strftime("%Y-%m-%d %H:%M:%S")

t0 = time.time()

# 连接mongdb数据库
client = MongoClient('mongodb://localhost:27017')


# 获取数据库db对象 库的名称 lottery
db = client.lottery

# 查询所有集合名字
collection_list = db.list_collection_names()

buffer_data = []
tempDict = {}
# 获取集合对象 表的名称 collection ==>
collection = db.real_result

# 获取集合中的所有数据
msg = collection.find({})

# 排序
list_msg = list(msg)
list_msg.sort(key=functools.cmp_to_key(lambda x,y: -1 if x["a_code"] > y["a_code"] else 1))

db.participant.remove({})
index = 0
max = [0,]
while len(list_msg):
    lottery_result = list_msg.pop()
    print("date: %s, person_count: %s"%(lottery_result['lottery_time'], lottery_result['a_code']))
    detail_data = lottery_result['detail_data']
    for i in detail_data:
        temp = 0
        if i['magnification'] in tempDict:
           temp = tempDict[i['magnification']] 
        tempDict[i['magnification']] = i['count'][0] - temp
        if tempDict[i['magnification']] > max[0]:
            max = [i['magnification'], tempDict[i['magnification']]]
    # for i in range(1, 15):
    #     if i in tempDict:
    #         print(tempDict[i])
    if db.participant.count() < lottery_result['a_code']:
        # 10000 用于测试，正式数据需要删除
        while index < lottery_result['a_code']:
            t = int(time.time())
            a_code = str(random.randint(0, 10_000_000_000_000)).zfill(13)
            while a_code in tempDict.keys():
                a_code = str(random.randint(0, 10_000_000_000_000)).zfill(13)
            # 预添数据
            buffer_data.append(
                InsertOne({
                    "_id": index,
                    "create_time": t,
                    "beijing_time": timeFormat(t),
                    "a_code": a_code,
                    "rate": max[0]
                }))
            if tempDict[max[1]] > 0:
                tempDict[max[1]] -= 1
            else:
                max -= 1
            
            # print(tempDict[max])
            if index % 2 ** 10 == 2 ** 10 - 1:
                # print('max: %s'%max)
                db.participant.bulk_write(buffer_data)
                buffer_data = []
            index += 1
        if len(buffer_data) > 0:
            # print('max: %s'%max)
            db.participant.bulk_write(buffer_data)
            buffer_data = []

print('duration: %s' % (time.time() - t0))