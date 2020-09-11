from pymongo import MongoClient
from pymongo import InsertOne

# 连接mongdb数据库
client = MongoClient('mongodb://localhost:27017')

# 获取数据库db对象 库的名称 lottery
db = client.lottery

# 获取集合对象 表的名称 collection ==>
collection = db.real_result

collection.remove({})

collection.insert_one({
    "lottery_time": "2016/06/26",
    "a_code": 2_707_639,
    "generation_time": "2016/06/24 22:25",
    "total_ids": 9_918_814,
    "winners": 13675,
    "winning_percent": 0.0014,
    "winner_ratio": 725.324607,
    "detail_data": [
        {"magnification": 1, "count": (514635, 731), "percentage": (
            0.19007, 0.05346), "winning_percent": (0.0014, 0.0014)},
        {"magnification": 2, "count": (526472, 1403), "percentage": (
            0.19444, 0.10260), "winning_percent": (0.0028, 0.0027)},
        {"magnification": 3, "count": (437333, 1802), "percentage": (
            0.16152, 0.13177), "winning_percent": (0.0041, 0.0041)},
        {"magnification": 4, "count": (295368, 1650), "percentage": (
            0.10909, 0.12066), "winning_percent": (0.0055, 0.0056)},
        {"magnification": 5, "count": (335800, 2293), "percentage": (
            0.12402, 0.16768), "winning_percent": (0.0069, 0.0068)},
        {"magnification": 6, "count": (248674, 2108), "percentage": (
            0.09184, 0.15415), "winning_percent": (0.0083, 0.0085)},
        {"magnification": 7, "count": (163430, 1527), "percentage": (
            0.06036, 0.11166), "winning_percent": (0.0097, 0.0093)},
        {"magnification": 8, "count": (130662, 1471), "percentage": (
            0.04826, 0.10757), "winning_percent": (0.0110, 0.0113)},
        {"magnification": 9, "count": (55236, 689), "percentage": (
            0.02040, 0.05038), "winning_percent": (0.0124, 0.0125)},
        {"magnification": 10, "count": (29, 1), "percentage": (
            0.00001, 0.0007), "winning_percent": (0.0138, 0.0345)}
    ]
})

collection.insert_one({
    "lottery_time": "2016/08/26",
    "a_code": 2_684_759,
    "generation_time": "2016/08/24 22:14",
    "total_ids": 10_026_318,
    "winners": 13674,
    "winning_percent": 0.00136,
    "winner_ratio": 733.239579,
    "detail_data": [
        {"magnification": 1, "count": (485800, 693), "percentage": (
            0.18095, 0.05068), "winning_percent": (0.00136, 0.00143)},
        {"magnification": 2, "count": (511891, 1394), "percentage": (
            0.19067, 0.10195), "winning_percent": (0.00273, 0.00272)},
        {"magnification": 3, "count": (444690, 1815), "percentage": (
            0.16564, 0.13273), "winning_percent": (0.00409, 0.00408)},
        {"magnification": 4, "count": (295761, 1642), "percentage": (
            0.11016, 0.12008), "winning_percent": (0.00546, 0.00555)},
        {"magnification": 5, "count": (319064, 2179), "percentage": (
            0.11884, 0.15935), "winning_percent": (0.00682, 0.00683)},
        {"magnification": 6, "count": (261469, 2152), "percentage": (
            0.09739, 0.15738), "winning_percent": (0.00818, 0.00823)},
        {"magnification": 7, "count": (166824, 1538), "percentage": (
            0.06214, 0.11248), "winning_percent": (0.00955, 0.00922)},
        {"magnification": 8, "count": (125602, 1369), "percentage": (
            0.04678, 0.10012), "winning_percent": (0.01091, 0.01090)},
        {"magnification": 9, "count": (73614, 891), "percentage": (
            0.02742, 0.06516), "winning_percent": (0.01227, 0.01210)},
        {"magnification": 10, "count": (36, 1), "percentage": (
            0.00001, 0.0007), "winning_percent": (0.01364, 0.02778)}
    ]
})

collection.insert_one({
    "lottery_time": "2016/10/26",
    "a_code": 2_692_690,
    "generation_time": "2016/10/26 10:11",
    "total_ids": 10_245_792,
    "winners": 13598,
    "winning_percent": 0.001327179,
    "winner_ratio": 753.477864,
    "detail_data": [
        {"magnification": 1, "count": (462696, 603), "percentage": (
            0.17183, 0.04439), "winning_percent": (0.001, 0.001)},
        {"magnification": 2, "count": (502896, 1350), "percentage": (
            0.18676, 0.09928), "winning_percent": (0.003, 0.003)},
        {"magnification": 3, "count": (459780, 1814), "percentage": (
            0.17075, 0.13340), "winning_percent": (0.004, 0.004)},
        {"magnification": 4, "count": (300310, 1627), "percentage": (
            0.11153, 0.11965), "winning_percent": (0.005, 0.005)},
        {"magnification": 5, "count": (304409, 2089), "percentage": (
            0.11305, 0.15363), "winning_percent": (0.007, 0.007)},
        {"magnification": 6, "count": (274952, 2113), "percentage": (
            0.10211, 0.15539), "winning_percent": (0.008, 0.008)},
        {"magnification": 7, "count": (168962, 1575), "percentage": (
            0.06275, 0.11583), "winning_percent": (0.009, 0.009)},
        {"magnification": 8, "count": (125978, 1307), "percentage": (
            0.04679, 0.09612), "winning_percent": (0.011, 0.010)},
        {"magnification": 9, "count": (92661, 1119), "percentage": (
            0.03441, 0.08229), "winning_percent": (0.012, 0.012)},
        {"magnification": 10, "count": (46, 1), "percentage": (
            0.00002, 0.0007), "winning_percent": (0.013, 0.022)}
    ]
})

collection.insert_one({
    "lottery_time": "2017/02/26",
    "a_code": 2_783_966,
    "generation_time": "2017/02/26 10:12",
    "total_ids": 10_961_022,
    "winners": 13905,
    "winning_percent": 0.001268586,
    "winner_ratio": 788.2791802,
    "detail_data": [
        {"magnification": 1, "count": (445844, 552), "percentage": (
            0.16015, 0.03979), "winning_percent": (0.0013, 0.0012)},
        {"magnification": 2, "count": (491419, 1328), "percentage": (
            0.17652, 0.09551), "winning_percent": (0.0025, 0.0027)},
        {"magnification": 3, "count": (477263, 1817), "percentage": (
            0.17143, 0.13067), "winning_percent": (0.0038, 0.0038)},
        {"magnification": 4, "count": (338198, 1694), "percentage": (
            0.12148, 0.12183), "winning_percent": (0.0051, 0.0050)},
        {"magnification": 5, "count": (280660, 1777), "percentage": (
            0.10081, 0.12780), "winning_percent": (0.0063, 0.0063)},
        {"magnification": 6, "count": (304737, 2236), "percentage": (
            0.10946, 0.16081), "winning_percent": (0.0076, 0.0073)},
        {"magnification": 7, "count": (188301, 1683), "percentage": (
            0.06764, 0.12104), "winning_percent": (0.0089, 0.0089)},
        {"magnification": 8, "count": (132298, 1387), "percentage": (
            0.04752, 0.09975), "winning_percent": (0.0101, 0.0105)},
        {"magnification": 9, "count": (112922, 1270), "percentage": (
            0.04056, 0.09133), "winning_percent": (0.0114, 0.0112)},
        {"magnification": 10, "count": (12316, 160), "percentage": (
            0.00442, 0.01151), "winning_percent": (0.0127, 0.0103)},
        {"magnification": 11, "count": (8, 0), "percentage": (
            0.00000, 0.0000), "winning_percent": (0.0140, 0.0000)},
    ]
})

collection.insert_one({
    "lottery_time": "2017/04/26",
    "a_code": 2_836_364,
    "generation_time": "2017/04/26 10:12",
    "total_ids": 11_337_568,
    "winners": 13883,
    "winning_percent": 0.001224513,
    "winner_ratio": 816.6511561,
    "detail_data": [
        {"magnification": 1, "count": (443249, 534), "percentage": (
            0.156274, 0.038464), "winning_percent": (0.0012, 0.0012)},
        {"magnification": 2, "count": (485242, 1151), "percentage": (
            0.171079, 0.082907), "winning_percent": (0.0024, 0.0024)},
        {"magnification": 3, "count": (480079, 1760), "percentage": (
            0.169259, 0.126774), "winning_percent": (0.0037, 0.0037)},
        {"magnification": 4, "count": (369788, 1838), "percentage": (
            0.130374, 0.132392), "winning_percent": (0.0049, 0.0050)},
        {"magnification": 5, "count": (272894, 1723), "percentage": (
            0.096213, 0.124109), "winning_percent": (0.0061, 0.0063)},
        {"magnification": 6, "count": (305284, 2183), "percentage": (
            0.107632, 0.157243), "winning_percent": (0.0073, 0.0072)},
        {"magnification": 7, "count": (200373, 1754), "percentage": (
            0.070644, 0.126342), "winning_percent": (0.0086, 0.0088)},
        {"magnification": 8, "count": (137299, 1355), "percentage": (
            0.048407, 0.097601), "winning_percent": (0.0098, 0.0099)},
        {"magnification": 9, "count": (114308, 1278), "percentage": (
            0.040301, 0.092055), "winning_percent": (0.0110, 0.0112)},
        {"magnification": 10, "count": (27831, 306), "percentage": (
            0.0009812, 0.022041), "winning_percent": (0.0122, 0.0110)},
        {"magnification": 11, "count": (17, 1), "percentage": (
            0.000006, 0.000072), "winning_percent": (0.0135, 0.0588)},
    ]
})

collection.insert_one({
    "lottery_time": "2017/06/26",
    "a_code": 2_867_632,
    "generation_time": "2017/06/26 10:12",
    "total_ids": 11_727_403,
    "winners": 13918,
    "winning_percent": 0.001187,
    "winner_ratio": 842.6069119,
    "detail_data": [
        {"magnification": 1, "count": (430070, 496), "percentage": (
            0.14997, 0.03564), "winning_percent": (0.00119, 0.00115)},
        {"magnification": 2, "count": (472668, 1182), "percentage": (
            0.16483, 0.08493), "winning_percent": (0.00237, 0.00250)},
        {"magnification": 3, "count": (473985, 1748), "percentage": (
            0.16529, 0.12559), "winning_percent": (0.00356, 0.00369)},
        {"magnification": 4, "count": (391291, 1910), "percentage": (
            0.13645, 0.13723), "winning_percent": (0.00475, 0.00488)},
        {"magnification": 5, "count": (271304, 1530), "percentage": (
            0.09461, 0.10993), "winning_percent": (0.00593, 0.00564)},
        {"magnification": 6, "count": (302530, 2132), "percentage": (
            0.10550, 0.15318), "winning_percent": (0.00712, 0.00705)},
        {"magnification": 7, "count": (220228, 1756), "percentage": (
            0.07680, 0.12617), "winning_percent": (0.00831, 0.00797)},
        {"magnification": 8, "count": (144733, 1387), "percentage": (
            0.05047, 0.09966), "winning_percent": (0.00949, 0.00958)},
        {"magnification": 9, "count": (114534, 1238), "percentage": (
            0.03994, 0.08895), "winning_percent": (0.01068, 0.01081)},
        {"magnification": 10, "count": (46267, 539), "percentage": (
            0.01613, 0.03873), "winning_percent": (0.01187, 0.01165)},
        {"magnification": 11, "count": (22, 0), "percentage": (
            0.00001, 0.00000), "winning_percent": (0.01305, 0.00000)},
    ]
})

collection.insert_one({
    "lottery_time": "2017/08/26",
    "a_code": 2_886_166,
    "generation_time": "2017/08/26 10:14",
    "total_ids": 11_893_449,
    "winners": 13923,
    "winning_percent": 0.001170644,
    "winner_ratio": 854.2303383,
    "detail_data": [
        {"magnification": 1, "count": (443249, 534), "percentage": (
            0.156274, 0.038464), "winning_percent": (0.0012, 0.0012)},
        {"magnification": 2, "count": (485242, 1151), "percentage": (
            0.171079, 0.082907), "winning_percent": (0.0024, 0.0024)},
        {"magnification": 3, "count": (480079, 1760), "percentage": (
            0.169259, 0.126774), "winning_percent": (0.0037, 0.0037)},
        {"magnification": 4, "count": (369788, 1838), "percentage": (
            0.130374, 0.132392), "winning_percent": (0.0049, 0.0050)},
        {"magnification": 5, "count": (272894, 1723), "percentage": (
            0.096213, 0.124109), "winning_percent": (0.0061, 0.0063)},
        {"magnification": 6, "count": (305284, 2183), "percentage": (
            0.107632, 0.157243), "winning_percent": (0.0073, 0.0072)},
        {"magnification": 7, "count": (200373, 1754), "percentage": (
            0.070644, 0.126342), "winning_percent": (0.0086, 0.0088)},
        {"magnification": 8, "count": (137299, 1355), "percentage": (
            0.048407, 0.097601), "winning_percent": (0.0098, 0.0099)},
        {"magnification": 9, "count": (114308, 1278), "percentage": (
            0.040301, 0.092055), "winning_percent": (0.0110, 0.0112)},
        {"magnification": 10, "count": (27831, 306), "percentage": (
            0.0009812, 0.022041), "winning_percent": (0.0122, 0.0110)},
        {"magnification": 11, "count": (17, 1), "percentage": (
            0.000006, 0.000072), "winning_percent": (0.0135, 0.0588)},
    ]
})

collection.insert_one({
    "lottery_time": "2017/10/26",
    "a_code": 2_836_463,
    "generation_time": "2017/10/26 10:14",
    "total_ids": 12_023_928,
    "winners": 13904,
    "winning_percent": 0.001156,
    "winner_ratio": 864.78,
    "detail_data": [
        {"magnification": 1, "count": (397041, 459), "percentage": (
            0.1400, 0.0330), "winning_percent": (0.0012, 0.0012)},
        {"magnification": 2, "count": (433501, 979), "percentage": (
            0.1528, 0.0704), "winning_percent": (0.0023, 0.0023)},
        {"magnification": 3, "count": (456277, 1555), "percentage": (
            0.1609, 0.1118), "winning_percent": (0.0035, 0.0034)},
        {"magnification": 4, "count": (412836, 1877), "percentage": (
            0.1455, 0.1350), "winning_percent": (0.0046, 0.0045)},
        {"magnification": 5, "count": (274432, 1646), "percentage": (
            0.0968, 0.1184), "winning_percent": (0.0058, 0.0060)},
        {"magnification": 6, "count": (277638, 1987), "percentage": (
            0.0979, 0.1429), "winning_percent": (0.0069, 0.0072)},
        {"magnification": 7, "count": (244833, 1908), "percentage": (
            0.0863, 0.1372), "winning_percent": (0.0081, 0.0078)},
        {"magnification": 8, "count": (150060, 1411), "percentage": (
            0.0529, 0.1015), "winning_percent": (0.0093, 0.0094)},
        {"magnification": 9, "count": (111079, 1195), "percentage": (
            0.0392, 0.0859), "winning_percent": (0.0104, 0.0108)},
        {"magnification": 10, "count": (78726, 887), "percentage": (
            0.0278, 0.0638), "winning_percent": (0.0116, 0.0113)},
        {"magnification": 11, "count": (40, 0), "percentage": (
            0.0000, 0.0000), "winning_percent": (0.0127, 0.0000)},
    ]
})

collection.insert_one({
    "lottery_time": "2017/12/26",
    "a_code": 2_839_459,
    "generation_time": "2017/12/26 10:14",
    "total_ids": 12_292_327,
    "winners": 13922,
    "winning_percent": 0.001133,
    "winner_ratio": 882.94,
    "detail_data": [
        {"magnification": 1, "count": (387956, 444), "percentage": (
            0.1366, 0.0319), "winning_percent": (0.0011, 0.0011)},
        {"magnification": 2, "count": (411403, 895), "percentage": (
            0.1449, 0.0643), "winning_percent": (0.0023, 0.0022)},
        {"magnification": 3, "count": (445357, 1480), "percentage": (
            0.1568, 0.1063), "winning_percent": (0.0034, 0.0033)},
        {"magnification": 4, "count": (416976, 1893), "percentage": (
            0.1469, 0.1360), "winning_percent": (0.0046, 0.0045)},
        {"magnification": 5, "count": (284474, 1597), "percentage": (
            0.1002, 0.1147), "winning_percent": (0.0057, 0.0056)},
        {"magnification": 6, "count": (266525, 1910), "percentage": (
            0.0939, 0.1372), "winning_percent": (0.0068, 0.0072)},
        {"magnification": 7, "count": (261457, 2017), "percentage": (
            0.0921, 0.1449), "winning_percent": (0.0079, 0.0077)},
        {"magnification": 8, "count": (156709, 1431), "percentage": (
            0.0552, 0.1028), "winning_percent": (0.0091, 0.0091)},
        {"magnification": 9, "count": (113871, 1142), "percentage": (
            0.0401, 0.0820), "winning_percent": (0.0102, 0.0100)},
        {"magnification": 10, "count": (94681, 1112), "percentage": (
            0.0333, 0.0799), "winning_percent": (0.0113, 0.0117)},
        {"magnification": 11, "count": (50, 1), "percentage": (
            0.0000, 0.0001), "winning_percent": (0.0125, 0.0200)},
    ]
})

collection.insert_one({
    "lottery_time": "2018/02/26",
    "a_code": 2_800_927,
    "generation_time": "2018/02/26 10:15",
    "total_ids": 12_320_966,
    "winners": 6460,
    "winning_percent": 0.000524,
    "winner_ratio": 1907.27,
    "detail_data": [
        {"magnification": 1, "count": (379818, 213), "percentage": (
            0.1356, 0.0330), "winning_percent": (0.0005, 0.0006)},
        {"magnification": 2, "count": (388552, 401), "percentage": (
            0.1387, 0.0621), "winning_percent": (0.0010, 0.0010)},
        {"magnification": 3, "count": (426907, 690), "percentage": (
            0.1524, 0.1068), "winning_percent": (0.0016, 0.0016)},
        {"magnification": 4, "count": (411820, 874), "percentage": (
            0.1470, 0.1353), "winning_percent": (0.0021, 0.0021)},
        {"magnification": 5, "count": (295541, 783), "percentage": (
            0.1055, 0.1212), "winning_percent": (0.0026, 0.0026)},
        {"magnification": 6, "count": (249724, 774), "percentage": (
            0.0892, 0.1198), "winning_percent": (0.0031, 0.0031)},
        {"magnification": 7, "count": (264804, 927), "percentage": (
            0.0945, 0.1435), "winning_percent": (0.0037, 0.0035)},
        {"magnification": 8, "count": (163383, 680), "percentage": (
            0.0583, 0.1053), "winning_percent": (0.0042, 0.0042)},
        {"magnification": 9, "count": (114509, 515), "percentage": (
            0.0409, 0.0797), "winning_percent": (0.0047, 0.0045)},
        {"magnification": 10, "count": (95844, 533), "percentage": (
            0.0342, 0.0825), "winning_percent": (0.0052, 0.0056)},
        {"magnification": 11, "count": (10019, 70), "percentage": (
            0.0036, 0.0108), "winning_percent": (0.0058, 0.0070)},
        {"magnification": 12, "count": (6, 0), "percentage": (
            0.0000, 0.0000), "winning_percent": (0.0063, 0.0000)},
    ]
})

collection.insert_one({
    "lottery_time": "2018/04/26",
    "a_code": 2_769_423,
    "generation_time": "2018/04/26 10:15",
    "total_ids": 12_430_084,
    "winners": 6333,
    "winning_percent": 0.000509,
    "winner_ratio": 1962.75,
    "detail_data": [
        {"magnification": 1, "count": (364601, 169), "percentage": (
            0.1317, 0.0267), "winning_percent": (0.0005, 0.0005)},
        {"magnification": 2, "count": (369000, 385), "percentage": (
            0.1332, 0.0608), "winning_percent": (0.0010, 0.0010)},
        {"magnification": 3, "count": (408085, 632), "percentage": (
            0.1474, 0.0998), "winning_percent": (0.0015, 0.0015)},
        {"magnification": 4, "count": (404082, 877), "percentage": (
            0.1459, 0.1385), "winning_percent": (0.0020, 0.0022)},
        {"magnification": 5, "count": (314476, 788), "percentage": (
            0.1136, 0.1244), "winning_percent": (0.0025, 0.0025)},
        {"magnification": 6, "count": (238124, 755), "percentage": (
            0.0860, 0.1192), "winning_percent": (0.0031, 0.0032)},
        {"magnification": 7, "count": (262427, 902), "percentage": (
            0.0948, 0.1424), "winning_percent": (0.0036, 0.0034)},
        {"magnification": 8, "count": (171590, 696), "percentage": (
            0.0620, 0.1099), "winning_percent": (0.0041, 0.0041)},
        {"magnification": 9, "count": (117224, 508), "percentage": (
            0.0423, 0.0802), "winning_percent": (0.0046, 0.0043)},
        {"magnification": 10, "count": (96917, 497), "percentage": (
            0.0350, 0.0785), "winning_percent": (0.0051, 0.0051)},
        {"magnification": 11, "count": (22883, 124), "percentage": (
            0.0083, 0.0196), "winning_percent": (0.0056, 0.0054)},
        {"magnification": 12, "count": (14, 0), "percentage": (
            0.0000, 0.0000), "winning_percent": (0.0061, 0.0000)},
    ]
})

collection.insert_one({
    "lottery_time": "2018/06/26",
    "a_code": 2_808_047,
    "generation_time": "2018/06/26 10:15",
    "total_ids": 12_859_766,
    "winners": 6333,
    "winning_percent": 0.000492,
    "winner_ratio": 2030.60,
    "detail_data": [
        {"magnification": 1, "count": (357098, 157), "percentage": (
            0.1272, 0.0248), "winning_percent": (0.0005, 0.0004)},
        {"magnification": 2, "count": (363183, 325), "percentage": (
            0.1293, 0.0513), "winning_percent": (0.0010, 0.0009)},
        {"magnification": 3, "count": (401153, 624), "percentage": (
            0.1429, 0.0985), "winning_percent": (0.0015, 0.0016)},
        {"magnification": 4, "count": (403153, 844), "percentage": (
            0.1438, 0.1333), "winning_percent": (0.0020, 0.0021)},
        {"magnification": 5, "count": (334122, 832), "percentage": (
            0.1190, 0.1314), "winning_percent": (0.0025, 0.0025)},
        {"magnification": 6, "count": (238043, 717), "percentage": (
            0.0848, 0.1132), "winning_percent": (0.0030, 0.0030)},
        {"magnification": 7, "count": (261247, 859), "percentage": (
            0.0930, 0.1356), "winning_percent": (0.0034, 0.0033)},
        {"magnification": 8, "count": (188760, 737), "percentage": (
            0.0672, 0.1164), "winning_percent": (0.0039, 0.0039)},
        {"magnification": 9, "count": (124229, 577), "percentage": (
            0.0442, 0.0911), "winning_percent": (0.0044, 0.0046)},
        {"magnification": 10, "count": (98088, 458), "percentage": (
            0.0349, 0.0723), "winning_percent": (0.0049, 0.0047)},
        {"magnification": 11, "count": (38223, 203), "percentage": (
            0.0136, 0.0321), "winning_percent": (0.0054, 0.0053)},
        {"magnification": 12, "count": (21, 0), "percentage": (
            0.0000, 0.0000), "winning_percent": (0.0059, 0.0000)},
    ]
})

collection.insert_one({
    "lottery_time": "2018/08/26",
    "a_code": 2_932_227,
    "generation_time": "2018/08/26 10:15",
    "total_ids": 13_603_346,
    "winners": 6333,
    "winning_percent": 0.000466,
    "winner_ratio": 2148.01,
    "detail_data": [
        {"magnification": 1, "count": (369142, 161), "percentage": (
            0.1259, 0.0248), "winning_percent": (0.0005, 0.0004)},
        {"magnification": 2, "count": (371715, 353), "percentage": (
            0.1268, 0.0513), "winning_percent": (0.0009, 0.0009)},
        {"magnification": 3, "count": (407283, 546), "percentage": (
            0.1389, 0.0985), "winning_percent": (0.0014, 0.0016)},
        {"magnification": 4, "count": (416415, 724), "percentage": (
            0.1420, 0.1333), "winning_percent": (0.0019, 0.0021)},
        {"magnification": 5, "count": (357288, 830), "percentage": (
            0.1218, 0.1314), "winning_percent": (0.0023, 0.0025)},
        {"magnification": 6, "count": (249747, 757), "percentage": (
            0.0852, 0.1132), "winning_percent": (0.0028, 0.0030)},
        {"magnification": 7, "count": (263758, 835), "percentage": (
            0.0900, 0.1356), "winning_percent": (0.0033, 0.0033)},
        {"magnification": 8, "count": (208610, 789), "percentage": (
            0.0711, 0.1164), "winning_percent": (0.0037, 0.0039)},
        {"magnification": 9, "count": (133910, 577), "percentage": (
            0.0457, 0.0911), "winning_percent": (0.0042, 0.0046)},
        {"magnification": 10, "count": (100011, 458), "percentage": (
            0.0341, 0.0723), "winning_percent": (0.0047, 0.0047)},
        {"magnification": 11, "count": (54219, 203), "percentage": (
            0.0185, 0.0321), "winning_percent": (0.0051, 0.0053)},
        {"magnification": 12, "count": (29, 0), "percentage": (
            0.0000, 0.0000), "winning_percent": (0.0056, 0.0000)},
    ]
})
