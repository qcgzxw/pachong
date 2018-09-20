import re
import requests
import threading

from time import sleep

url_base = 'https://www.qcgzxw.cn/'
id_start = 0
id_end = 300
res = []

def valid_url(url, yz=3):
    try:
        respose = requests.get(url)
    except:
        print('异常等待5S！')
        sleep(5)
        yz -= 1
        if yz > 0:
            return valid_url(url, yz)
        else:
            return
    if respose.status_code == requests.codes.ok:
        print(url)
        res.append(url)
    else:
        yz -= 1
        if yz > 0:
            sleep(2)
            return valid_url(url, yz)
        else:
            return

for i in range(id_start, id_end):
    url = url_base + str(i) + '.html'
    valid_url(url)
print('done')
with open('res.txt', 'w') as res_file:
    for url in res:
        res_file.write(url+'\n')