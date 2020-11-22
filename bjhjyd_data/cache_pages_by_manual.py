
import sys
sys.path.append('')
from download_data import *

def manual_cache_web_page():
    '''1. 请求往期摇号信息列表网址（GET）
       2. 请求验证码网址
       3. 打开验证码图片
       4. 等待用户手动输入验证码
       5. 携带验证码信息请求往期摇号信息列表网址（POST）
            a. 如果返回没有数据，错误处理，给出提示信息
            b. 延时 5 ~ 10 秒钟
            c. 重新登陆并获取新的 cookie，并重新请求列表网址
       6. 保存返回信息至指定路径
    '''
    request_lettory_pool()

if __name__ == "__main__":
    manual_cache_web_page()