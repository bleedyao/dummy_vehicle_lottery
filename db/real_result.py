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
            0.1259, 0.0254), "winning_percent": (0.0005, 0.0004)},
        {"magnification": 2, "count": (371715, 353), "percentage": (
            0.1268, 0.0557), "winning_percent": (0.0009, 0.0009)},
        {"magnification": 3, "count": (407283, 546), "percentage": (
            0.1389, 0.0862), "winning_percent": (0.0014, 0.0013)},
        {"magnification": 4, "count": (416415, 724), "percentage": (
            0.1420, 0.1143), "winning_percent": (0.0019, 0.0017)},
        {"magnification": 5, "count": (357288, 830), "percentage": (
            0.1218, 0.1311), "winning_percent": (0.0023, 0.0023)},
        {"magnification": 6, "count": (249747, 751), "percentage": (
            0.0852, 0.1186), "winning_percent": (0.0028, 0.0030)},
        {"magnification": 7, "count": (263758, 835), "percentage": (
            0.0900, 0.1318), "winning_percent": (0.0033, 0.0032)},
        {"magnification": 8, "count": (208610, 789), "percentage": (
            0.0711, 0.1246), "winning_percent": (0.0037, 0.0038)},
        {"magnification": 9, "count": (133910, 600), "percentage": (
            0.0457, 0.0947), "winning_percent": (0.0042, 0.0045)},
        {"magnification": 10, "count": (100011, 450), "percentage": (
            0.0341, 0.0711), "winning_percent": (0.0047, 0.0045)},
        {"magnification": 11, "count": (54319, 294), "percentage": (
            0.0185, 0.0464), "winning_percent": (0.0051, 0.0054)},
        {"magnification": 12, "count": (29, 0), "percentage": (
            0.0000, 0.0000), "winning_percent": (0.0056, 0.0000)},
    ]
})

collection.insert_one({
    "lottery_time": "2018/10/26",
    "a_code": 3_003_201,
    "generation_time": "2018/10/26 10:15",
    "total_ids": 14_123_942,
    "winners": 6402,
    "winning_percent": 0.000453,
    "winner_ratio": 2206.18,
    "detail_data": [
        {"magnification": 1, "count": (372571, 161), "percentage": (
            0.1241, 0.0283), "winning_percent": (0.0005, 0.0005)},
        {"magnification": 2, "count": (374140, 331), "percentage": (
            0.1268, 0.0517), "winning_percent": (0.0009, 0.0009)},
        {"magnification": 3, "count": (403137, 548), "percentage": (
            0.1342, 0.0856), "winning_percent": (0.0014, 0.0014)},
        {"magnification": 4, "count": (419793, 760), "percentage": (
            0.1398, 0.1187), "winning_percent": (0.0018, 0.0018)},
        {"magnification": 5, "count": (377295, 845), "percentage": (
            0.1256, 0.1320), "winning_percent": (0.0023, 0.0022)},
        {"magnification": 6, "count": (258198, 678), "percentage": (
            0.0860, 0.1059), "winning_percent": (0.0027, 0.0026)},
        {"magnification": 7, "count": (260805, 868), "percentage": (
            0.0868, 0.1356), "winning_percent": (0.0032, 0.0033)},
        {"magnification": 8, "count": (225100, 774), "percentage": (
            0.0750, 0.1209), "winning_percent": (0.0036, 0.0034)},
        {"magnification": 9, "count": (139241, 587), "percentage": (
            0.0464, 0.0917), "winning_percent": (0.0041, 0.0042)},
        {"magnification": 10, "count": (102927, 488), "percentage": (
            0.0343, 0.0762), "winning_percent": (0.0045, 0.0047)},
        {"magnification": 11, "count": (69957, 341), "percentage": (
            0.0233, 0.0533), "winning_percent": (0.0050, 0.0049)},
        {"magnification": 12, "count": (37, 1), "percentage": (
            0.0000, 0.0002), "winning_percent": (0.0054, 0.0200)},
    ]
})

collection.insert_one({
    "lottery_time": "2018/12/26",
    "a_code": 3_060_913,
    "generation_time": "2018/12/26 10:15",
    "total_ids": 14_620_617,
    "winners": 6413,
    "winning_percent": 0.000439,
    "winner_ratio": 2279.84,
    "detail_data": [
        {"magnification": 1, "count": (368604, 159), "percentage": (
            0.1204, 0.0247), "winning_percent": (0.0004, 0.0004)},
        {"magnification": 2, "count": (378516, 335), "percentage": (
            0.1236, 0.0522), "winning_percent": (0.0008, 0.0008)},
        {"magnification": 3, "count": (395895, 494), "percentage": (
            0.1293, 0.0770), "winning_percent": (0.0013, 0.0012)},
        {"magnification": 4, "count": (421280, 753), "percentage": (
            0.1376, 0.1174), "winning_percent": (0.0017, 0.0017)},
        {"magnification": 5, "count": (390309, 876), "percentage": (
            0.1275, 0.1366), "winning_percent": (0.0021, 0.0022)},
        {"magnification": 6, "count": (270565, 692), "percentage": (
            0.0883, 0.1079), "winning_percent": (0.0026, 0.0025)},
        {"magnification": 7, "count": (254430, 760), "percentage": (
            0.0831, 0.1185), "winning_percent": (0.0030, 0.0029)},
        {"magnification": 8, "count": (242707, 854), "percentage": (
            0.0792, 0.1331), "winning_percent": (0.0035, 0.0035)},
        {"magnification": 9, "count": (146739, 583), "percentage": (
            0.0479, 0.0909), "winning_percent": (0.0039, 0.0039)},
        {"magnification": 10, "count": (106670, 468), "percentage": (
            0.0348, 0.0729), "winning_percent": (0.0043, 0.0043)},
        {"magnification": 11, "count": (85152, 439), "percentage": (
            0.0278, 0.0684), "winning_percent": (0.0048, 0.0051)},
        {"magnification": 12, "count": (46, 0), "percentage": (
            0.0002, 0.0000), "winning_percent": (0.0052, 0.0000)},
    ]
})

collection.insert_one({
    "lottery_time": "2019/02/26",
    "a_code": 3_135_548,
    "generation_time": "2019/02/26 10:15",
    "total_ids": 15_175_162,
    "winners": 6412,
    "winning_percent": 0.000423,
    "winner_ratio": 2366.68,
    "detail_data": [
        {"magnification": 1, "count": (366313, 134), "percentage": (
            0.1168, 0.0209), "winning_percent": (0.0004, 0.0004)},
        {"magnification": 2, "count": (393233, 335), "percentage": (
            0.1254, 0.0522), "winning_percent": (0.0008, 0.0009)},
        {"magnification": 3, "count": (392314, 512), "percentage": (
            0.1251, 0.0799), "winning_percent": (0.0013, 0.0013)},
        {"magnification": 4, "count": (420923, 744), "percentage": (
            0.1342, 0.1160), "winning_percent": (0.0017, 0.0018)},
        {"magnification": 5, "count": (401460, 831), "percentage": (
            0.1280, 0.1296), "winning_percent": (0.0021, 0.0021)},
        {"magnification": 6, "count": (289818, 750), "percentage": (
            0.0924, 0.1170), "winning_percent": (0.0025, 0.0026)},
        {"magnification": 7, "count": (246670, 710), "percentage": (
            0.0787, 0.1107), "winning_percent": (0.0030, 0.0029)},
        {"magnification": 8, "count": (254959, 868), "percentage": (
            0.0813, 0.1354), "winning_percent": (0.0034, 0.0034)},
        {"magnification": 9, "count": (158392, 638), "percentage": (
            0.0505, 0.0995), "winning_percent": (0.0038, 0.0040)},
        {"magnification": 10, "count": (111652, 438), "percentage": (
            0.0356, 0.0683), "winning_percent": (0.0042, 0.0039)},
        {"magnification": 11, "count": (90643, 404), "percentage": (
            0.0289, 0.0630), "winning_percent": (0.0046, 0.0045)},
        {"magnification": 12, "count": (9165, 48), "percentage": (
            0.0029, 0.0075), "winning_percent": (0.0051, 0.0052)},
        {"magnification": 13, "count": (6, 0), "percentage": (
            0.0000, 0.0000), "winning_percent": (0.0055, 0.0000)},
    ]
})

collection.insert_one({
    "lottery_time": "2019/04/26",
    "a_code": 3_209_304,
    "generation_time": "2019/04/26 10:15",
    "total_ids": 15_707_277,
    "winners": 6379,
    "winning_percent": 0.000406,
    "winner_ratio": 2462.34,
    "detail_data": [
        {"magnification": 1, "count": (377533, 166), "percentage": (
            0.1176, 0.0260), "winning_percent": (0.0004, 0.0004)},
        {"magnification": 2, "count": (398433, 336), "percentage": (
            0.1241, 0.0527), "winning_percent": (0.0008, 0.0008)},
        {"magnification": 3, "count": (388518, 481), "percentage": (
            0.1211, 0.0754), "winning_percent": (0.0012, 0.0012)},
        {"magnification": 4, "count": (417118, 684), "percentage": (
            0.1300, 0.1072), "winning_percent": (0.0016, 0.0016)},
        {"magnification": 5, "count": (406237, 803), "percentage": (
            0.1266, 0.1259), "winning_percent": (0.0020, 0.0020)},
        {"magnification": 6, "count": (316003, 757), "percentage": (
            0.0985, 0.1187), "winning_percent": (0.0024, 0.0024)},
        {"magnification": 7, "count": (242635, 695), "percentage": (
            0.0756, 0.1090), "winning_percent": (0.0028, 0.0029)},
        {"magnification": 8, "count": (260527, 818), "percentage": (
            0.0812, 0.1282), "winning_percent": (0.0032, 0.0031)},
        {"magnification": 9, "count": (170683, 646), "percentage": (
            0.0532, 0.1013), "winning_percent": (0.0037, 0.0038)},
        {"magnification": 10, "count": (116405, 480), "percentage": (
            0.0363, 0.0752), "winning_percent": (0.0041, 0.0041)},
        {"magnification": 11, "count": (93768, 403), "percentage": (
            0.0292, 0.0632), "winning_percent": (0.0045, 0.0043)},
        {"magnification": 12, "count": (21429, 110), "percentage": (
            0.0067, 0.0172), "winning_percent": (0.0049, 0.0051)},
        {"magnification": 13, "count": (15, 0), "percentage": (
            0.0000, 0.0000), "winning_percent": (0.0053, 0.0000)},
    ]
})

collection.insert_one({
    "lottery_time": "2019/06/26",
    "a_code": 3_264_065,
    "generation_time": "2019/06/26 10:15",
    "total_ids": 16_225_458,
    "winners": 6373,
    "winning_percent": 0.000393,
    "winner_ratio": 2545.97,
    "detail_data": [
        {"magnification": 1, "count": (382451, 159), "percentage": (
            0.1172, 0.0249), "winning_percent": (0.0004, 0.0004)},
        {"magnification": 2, "count": (392398, 304), "percentage": (
            0.1202, 0.0477), "winning_percent": (0.0008, 0.0008)},
        {"magnification": 3, "count": (384872, 473), "percentage": (
            0.1179, 0.0742), "winning_percent": (0.0012, 0.0012)},
        {"magnification": 4, "count": (413265, 650), "percentage": (
            0.1266, 0.1020), "winning_percent": (0.0016, 0.0016)},
        {"magnification": 5, "count": (409200, 739), "percentage": (
            0.1254, 0.1160), "winning_percent": (0.0020, 0.0018)},
        {"magnification": 6, "count": (336103, 754), "percentage": (
            0.1030, 0.1183), "winning_percent": (0.0024, 0.0022)},
        {"magnification": 7, "count": (242778, 720), "percentage": (
            0.0744, 0.1133), "winning_percent": (0.0027, 0.0030)},
        {"magnification": 8, "count": (260904, 800), "percentage": (
            0.0799, 0.1255), "winning_percent": (0.0031, 0.0031)},
        {"magnification": 9, "count": (187399, 677), "percentage": (
            0.0574, 0.1062), "winning_percent": (0.0035, 0.0036)},
        {"magnification": 10, "count": (123138, 502), "percentage": (
            0.0377, 0.0788), "winning_percent": (0.0039, 0.0041)},
        {"magnification": 11, "count": (95438, 421), "percentage": (
            0.0292, 0.0661), "winning_percent": (0.0043, 0.0044)},
        {"magnification": 12, "count": (36097, 172), "percentage": (
            0.0111, 0.0270), "winning_percent": (0.0047, 0.0048)},
        {"magnification": 13, "count": (22, 0), "percentage": (
            0.0000, 0.0000), "winning_percent": (0.0051, 0.0000)},
    ]
})

collection.insert_one({
    "lottery_time": "2019/08/26",
    "a_code": 3_317_404,
    "generation_time": "2019/08/26 10:15",
    "total_ids": 16_750_880,
    "winners": 6389,
    "winning_percent": 0.000381,
    "winner_ratio": 2621.83,
    "detail_data": [
        {"magnification": 1, "count": (381766, 126), "percentage": (
            0.1151, 0.0197), "winning_percent": (0.0004, 0.0003)},
        {"magnification": 2, "count": (390338, 306), "percentage": (
            0.1177, 0.0479), "winning_percent": (0.0008, 0.0008)},
        {"magnification": 3, "count": (381175, 431), "percentage": (
            0.1149, 0.0675), "winning_percent": (0.0011, 0.0011)},
        {"magnification": 4, "count": (409003, 616), "percentage": (
            0.1233, 0.0964), "winning_percent": (0.0015, 0.0015)},
        {"magnification": 5, "count": (413526, 774), "percentage": (
            0.1247, 0.1211), "winning_percent": (0.0019, 0.0019)},
        {"magnification": 6, "count": (352525, 841), "percentage": (
            0.1063, 0.1316), "winning_percent": (0.0023, 0.0024)},
        {"magnification": 7, "count": (247139, 682), "percentage": (
            0.0745, 0.1067), "winning_percent": (0.0027, 0.0028)},
        {"magnification": 8, "count": (259349, 762), "percentage": (
            0.0782, 0.1193), "winning_percent": (0.0031, 0.0029)},
        {"magnification": 9, "count": (203933, 692), "percentage": (
            0.0615, 0.1083), "winning_percent": (0.0034, 0.0034)},
        {"magnification": 10, "count": (130648, 509), "percentage": (
            0.0394, 0.0797), "winning_percent": (0.0038, 0.0039)},
        {"magnification": 11, "count": (96500, 405), "percentage": (
            0.0291, 0.0634), "winning_percent": (0.0042, 0.0042)},
        {"magnification": 12, "count": (51472, 245), "percentage": (
            0.0155, 0.0383), "winning_percent": (0.0046, 0.0048)},
        {"magnification": 13, "count": (29, 0), "percentage": (
            0.0000, 0.0000), "winning_percent": (0.0050, 0.0000)},
    ]
})

collection.insert_one({
    "lottery_time": "2019/10/26",
    "a_code": 3_317_568,
    "generation_time": "2019/10/26 10:15",
    "total_ids": 17_099_033,
    "winners": 6383,
    "winning_percent": 0.000373,
    "winner_ratio": 2678.84,
    "detail_data": [
        {"magnification": 1, "count": (371189, 129), "percentage": (
            0.1119, 0.0202), "winning_percent": (0.0004, 0.0003)},
        {"magnification": 2, "count": (375188, 289), "percentage": (
            0.1131, 0.0453), "winning_percent": (0.0007, 0.0008)},
        {"magnification": 3, "count": (369094, 403), "percentage": (
            0.1113, 0.0631), "winning_percent": (0.0011, 0.0011)},
        {"magnification": 4, "count": (394829, 577), "percentage": (
            0.1190, 0.0904), "winning_percent": (0.0015, 0.0015)},
        {"magnification": 5, "count": (410636, 750), "percentage": (
            0.1238, 0.1117), "winning_percent": (0.0019, 0.0018)},
        {"magnification": 6, "count": (368304, 877), "percentage": (
            0.1110, 0.1374), "winning_percent": (0.0022, 0.0024)},
        {"magnification": 7, "count": (252637, 652), "percentage": (
            0.0762, 0.1021), "winning_percent": (0.0026, 0.0028)},
        {"magnification": 8, "count": (255248, 765), "percentage": (
            0.0769, 0.1198), "winning_percent": (0.0030, 0.0030)},
        {"magnification": 9, "count": (219395, 767), "percentage": (
            0.0661, 0.1202), "winning_percent": (0.0034, 0.0035)},
        {"magnification": 10, "count": (135317, 488), "percentage": (
            0.0408, 0.0765), "winning_percent": (0.0037, 0.0036)},
        {"magnification": 11, "count": (99110, 388), "percentage": (
            0.0299, 0.0608), "winning_percent": (0.0041, 0.0039)},
        {"magnification": 12, "count": (66585, 298), "percentage": (
            0.0201, 0.0467), "winning_percent": (0.0045, 0.0045)},
        {"magnification": 13, "count": (36, 0), "percentage": (
            0.0000, 0.0000), "winning_percent": (0.0049, 0.0000)},
    ]
})

collection.insert_one({
    "lottery_time": "2019/12/26",
    "a_code": 3_335_437,
    "generation_time": "2019/12/26 10:15",
    "total_ids": 17_493_388,
    "winners": 6384,
    "winning_percent": 0.000365,
    "winner_ratio": 2740.19,
    "detail_data": [
        {"magnification": 1, "count": (372312, 107), "percentage": (
            0.1116, 0.0168), "winning_percent": (0.0004, 0.0003)},
        {"magnification": 2, "count": (359586, 244), "percentage": (
            0.1078, 0.0382), "winning_percent": (0.0007, 0.0007)},
        {"magnification": 3, "count": (362343, 391), "percentage": (
            0.1086, 0.0612), "winning_percent": (0.0011, 0.0011)},
        {"magnification": 4, "count": (381066, 585), "percentage": (
            0.1142, 0.0916), "winning_percent": (0.0015, 0.0015)},
        {"magnification": 5, "count": (407661, 746), "percentage": (
            0.1222, 0.1169), "winning_percent": (0.0018, 0.0018)},
        {"magnification": 6, "count": (378509, 829), "percentage": (
            0.1135, 0.1299), "winning_percent": (0.0022, 0.0022)},
        {"magnification": 7, "count": (263499, 677), "percentage": (
            0.0790, 0.1060), "winning_percent": (0.0026, 0.0026)},
        {"magnification": 8, "count": (248556, 712), "percentage": (
            0.0745, 0.1115), "winning_percent": (0.0029, 0.0029)},
        {"magnification": 9, "count": (235860, 789), "percentage": (
            0.0707, 0.1236), "winning_percent": (0.0033, 0.0033)},
        {"magnification": 10, "count": (142112, 530), "percentage": (
            0.0426, 0.0830), "winning_percent": (0.0036, 0.0037)},
        {"magnification": 11, "count": (102792, 436), "percentage": (
            0.0308, 0.0683), "winning_percent": (0.0040, 0.0042)},
        {"magnification": 12, "count": (81094, 338), "percentage": (
            0.0243, 0.0529), "winning_percent": (0.0044, 0.0042)},
        {"magnification": 13, "count": (47, 0), "percentage": (
            0.0000, 0.0000), "winning_percent": (0.0047, 0.0000)},
    ]
})

collection.insert_one({
    "lottery_time": "2020/04/26",
    "a_code": 3_376_458,
    "generation_time": "2020/04/26 10:15",
    "total_ids": 18_446_810,
    "winners": 6366,
    "winning_percent": 0.000345,
    "winner_ratio": 2897.71,
    "detail_data": [
        {"magnification": 1, "count": (331453, 98), "percentage": (
            0.0982, 0.0154), "winning_percent": (0.0003, 0.0003)},
        {"magnification": 2, "count": (346692, 252), "percentage": (
            0.1027, 0.0396), "winning_percent": (0.0007, 0.0007)},
        {"magnification": 3, "count": (362667, 357), "percentage": (
            0.1074, 0.0561), "winning_percent": (0.0010, 0.0010)},
        {"magnification": 4, "count": (362804, 499), "percentage": (
            0.1075, 0.0784), "winning_percent": (0.0014, 0.0014)},
        {"magnification": 5, "count": (397459, 694), "percentage": (
            0.1177, 0.1090), "winning_percent": (0.0017, 0.0017)},
        {"magnification": 6, "count": (391798, 765), "percentage": (
            0.1160, 0.1202), "winning_percent": (0.0021, 0.0020)},
        {"magnification": 7, "count": (306188, 729), "percentage": (
            0.0907, 0.1145), "winning_percent": (0.0024, 0.0024)},
        {"magnification": 8, "count": (236468, 617), "percentage": (
            0.0700, 0.0969), "winning_percent": (0.0028, 0.0026)},
        {"magnification": 9, "count": (253106, 853), "percentage": (
            0.0750, 0.1340), "winning_percent": (0.0031, 0.0034)},
        {"magnification": 10, "count": (165171, 561), "percentage": (
            0.0489, 0.0881), "winning_percent": (0.0035, 0.0034)},
        {"magnification": 11, "count": (112239, 481), "percentage": (
            0.0332, 0.0756), "winning_percent": (0.0038, 0.0043)},
        {"magnification": 12, "count": (90064, 373), "percentage": (
            0.0267, 0.0586), "winning_percent": (0.0041, 0.0041)},
        {"magnification": 13, "count": (20334, 87), "percentage": (
            0.0060, 0.0137), "winning_percent": (0.0045, 0.0043)},
        {"magnification": 14, "count": (15, 0), "percentage": (
            0.0000, 0.0000), "winning_percent": (0.0048, 0.0000)},
    ]
})

collection.insert_one({
    "lottery_time": "2020/06/26",
    "a_code": 3_435_294,
    "generation_time": "2020/06/26 10:15",
    "total_ids": 19_012_845,
    "winners": 6366,
    "winning_percent": 0.000335,
    "winner_ratio": 2986.62,
    "detail_data": [
        {"magnification": 1, "count": (333543, 110), "percentage": (
            0.0971, 0.0173), "winning_percent": (0.0003, 0.0003)},
        {"magnification": 2, "count": (353089, 261), "percentage": (
            0.1028, 0.0410), "winning_percent": (0.0007, 0.0007)},
        {"magnification": 3, "count": (358269, 374), "percentage": (
            0.1043, 0.0587), "winning_percent": (0.0010, 0.0010)},
        {"magnification": 4, "count": (359631, 477), "percentage": (
            0.1047, 0.0749), "winning_percent": (0.0013, 0.0013)},
        {"magnification": 5, "count": (393900, 677), "percentage": (
            0.1147, 0.1063), "winning_percent": (0.0017, 0.0017)},
        {"magnification": 6, "count": (394771, 785), "percentage": (
            0.1149, 0.1233), "winning_percent": (0.0020, 0.0020)},
        {"magnification": 7, "count": (326530, 749), "percentage": (
            0.0951, 0.1177), "winning_percent": (0.0023, 0.0023)},
        {"magnification": 8, "count": (236530, 628), "percentage": (
            0.0687, 0.0989), "winning_percent": (0.0027, 0.0027)},
        {"magnification": 9, "count": (253338, 754), "percentage": (
            0.0737, 0.1184), "winning_percent": (0.0030, 0.0030)},
        {"magnification": 10, "count": (181189, 596), "percentage": (
            0.0527, 0.0936), "winning_percent": (0.0033, 0.0033)},
        {"magnification": 11, "count": (118721, 451), "percentage": (
            0.0346, 0.0708), "winning_percent": (0.0037, 0.0038)},
        {"magnification": 12, "count": (90712, 362), "percentage": (
            0.0267, 0.0569), "winning_percent": (0.0040, 0.0039)},
        {"magnification": 13, "count": (34522, 142), "percentage": (
            0.0100, 0.0223), "winning_percent": (0.0044, 0.0041)},
        {"magnification": 14, "count": (22, 0), "percentage": (
            0.0000, 0.0000), "winning_percent": (0.0047, 0.0000)},
    ]
})

collection.insert_one({
    "lottery_time": "2020/08/26",
    "a_code": 3_487_665,
    "generation_time": "2020/08/26 10:15",
    "total_ids": 19_580_861,
    "winners": 6366,
    "winning_percent": 0.000325,
    "winner_ratio": 3075.85,
    "detail_data": [
        {"magnification": 1, "count": (331078, 106), "percentage": (
            0.0949, 0.0163), "winning_percent": (0.0003, 0.0003)},
        {"magnification": 2, "count": (354401, 228), "percentage": (
            0.1016, 0.0358), "winning_percent": (0.0007, 0.0006)},
        {"magnification": 3, "count": (357023, 314), "percentage": (
            0.1024, 0.0497), "winning_percent": (0.0010, 0.0009)},
        {"magnification": 4, "count": (356078, 453), "percentage": (
            0.1021, 0.0712), "winning_percent": (0.0013, 0.0013)},
        {"magnification": 5, "count": (389453, 618), "percentage": (
            0.1117, 0.0971), "winning_percent": (0.0016, 0.0016)},
        {"magnification": 6, "count": (398918, 783), "percentage": (
            0.1144, 0.1230), "winning_percent": (0.0020, 0.0020)},
        {"magnification": 7, "count": (342467, 780), "percentage": (
            0.0982, 0.1225), "winning_percent": (0.0023, 0.0023)},
        {"magnification": 8, "count": (241212, 669), "percentage": (
            0.0692, 0.1051), "winning_percent": (0.0026, 0.0028)},
        {"magnification": 9, "count": (251746, 709), "percentage": (
            0.0722, 0.1114), "winning_percent": (0.0029, 0.0028)},
        {"magnification": 10, "count": (197286, 655), "percentage": (
            0.0566, 0.1029), "winning_percent": (0.0033, 0.0033)},
        {"magnification": 11, "count": (126016, 463), "percentage": (
            0.0361, 0.0727), "winning_percent": (0.0036, 0.0037)},
        {"magnification": 12, "count": (92748, 382), "percentage": (
            0.0266, 0.0600), "winning_percent": (0.0039, 0.0041)},
        {"magnification": 13, "count": (49210, 206), "percentage": (
            0.0141, 0.0324), "winning_percent": (0.0042, 0.0042)},
        {"magnification": 14, "count": (29, 0), "percentage": (
            0.0000, 0.0000), "winning_percent": (0.0046, 0.0000)},
    ]
})
