import re
import requests
import os
import shutil
from time import sleep

path_base = '/image'

def save_image(url):
    match = re.match(r'https://i.loli.net(\S+)/(\S+)', url)
    image_name = match.group(2)
    image_path = path_base + match.group(1)
    is_exists = os.path.exists(image_path)
    if not is_exists:
        os.makedirs(image_path)
        print('已创建'+str(image_path)+'目录')
    img1 = path_base + '/' + image_name
    img2 = image_path + '/' + image_name
    shutil.move(img1, img2)
    print(img1 + ' --> ' + img2 + '移动成功')

fail = []
with open(r'C:\Users\owen\Desktop\image_urls.txt') as urls:
    for url in urls:
        save_image(url)
        print(url+'移动成功!')
    print(fail)