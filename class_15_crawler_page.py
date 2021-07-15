import re
import time
import random
from lxml import html
from class_13_crawler_douban import MyCrawler

douban_crawler = MyCrawler('douban_page.txt')

url = 'https://book.douban.com/tag/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD'
content = douban_crawler.download(url)
tree = html.fromstring(content)
last_page_num = tree.xpath("//div[@class='paginator']/a[last()]")[0].text

print('Last Page Num :{}'.format(last_page_num))

for num in range(int(last_page_num)):
	url_page = url + '?start={}&type=T'.format(20 * num)
	content_page = douban_crawler.download(url)
	tree_page = html.fromstring(content)

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
		print(book_name)
	print(url_page)
	time.sleep(random.randint(1, 10))
