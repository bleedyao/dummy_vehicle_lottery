import requests
from PIL import Image
from pytesseract import *
from fnmatch import fnmatch
from queue import Queue
import matplotlib.pyplot as plt
import cv2
import time
import os
import random
import re

tmp_folder = './out_img/'

def get_valid_code_image():
    url = "https://apply.jtw.beijing.gov.cn/apply/app/common/validCodeImage?ee=1"
    payload={}
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Dest': 'image',
        'Referer': 'https://xkczb.jtw.beijing.gov.cn/',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'JSESSIONID=E4AEDF01EAE4983BF924A754301EF21C-n2.Tomcat1; __utmz=155578731.1609433414.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=155578731.920128297.1609433414.1624976475.1625068571.7; JSESSIONID=861710E19DE92D5662716A06C8384F99-n2.Tomcat1'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    file_name = str(int(time.time())) + ".jpg"
    path = tmp_folder + str(int(time.time())) + ".jpg"
    with open(path, 'wb') as f:
        f.write(response.content)
    return file_name
        

def clear_border(img,img_name):
  '''去除边框
  '''

  filename = tmp_folder+ img_name.split('.')[-2] + '-clearBorder.jpg'
  h, w = img.shape[:2]
  for y in range(0, w):
    for x in range(0, h):
      # if y ==0 or y == w -1 or y == w - 2:
      if y < 4 or y > w -4:
        img[x, y] = 255
      # if x == 0 or x == h - 1 or x == h - 2:
      if x < 4 or x > h - 4:
        img[x, y] = 255

  cv2.imwrite(filename,img)
  return img


def interference_line(img, img_name):
  '''
  干扰线降噪
  '''

  filename =  tmp_folder+ img_name.split('.')[-2] + '-interferenceline.jpg'
  h, w = img.shape[:2]
  # ！！！opencv矩阵点是反的
  # img[1,2] 1:图片的高度，2：图片的宽度
  for y in range(1, w - 1):
    for x in range(1, h - 1):
      count = 0
      if img[x, y - 1] > 245:
        count = count + 1
      if img[x, y + 1] > 245:
        count = count + 1
      if img[x - 1, y] > 245:
        count = count + 1
      if img[x + 1, y] > 245:
        count = count + 1
      if count > 2:
        img[x, y] = 255
  cv2.imwrite(filename,img)
  return img

def interference_point(img,img_name, x = 0, y = 0):
    """点降噪
    9邻域框,以当前点为中心的田字框,黑点个数
    :param x:
    :param y:
    :return:
    """
    filename =  tmp_folder+ img_name.split('.')[-2] + '-interferencePoint.jpg'
    # todo 判断图片的长宽度下限
    cur_pixel = img[x,y]# 当前像素点的值
    height,width = img.shape[:2]

    for y in range(0, width - 1):
      for x in range(0, height - 1):
        if y == 0:  # 第一行
            if x == 0:  # 左上顶点,4邻域
                # 中心点旁边3个点
                sum = int(cur_pixel) \
                      + int(img[x, y + 1]) \
                      + int(img[x + 1, y]) \
                      + int(img[x + 1, y + 1])
                if sum <= 2 * 245:
                  img[x, y] = 0
            elif x == height - 1:  # 右上顶点
                sum = int(cur_pixel) \
                      + int(img[x, y + 1]) \
                      + int(img[x - 1, y]) \
                      + int(img[x - 1, y + 1])
                if sum <= 2 * 245:
                  img[x, y] = 0
            else:  # 最上非顶点,6邻域
                sum = int(img[x - 1, y]) \
                      + int(img[x - 1, y + 1]) \
                      + int(cur_pixel) \
                      + int(img[x, y + 1]) \
                      + int(img[x + 1, y]) \
                      + int(img[x + 1, y + 1])
                if sum <= 3 * 245:
                  img[x, y] = 0
        elif y == width - 1:  # 最下面一行
            if x == 0:  # 左下顶点
                # 中心点旁边3个点
                sum = int(cur_pixel) \
                      + int(img[x + 1, y]) \
                      + int(img[x + 1, y - 1]) \
                      + int(img[x, y - 1])
                if sum <= 2 * 245:
                  img[x, y] = 0
            elif x == height - 1:  # 右下顶点
                sum = int(cur_pixel) \
                      + int(img[x, y - 1]) \
                      + int(img[x - 1, y]) \
                      + int(img[x - 1, y - 1])

                if sum <= 2 * 245:
                  img[x, y] = 0
            else:  # 最下非顶点,6邻域
                sum = int(cur_pixel) \
                      + int(img[x - 1, y]) \
                      + int(img[x + 1, y]) \
                      + int(img[x, y - 1]) \
                      + int(img[x - 1, y - 1]) \
                      + int(img[x + 1, y - 1])
                if sum <= 3 * 245:
                  img[x, y] = 0
        else:  # y不在边界
            if x == 0:  # 左边非顶点
                sum = int(img[x, y - 1]) \
                      + int(cur_pixel) \
                      + int(img[x, y + 1]) \
                      + int(img[x + 1, y - 1]) \
                      + int(img[x + 1, y]) \
                      + int(img[x + 1, y + 1])

                if sum <= 3 * 245:
                  img[x, y] = 0
            elif x == height - 1:  # 右边非顶点
                sum = int(img[x, y - 1]) \
                      + int(cur_pixel) \
                      + int(img[x, y + 1]) \
                      + int(img[x - 1, y - 1]) \
                      + int(img[x - 1, y]) \
                      + int(img[x - 1, y + 1])

                if sum <= 3 * 245:
                  img[x, y] = 0
            else:  # 具备9领域条件的
                sum = int(img[x - 1, y - 1]) \
                      + int(img[x - 1, y]) \
                      + int(img[x - 1, y + 1]) \
                      + int(img[x, y - 1]) \
                      + int(cur_pixel) \
                      + int(img[x, y + 1]) \
                      + int(img[x + 1, y - 1]) \
                      + int(img[x + 1, y]) \
                      + int(img[x + 1, y + 1])
                if sum <= 4 * 245:
                  img[x, y] = 0
    cv2.imwrite(filename,img)
    return img

def _get_dynamic_binary_image(img_name):
  '''
  自适应阀值二值化
  '''
  filename = tmp_folder + img_name.split('.')[-2] + '-binary.jpg'
  img_name = tmp_folder + img_name
  im = cv2.imread(img_name)
  im = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
  th1 = cv2.adaptiveThreshold(im, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 1)
  cv2.imwrite(filename,th1)
  return th1

def _get_static_binary_image(img, threshold = 140):
  '''
  手动二值化
  '''

  img = Image.open(img)
  img = img.convert('L')
  pixdata = img.load()
  w, h = img.size
  for y in range(h):
    for x in range(w):
      if pixdata[x, y] < threshold:
        pixdata[x, y] = 0
      else:
        pixdata[x, y] = 255

  return img


def cfs(im,x_fd,y_fd):
  '''用队列和集合记录遍历过的像素坐标代替单纯递归以解决cfs访问过深问题
  '''

  # print('**********')

  xaxis=[]
  yaxis=[]
  visited =set()
  q = Queue()
  q.put((x_fd, y_fd))
  visited.add((x_fd, y_fd))
  offsets=[(1, 0), (0, 1), (-1, 0), (0, -1)]#四邻域

  while not q.empty():
      x,y=q.get()

      for xoffset,yoffset in offsets:
          x_neighbor,y_neighbor = x+xoffset,y+yoffset

          if (x_neighbor,y_neighbor) in (visited):
              continue  # 已经访问过了

          visited.add((x_neighbor, y_neighbor))

          try:
              if im[x_neighbor, y_neighbor] == 0:
                  xaxis.append(x_neighbor)
                  yaxis.append(y_neighbor)
                  q.put((x_neighbor,y_neighbor))

          except IndexError:
              pass
  # print(xaxis)
  if (len(xaxis) == 0 | len(yaxis) == 0):
    xmax = x_fd + 1
    xmin = x_fd
    ymax = y_fd + 1
    ymin = y_fd

  else:
    xmax = max(xaxis)
    xmin = min(xaxis)
    ymax = max(yaxis)
    ymin = min(yaxis)
    #ymin,ymax=sort(yaxis)

  return ymax,ymin,xmax,xmin

def detectFgPix(im,xmax):
  '''搜索区块起点
  '''

  h,w = im.shape[:2]
  for y_fd in range(xmax+1,w):
      for x_fd in range(h):
          if im[x_fd,y_fd] == 0:
              return x_fd,y_fd

def CFS(im):
  '''切割字符位置
  '''

  zoneL=[]#各区块长度L列表
  zoneWB=[]#各区块的X轴[起始，终点]列表
  zoneHB=[]#各区块的Y轴[起始，终点]列表

  xmax=0#上一区块结束黑点横坐标,这里是初始化
  for i in range(10):

      try:
          x_fd,y_fd = detectFgPix(im,xmax)
          # print(y_fd,x_fd)
          xmax,xmin,ymax,ymin=cfs(im,x_fd,y_fd)
          L = xmax - xmin
          H = ymax - ymin
          zoneL.append(L)
          zoneWB.append([xmin,xmax])
          zoneHB.append([ymin,ymax])

      except TypeError:
          return zoneL,zoneWB,zoneHB

  return zoneL,zoneWB,zoneHB


def cutting_img(im,im_position,img,xoffset = 1,yoffset = 1):
  filename =  tmp_folder+ img.split('.')[-2]
  # 识别出的字符个数
  im_number = len(im_position[1])
  # 切割字符
  for i in range(im_number):
    im_start_X = im_position[1][i][0] - xoffset
    im_end_X = im_position[1][i][1] + xoffset
    im_start_Y = im_position[2][i][0] - yoffset
    im_end_Y = im_position[2][i][1] + yoffset
    cropped = im[im_start_Y:im_end_Y, im_start_X:im_end_X]
    cv2.imwrite(filename + '-cutting-' + str(i) + '.jpg',cropped)



def main():
  filedir = './easy_img'

  for file in os.listdir(filedir):
    if fnmatch(file, '*.jpeg'):
      img_name = file

      # 自适应阈值二值化
      im = _get_dynamic_binary_image(filedir, img_name)

      # 去除边框
      im = clear_border(im,img_name)

      # 对图片进行干扰线降噪
      im = interference_line(im,img_name)

      # 对图片进行点降噪
      im = interference_point(im,img_name)

      # 切割的位置
      im_position = CFS(im)

      maxL = max(im_position[0])
      minL = min(im_position[0])

      # 如果有粘连字符，如果一个字符的长度过长就认为是粘连字符，并从中间进行切割
      if(maxL > minL + minL * 0.7):
        maxL_index = im_position[0].index(maxL)
        minL_index = im_position[0].index(minL)
        # 设置字符的宽度
        im_position[0][maxL_index] = maxL // 2
        im_position[0].insert(maxL_index + 1, maxL // 2)
        # 设置字符X轴[起始，终点]位置
        im_position[1][maxL_index][1] = im_position[1][maxL_index][0] + maxL // 2
        im_position[1].insert(maxL_index + 1, [im_position[1][maxL_index][1] + 1, im_position[1][maxL_index][1] + 1 + maxL // 2])
        # 设置字符的Y轴[起始，终点]位置
        im_position[2].insert(maxL_index + 1, im_position[2][maxL_index])

      # 切割字符，要想切得好就得配置参数，通常 1 or 2 就可以
      cutting_img(im,im_position,img_name,1,1)

      # 识别验证码
      cutting_img_num = 0
      for file in os.listdir(tmp_folder):
        str_img = ''
        if fnmatch(file, '%s-cutting-*.jpg' % img_name.split('.')[-2]):
          cutting_img_num += 1
      for i in range(cutting_img_num):
        try:
          file = tmp_folder + '%s-cutting-%s.jpg' % (img_name.split('.')[-2], i)
          # 识别验证码
          str_img = str_img + image_to_string(Image.open(file),lang = 'eng', config='-psm 10') #单个字符是10，一行文本是7
        except Exception as err:
            pass
      print('切图：%s' % cutting_img_num)
      print('识别为：%s' % str_img)

def check_valid_code(code):
    if len(code) != 4:
        return False
    if re.match(r'\w{4}', code) == None:
        return False
    return remote_check(code)

def remote_check(code):
    url = "https://apply.jtw.beijing.gov.cn/apply/app/common/checkValidCode?validCode=%s&jsonpCallback=mycallback&name=value&_=%d" % (code, int(round(time.time() * 1000)))
    payload={}
    headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Dest': 'script',
    'Referer': 'https://xkczb.jtw.beijing.gov.cn/',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'JSESSIONID=BE38016C9CADB85511A734D2631B57D4-n1.Tomcat1; __utmz=155578731.1609433414.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=155578731.920128297.1609433414.1624976475.1625068571.7; JSESSIONID=861710E19DE92D5662716A06C8384F99-n2.Tomcat1'
    }

    print(url)
    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    return True if re.match(r'.*true.*', response.text) else False


def _main():
    if not os.path.exists(tmp_folder):
        os.mkdir(tmp_folder)
    file_name = get_valid_code_image()
    im = _get_dynamic_binary_image(file_name)
    # im = clear_border(im, file_name)
    im = interference_line(im, file_name)
    im = interference_point(im, file_name)
    # im_position = CFS(im)

    # maxL = max(im_position[0])
    # minL = min(im_position[0])

    # if(maxL > minL + minL * 0.7):
    #     maxL_index = im_position[0].index(maxL)
    #     minL_index = im_position[0].index(minL)
    #     im_position[0][maxL_index] = maxL // 2
    #     im_position[0].insert(maxL_index + 1, maxL // 2)
    #     im_position[1][maxL_index][1] = im_position[1][maxL_index][0] + maxL // 2
    #     im_position[1].insert(maxL_index + 1, [im_position[1][maxL_index][1] + 1, im_position[1][maxL_index][1] + 1 + maxL // 2])
    #     im_position[2].insert(maxL_index + 1, im_position[2][maxL_index])

    # cutting_img(im,im_position,file_name,1,1)

    # 识别一行验证码
    file = tmp_folder+ file_name.split('.')[-2] + '-interferencePoint.jpg'
    result = image_to_string(Image.open(file), lang= 'eng', config='--psm 7').strip()
    print(result, len(result))
    result = check_valid_code(result) 
    print(result)

    # 识别验证码
    # cutting_img_num = 0
    # for file in os.listdir(tmp_folder):
    #   str_img = ''
    #   if fnmatch(file, '%s-cutting-*.jpg' % file_name.split('.')[-2]):
    #     cutting_img_num += 1
    # for i in range(cutting_img_num):
    #   try:
    #     file = tmp_folder + '%s-cutting-%s.jpg' % (file_name.split('.')[-2], i)
    #     # 识别验证码
    #     str_img = str_img + image_to_string(Image.open(file),lang = 'eng', config='--psm 10') #单个字符是10，一行文本是7
    #   except Exception as err:
    #       print(err)
    # print('切图：%s' % cutting_img_num)
    # print('识别为：%s' % str_img)
    for file in os.listdir(tmp_folder):
        if "-" in file:
            os.remove(tmp_folder + file)

    return result


if __name__ == '__main__':
    count = 0
    while True:
        count += 1
        if _main():
            break
        sleep_time = random.randint(10, 20)
        print('延时: %d 秒' % sleep_time)
        time.sleep(sleep_time)
    print(count)