from class_13_crawler_douban import MyCrawler
from lxml import html
import re

douban_crawler = MyCrawler('douban.txt')
content = douban_crawler.download('https://book.douban.com/tag/%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C')

tree = html.fromstring(content)

xpath_book_title = list(map(lambda x: x.text.strip(), tree.xpath("//h2/a")))
xpath_book_pub = list(map(lambda x: x.text.strip(), tree.xpath("//div[@class='pub']")))
xpath_book_intro = list(map(lambda x: x.text.strip(), tree.xpath("//div[@class='info']/p")))

# print(xpath_book_title, xpath_book_pub, xpath_book_intro)

book_infos = tree.xpath("//li[@class='subject-item']")

for book_info in book_infos:
	book_title_elem = book_info.xpath(".//h2/a")[0]
	book_title = re.sub('\s{2,}', '', book_title_elem.text_content().replace('\n', ''))
	book_url = book_info.xpath(".//h2/a")[0].attrib['href']
	book_pub_info = book_info.xpath(".//div[@class='pub']")[0].text.strip()
	book_intro = 'N/A'
	book_intro_elem = book_info.xpath(".//div[@class='info']/p")
	if book_intro_elem:
		book_intro = book_intro_elem[0].text.strip()
	print(book_title, book_url, book_pub_info, '\n', book_intro)
