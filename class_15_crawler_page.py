import re
import time
import random
from lxml import html
from class_13_crawler_douban import MyCrawler
import urllib

# 初始化
douban_crawler = MyCrawler('douban_page.txt')

# 多标签爬取
# 1. 获取标签tag信息--下载页面并解析
tag_list_url = 'https://book.douban.com/tag/?view=type'
tag_content = douban_crawler.download(tag_list_url)
tag_tree = html.fromstring(tag_content)
tags = tag_tree.xpath('//td/a/text()')

# 逐个标签分页面进行爬取
for tag in tags[:5]:
	print("current tag:", tag)
	# 标签转url
	tag_url = urllib.parse.quote(tag)

	# 2. 分页进行抽取
	# 获取总页数
	url = 'https://book.douban.com/tag/' + tag_url
	print(url)
	content = douban_crawler.download(url)
	tree = html.fromstring(content)
	last_page_num = tree.xpath("//div[@class='paginator']/a[last()]/text()")[0]

	print('Last Page Num :{}'.format(last_page_num))

	# 分页抽取
	for num in range(int(last_page_num)):
		url_page = url + '?start={}&type=T'.format(20 * num)
		content_page = douban_crawler.download(url)
		tree_page = html.fromstring(content)

		print('当前页面url：', url_page)
		book_infos = tree.xpath("//li[@class='subject-item']")
		for book_info in book_infos:
			book_name_elem = book_info.xpath('.//h2/a')[0]
			book_name = re.sub('\s{2,}', '', book_name_elem.text_content().replace('\n', ''))
			book_url = book_name_elem.attrib['href']
			book_pub_info = book_info.xpath(".//div[@class='pub']")[0].text.strip()
			book_intro = 'N/A'
			book_intro_elem = book_info.xpath(".//div[@class='info']/p")
			if book_intro_elem:
				book_intro = book_intro_elem[0].text.strip()
			print('书名：', book_name)

		time.sleep(random.randint(1, 10))
