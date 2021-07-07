import requests
import re

# 1. 采——网页的采集
req = requests.get('https://wap.zol.com.cn/top/cell_phone/hot.html')

# 2. 抽——信息的抽取
result = re.findall('<p class="pro-info-name f28">(.*?)</p>[\S\s]*?<span class="pro-info-price f24">(.*?)</span>',
					req.text)

print(result)

# 3. 存——保存采集结果

with open('./crawler-media/mobile.txt', 'w', encoding='utf-8') as f:
	for res in result:
		f.write(res[0] + '\t' + res[1] + '\n')
