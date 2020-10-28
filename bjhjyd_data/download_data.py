import requests
from decorator import running_time, delay_time
import time
import random
import json
import os
import re


@running_time
def get_one_page(i, code='aaaa'):
    '''
    i: 页数
    code: 验证码
    '''
    url = 'https://apply.bjhjyd.gov.cn/apply/pool/personQuery.do'
    # pageNo=1&regType=PTC&issueNumber=202005&applyCode=&validCode=fw7l
    data = {'pageNo': '1', 'regType': 'PTC',
            'issueNumber': '202005', 'applyCode': '', 'validCode': code}
    res = requests.post(url, data=json.dumps(data), headers={
        'Cookie': 'JSESSIONID=368B29E053CA1CD21AB9EEFF09EC00C3-n1.Tomcat1; JSESSIONID=74886BC6300C65A7905F427F365D29A9-n1.Tomcat1; __utmc=25041897; __utmz=25041897.1603794941.23.11.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=25041897.589839711.1533966281.1603884035.1603892356.25; __utmt=1; __utmb=25041897.1.10.1603892356'
    })
    # print(res.text)
    save_file(res.text, str(i) + '.html')
    return total_page_num(str(i) + '.html')


def save_file(content, file_name):
    dir = os.path.abspath('pages')
    if not os.path.exists(dir):
        os.mkdir(dir)
    with open(os.path.join(dir, file_name), 'wb') as f:
        f.write(content.encode('utf8'))


def total_page_num(file_name):
    dir = os.path.abspath('pages')
    with open(os.path.join(dir, file_name), 'r') as f:
        temp = f.read()
        return re.search(r'共<span class="dred">(.*)</span>页', temp, re.M | re.I).group(1)


@delay_time
def delay():
    time.sleep(random.randint(5, 10))


if __name__ == "__main__":
    get_one_page(0)
    # 识别图片验证码 valid_code = 识别验证码
    delay()
