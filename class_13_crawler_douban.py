import requests
import re
import pandas as pd


class MyCrawler:
	def __init__(self, filename):
		self.filename = filename
		self.headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
		}

	# 1. 采——网页的采集
	def download(self, url):
		req = requests.get(url, headers=self.headers)
		return req.text

	# 2. 抽——信息的抽取
	def extract(self, content, pattern_main, pattern_star):
		result = re.findall(pattern_main, content)
		for index in range(len(result)):
			if 'allstar' in result[index][4]:
				star_info = re.findall(pattern_star, result[index][4])
			else:
				star_info = [['0', '0', '少于10人评价']]

			result[index] = list(result[index])
			del result[index][4]
			result[index].extend(star_info[0])

		return result

	# 3. 存——保存采集结果
	def save(self, info):
		df = pd.DataFrame(info, columns=['图片链接', '书籍链接', '书名', '书籍信息', 'star', '评分', '评价人数'])
		df.to_csv(self.filename, encoding='utf-8-sig', index=False)

	# with open(self.filename, 'w', encoding='utf-8') as f:
	# 	f.write('\t'.join(['图片链接', '书籍链接', '书名', '书籍信息', 'star', '评分','评价人数']) + '\n')
	# 	for res in info:
	# 		f.write('\t'.join(res) + '\n')

	def crawler(self, url, pattern_main, pattern_star):
		content = self.download(url)
		info = self.extract(content, pattern_main, pattern_star)
		self.save(info)


'''
爬取豆瓣书籍
'''

douban_filename = './crawler-media/douban.csv'

douban_url = 'https://book.douban.com/tag/%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C'
pattern_main = 'src="(.*?\d+.jpg)"[\s\S]*?<a\shref="(.*?)"\stitle="(.*?)"[\s\S]*?<div\sclass="pub">\s*(.*?)\s*<\/div>[\s\S]*?<div\sclass="star\sclearfix">\s*([\s\S]*?)\s*<\/div>'
pattern_star = 'allstar(\d+)[\s\S]*?rating_nums">([^<]*?)<\/span>[\s\S]*?\((\d+)'
douban_crawler = MyCrawler(filename=douban_filename)

douban_content = douban_crawler.download(douban_url)

douban_info = douban_crawler.extract(douban_content, pattern_main, pattern_star)

douban_crawler.save(douban_info)
