import requests
from decorator import running_time, delay_time
import time
import random
import json
import os
import re
from PIL import Image
import pytesseract
import logging

cookie = 'JSESSIONID=656B4D146910CA0A5DF0FDD604D05EA2-n1.Tomcat1; __utmz=25041897.1606098025.15.11.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=25041897.654479457.1598424218.1606703035.1606793807.24; __utmc=25041897; __utmt=1; __utmb=25041897.1.10.1606793807; BCSI-CS-7e324c105e396941=2'
ustom_delay_time = (5, 10)
cache_time = 1 # hour


def request_lettory_pool():
    # 1. 请求摇号池列表
    url = 'https://apply.bjhjyd.gov.cn/apply/pool/personQuery.do?regType=PTC'
    res = requests.get(url)
    print(res.status_code)
    res.encoding = 'utf8'
    tmp = res.text
    # 如果 cookie 已经过期，重新登陆，更新 cookie
    if tmp.find('个人普通指标摇号池编码公布') == -1:
        print('the cookie was expired')
        # update_cookie()
        
# def update_cookie():
#     url = 'https://apply.bjhjyd.gov.cn/apply/user/person/login.html'
#     '''
#     userType: 0
#     ranStr: 
#     userTypeSelect: 0
#     serviceUserTypeSelect: 0
#     serviceType: 1
#     personMobile: xxxxxxx
#     loginType: mobile
#     unitLoginTypeSelect: 0
#     unitMobile: 
#     orgCode: 
#     password: xxxxxx
#     pin: 
#     validCode: 7thq
#     '''
#     data = {
#         'userType': 0,
#         'ranStr': '',
#         'userTypeSelect': 0,
#         'serviceUserTypeSelect': 0,
#         'serviceType': 1,
#         'personMobile': my_infomation['name'],
#         'loginType': 'mobile',
#         'unitLoginTypeSelect': 0,
#         'unitMobile': '',
#         'orgCode': '',
#         'password': my_infomation['pwd'],
#         'pin': '',
#         'validCode': get_new_vaild_code()
#     }

#     res = requests.post(url, data=json.dumps(data))
#     print(res.status_code)

# def get_new_vaild_code():
#     res = requests.get('https://apply.bjhjyd.gov.cn/apply/validCodeImage.html?ee=1', headers={
#         'Host': 'apply.bjhjyd.gov.cn'
#         'Connection': 'keep-alive'
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
#         'Accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8'
#         'Sec-Fetch-Site': 'same-site'
#         'Sec-Fetch-Mode': 'no-cors'
#         'Sec-Fetch-Dest': 'image'
#         'Referer': 'https://www.bjhjyd.gov.cn/'
#         'Accept-Encoding': 'gzip, deflate, br'
#         'Accept-Language': 'en-US,en;q=0.9'
#         'Cookie': cookie
#     })
#     delay('ready to request the valid code')
#     path = os.path.join(os.path.abspath('pages'), 'vaild_code.jpg')
#     print('status code: '+ str(res.status_code))
#     with open(path, 'wb') as f:
#         f.write(res.content)
#     image = Image.open(path)
#     image.show()
#     vaild_code = input('手动输入你看到的验证码：')
#     return vaild_code

@running_time
def get_one_page(i, code='aaaa'):
    '''
    i: 页数
    code: 验证码
    '''
    try:
        from http.client import HTTPConnection
    except ImportError:
        from httplib import HTTPConnection
    HTTPConnection.debuglevel = 1
    logging.basicConfig() # 初始化 logging，否则不会看到任何 requests 的输出。
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True
    # 增加检查缓存的功能
    file_name = str(i) + '.html' 
    # if get_expiration_time(file_name) > time.time():
    #     print('read the cache content: %s' % file_name)
    #     return (int(total_page_num(file_name)), get_valid_code(i))
        
    url = 'https://apply.bjhjyd.gov.cn/apply/pool/personQuery.do'
    # pageNo=1&regType=PTC&issueNumber=202005&applyCode=&validCode=fw7l
    tmp = i 
    if tmp < 0:
        tmp = 1
    data = {'pageNo': str(tmp), 'regType': 'PTC',
            'issueNumber': '202005', 'applyCode': '', 'validCode': code}
    # delay('ready to request person query')
    res = requests.post(url, data=data, headers={
        'Cookie': cookie
    })
    res.encoding = 'utf8'
    print(re.search(r'共<span class="dred">(.*)</span>页', res.text, re.M | re.I).group(1))
    dir = os.path.abspath('pages')
    if not os.path.exists(dir):
        os.mkdir(dir)
    file_path = os.path.join(dir, file_name)
    save_file(res.text, file_path)
    # return (int(total_page_num(file_name)), get_valid_code(i))

def get_page_count():
    result = 1
    dir = os.path.abspath('pages')
    for path, dirs, files in os.walk(dir):
        for file_name in files:
            if file_name.endswith('.html'):
                if int(os.path.splitext(file_name)[0]) >= result:
                    result = int(os.path.splitext(file_name)[0]) + 1
    return result

def save_file(content, file_path):
    with open(file_path, 'wb') as f:
        # f.write(str(time.time() + cache_time * 60 * 60 ).join('\r\n').encode('utf8'))
        f.write(content.encode('utf8'))
    print('save the file: %s' % file_path)


def total_page_num(file_name):
    dir = os.path.abspath('pages')
    with open(os.path.join(dir, file_name), 'r') as f:
        temp = f.read()
        return re.search(r'共<span class="dred">(.*)</span>页', temp, re.M | re.I).group(1)

def get_valid_code():
    # 识别图片验证码 valid_code = 识别验证码
    dir = os.path.abspath('pages')
    print('获取一个新的验证码')
    res = requests.get('https://apply.bjhjyd.gov.cn/apply/validCodeImage.html?ee=1',  headers={
       'Cookie': cookie
    })
    # delay('ready to request the valid code')
    with open(os.path.join(dir, 'valid_code.jpg'), 'wb') as f:
        f.write(res.content)
    image = Image.open(os.path.join(dir, 'valid_code.jpg'))
    image.show()

def check_valid_code(str):
    # print('https://apply.bjhjyd.gov.cn/apply/checkValidCode.html?validCode=%s' % str)
    res = requests.get('https://apply.bjhjyd.gov.cn/apply/checkValidCode.html?validCode=%s' % str, headers={
       'Cookie': cookie
    })
    # print(res.headers)
    result = re.search(r'\'(.*)\'', res.text, re.M | re.I).group(1)
    print(result)
    return result

def recogniztion_img(file_path):
    image = Image.open(file_path)
    # image.show()
    image_grey = image.convert('L')
    # image_grey.show()
    table = []
    for i in range(256):
        if i < 140:
            table.append(0)
        else:
            table.append(1)
    image_bi = image_grey.point(table, '1')
    # 识别验证码
    verify_code = pytesseract.image_to_string(image_bi)
    print(verify_code)
    pass

def get_expiration_time(file_name):
    dir = os.path.abspath('pages')
    result = 0
    if os.path.exists(dir) and os.path.exists(os.path.join(dir, file_name)):
        with open(os.path.join(dir, file_name), 'r') as f:
            f.readline()
            tmp = f.readline()
            print(tmp)
            try:
                result = float(tmp)
            except TypeError as e:
                print(e)
    return result

@delay_time
def delay(detail='ready into delay'):
    print(detail)
    time.sleep(random.randint(custom_delay_time[0], custom_delay_time[1]))


my_infomation = {
    'name': 'xxxx',
    'pwd': 'xxxxxxx'
}