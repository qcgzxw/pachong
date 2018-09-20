import re
import requests
from bs4 import BeautifulSoup
url = 'http://news.sina.com.cn/china/'

id_start = 1100000
id_end = 1100100

respose = requests.get(url)
respose.encoding = 'utf-8'
text = respose.text
soup = BeautifulSoup(text, 'html.parser')
for news in soup.select('.blk122'):
	for url in news.select('a'):
		print(url.text)
		print(url['href'])
		article_text = requests.get(url['href'])
		article_text.encoding = 'utf-8'
		article = BeautifulSoup(article_text.text, 'html.parser')
		print(article.select('.article')[0].text)