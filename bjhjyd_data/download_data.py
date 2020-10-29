import requests
from decorator import running_time, delay_time
import time
import random
import json
import os
import re

updated_cookie = 'JSESSIONID=8C8E953C583B6051E519894092685673-n1.Tomcat1; __utmc=25041897; BCSI-CS-e1a6168bf77b613b=2; __utmz=25041897.1603951976.8.7.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=25041897.654479457.1598424218.1603951976.1603956833.9; __utmt=1; __utmb=25041897.1.10.1603956833'
custom_delay_time = (5, 15)
cache_time = 1 # hour

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
        return (int(total_page_num(file_name)), get_valid_code(file_name))
        
    url = 'https://apply.bjhjyd.gov.cn/apply/pool/personQuery.do'
    # pageNo=1&regType=PTC&issueNumber=202005&applyCode=&validCode=fw7l
    tmp = i 
    if tmp < 0:
        tmp = 1
    data = {'pageNo': str(tmp), 'regType': 'PTC',
            'issueNumber': '202005', 'applyCode': '', 'validCode': code}
    delay('ready to request person query')
    res = requests.post(url, data=json.dumps(data), headers={
        'Cookie': updated_cookie
    })
    res.encoding = 'utf8'
    save_file(res.text, file_name)
    return (int(total_page_num(file_name)), get_valid_code(file_name))


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

def get_valid_code(file_name):
    # 识别图片验证码 valid_code = 识别验证码
    dir = os.path.abspath('pages')
    delay('ready to request the valid code')

    return 'bbbb'

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
