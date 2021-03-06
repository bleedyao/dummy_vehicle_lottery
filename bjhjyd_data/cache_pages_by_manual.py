
import sys
sys.path.append('')
from download_data import *

def manual_cache_web_page():
    '''1. 第一次请求验证码
       2. 打开验证码图片
       3. 手动输入验证码
       4. 检查验证码是否正确，重新请求验证码
       5. 请求摇奖池数据
    '''
    result_for_check = 'false'
    valid_code = ''
    while result_for_check == 'false':
        get_valid_code()
        valid_code = input('请手动输入验证码: ')
        print(valid_code)
        result_for_check = check_valid_code(valid_code)
        continue
    count = get_page_count()
    get_one_page(count, code=valid_code)
    # print(count)
if __name__ == "__main__":
    manual_cache_web_page()