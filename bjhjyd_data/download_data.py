import requests
from decorator import running_time, delay_time
import time
import random
import json
import os
import re
from PIL import Image
import pytesseract

cookie = 'JSESSIONID=8C8E953C583B6051E519894092685673-n1.Tomcat1; __utmc=25041897; BCSI-CS-e1a6168bf77b613b=2; __utmz=25041897.1603951976.8.7.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=25041897.654479457.1598424218.1603951976.1603956833.9; __utmt=1; __utmb=25041897.1.10.1603956833'
custom_delay_time = (5, 10)
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
        update_cookie()
        
def update_cookie():
    url = 'https://apply.bjhjyd.gov.cn/apply/user/person/login.html'
    '''
    userType: 0
    ranStr: 
    userTypeSelect: 0
    serviceUserTypeSelect: 0
    serviceType: 1
    personMobile: xxxxxxx
    loginType: mobile
    unitLoginTypeSelect: 0
    unitMobile: 
    orgCode: 
    password: xxxxxx
    pin: 
    validCode: 7thq
    '''
    data = {
        'userType': 0,
        'ranStr': '',
        'userTypeSelect': 0,
        'serviceUserTypeSelect': 0,
        'serviceType': 1,
        'personMobile': my_infomation['name'],
        'loginType': 'mobile',
        'unitLoginTypeSelect': 0,
        'unitMobile': '',
        'orgCode': '',
        'password': my_infomation['pwd'],
        'pin': '',
        'validCode': get_new_vaild_code()
    }

    res = requests.post(url, data=json.dumps(data))
    print(res.status_code)

def get_new_vaild_code():
    res = requests.get('https://apply.bjhjyd.gov.cn/apply/validCodeImage.html?ee=1')
    delay('ready to request the valid code')
    path = os.path.join(os.path.abspath('pages'), 'vaild_code.jpg')
    print('status code: '+ str(res.status_code))
    with open(path, 'wb') as f:
        f.write(res.content)
    image = Image.open(path)
    image.show()
    vaild_code = input('手动输入你看到的验证码：')
    return vaild_code

@running_time
def get_one_page(i, code='aaaa'):
    '''
    i: 页数
    code: 验证码
    '''
    # 增加检查缓存的功能
    file_name = str(i) + '.html' 
    if get_expiration_time(file_name) > time.time():
        print('read the cache content: %s' % file_name)
        return (int(total_page_num(file_name)), get_valid_code(i))
        
    url = 'https://apply.bjhjyd.gov.cn/apply/pool/personQuery.do'
    # pageNo=1&regType=PTC&issueNumber=202005&applyCode=&validCode=fw7l
    tmp = i 
    if tmp < 0:
        tmp = 1
    data = {'pageNo': str(tmp), 'regType': 'PTC',
            'issueNumber': '202005', 'applyCode': '', 'validCode': code}
    delay('ready to request person query')
    res = requests.post(url, data=json.dumps(data), headers={
        'Cookie': cookie
    })
    res.encoding = 'utf8'
    save_file(res.text, file_name)
    return (int(total_page_num(file_name)), get_valid_code(i))


def save_file(content, file_name):
    dir = os.path.abspath('pages')
    if not os.path.exists(dir):
        os.mkdir(dir)
    with open(os.path.join(dir, file_name), 'wb') as f:
        f.write(str(time.time() + cache_time * 60 * 60 ).join('\r\n').encode('utf8'))
        f.write(content.encode('utf8'))
    print('save the file: %s' % file_name)


def total_page_num(file_name):
    dir = os.path.abspath('pages')
    with open(os.path.join(dir, file_name), 'r') as f:
        temp = f.read()
        return re.search(r'共<span class="dred">(.*)</span>页', temp, re.M | re.I).group(1)

def get_valid_code(index):
    # 识别图片验证码 valid_code = 识别验证码
    dir = os.path.abspath('pages')
    # res = requests.get('https://apply.bjhjyd.gov.cn/apply/validCodeImage.html?ee=1')
    # delay('ready to request the valid code')
    # with open(os.path.join(dir, str(index) + '.jpg'), 'wb') as f:
    #     f.write(res.content)
    return recogniztion_img(os.path.join(dir, str(index) + '.jpg'))

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