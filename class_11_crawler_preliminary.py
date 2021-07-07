import requests
import re

class MyCrawler:
	def __init__(self, filename):
		self.filename = filename

	# 1. 采——网页的采集
	def download(self, url):
		req = requests.get(url)
		return req.text

	# 2. 抽——信息的抽取
	def extract(self, content, pattern):
		info = re.findall(pattern, content)
		return info

	# 3. 存——保存采集结果
	def save(self, info):
		with open(self.filename, 'w', encoding='utf-8') as f:
			for res in info:
				f.write(res[0] + '\t' + res[1] + '\n')

	def crawler(self, url, pattern):
		content = self.download(url)
		info = self.extract(content, pattern)
		self.save(info)


filename = './crawler-media/mobile.txt'
url = 'https://wap.zol.com.cn/top/cell_phone/hot.html'
pattern = '<p class="pro-info-name f28">(.*?)</p>[\S\s]*?<span class="pro-info-price f24">(.*?)</span>'

mycrawler = MyCrawler(filename=filename)

mycrawler.crawler(url, pattern)
