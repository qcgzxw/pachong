import re
import requests
import os
from time import sleep

path_urls = r'C:\Users\owen\Desktop\neilian.txt'# 图片路径（一行一条）
guize = r'https://www.qcgzxw.cn/wp-content/uploads(\S+)/(\S+)\.(png|jpg|gif|jpeg|webp)'# 图片目录，图片名称正则
path_base = '/image'# 图片保存路径
headers = {
 'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
 'Cookie':'love_2795=2795; _ga=GA1.2.1779309949.1534838090; pgv_pvi=6978058240; Hm_lvt_0d49c9511331d0f9de734c0672f05e0c=1534847357,1534916778,1534932956,1534993674; __cfduid=d0cf8573770b8b40c49bccdbacffc9be51535003911; love_2799=2799; wordpress_test_cookie=WP+Cookie+check; _gid=GA1.2.1503872837.1536925973; UM_distinctid=165db3e127f1b0-0ed896ea11ca88-5701631-144000-165db3e12809b2; wp-settings-1=libraryContent%3Dbrowse%26editor%3Dtinymce%26mfold%3Do%26hidetb%3D1%26post_dfw%3Doff%26align%3Dcenter%26imgsize%3Dfull%26advImgDetails%3Dshow%26urlbutton%3Dfile%26widgets_access%3Doff%26editor_plain_text_paste_warning%3D2; wp-settings-time-1=1537267999; wordpress_logged_in_c2cef18eb92a696cdc19704ce902fda4=admin%7C1537619979%7CJQDSsVjjr0dd9p1CI8Jabuci3IFAnpd3t8EVgoxPBhQ%7Cea03dd4a869c3f55295ebdc7f889be6868ae588a35bc4e03e6cb95633ae7dab0'
}

def save_image(url):
    match = re.match(guize, url)
    image_name = match.group(2) + '.' + match.group(3)
    image_path = path_base + match.group(1)
    is_exists = os.path.exists(image_path)
    if not is_exists:
        os.makedirs(image_path)
        print('已创建'+str(image_path)+'目录')
    img = image_path + '/' + image_name
    image = requests.get(url)
    with open(img, 'wb') as f:
        f.write(image.content)


fail = []# 存放出错url
with open(path_urls, encoding='utf-8') as urls:
    for url in urls.readlines():
        try:
            save_image(str(url.splitlines()[0]))
            print(url+'下载成功!')
        except:
            fail.append(str(url.splitlines()[0]))
            print(url+'下载失败!')
    print(fail)