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
			f.write('\t'.join(['链接', '标题', '播放量', '弹幕数', 'UP主', '综合得分']) + '\n')
			for res in info:
				f.write('\t'.join(res) + '\n')

	def crawler(self, url, pattern):
		content = self.download(url)
		info = self.extract(content, pattern)
		self.save(info)


# filename = './crawler-media/mobile.txt'
# url = 'https://wap.zol.com.cn/top/cell_phone/hot.html'
# pattern = '<p class="pro-info-name f28">(.*?)</p>[\S\s]*?<span class="pro-info-price f24">(.*?)</span>'

filename = './crawler-media/bilibili_rank.txt'
url = 'https://www.bilibili.com/v/popular/rank/all'
pattern = '<div class="info"><a href="\/\/(.*?)" target="_blank" class="title">(.*?)<\/a>.*?<\/i>\s+(.*?)\s+.*?<\/i>\s+(.*?)\s+.*?<\/i>\s+(.*?)\s+.*?<div class="pts"><div>(\d+)<\/div>'

mycrawler = MyCrawler(filename=filename)

content = mycrawler.download(url)
info = mycrawler.extract(content, pattern)
mycrawler.save(info)

# mycrawler.crawler(url, pattern)
