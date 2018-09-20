import requests
import re
from bs4 import BeautifulSoup
from time import sleep
# data-original="(https://i.loli.net\S+)"
urls_path = r'C:\Users\owen\Desktop\urls.txt'
image_path = r'C:\Users\owen\Desktop\res.txt'
pattern = r'data-original="(https://i.loli.net\S+)"'

def get_image_url(text):
    '''
    获取图片外链地址，返回值为图片链接列表
    '''
    result = re.findall(pattern, text)
    return set(result)

def get_content(url, num=3):
    '''
    获取网页内容，返回值为文章内容
    '''
    response = requests.get(url, timeout=5)
    if response.status_code == requests.codes.ok:
        response.encoding = 'utf-8'
        Soup = BeautifulSoup(response.text, 'html.parser')
        post = Soup.select('#article-post')
        return str(post[0])
    else:
        sleep(1)
        return get_content(url, num=num-1)
    return [url]

def sava_to_text(urls):
    '''
    保存图片链接
    '''
    with open(image_path, 'a+') as res:
        for url in urls:
            res.write(str(url)+'\n')

if __name__ == '__main__':
    with open(urls_path, 'r') as urls:
        for url in urls:
            try:
                content = get_content(url)
                sava_to_text(get_image_url(content))
                print(str(url) + 'saved.')
            except:
                print(url)
                sleep(1)