"""
在“http://money.cnn.com/data/dow30/”上
抓取道指成分股数据并将30家公司的代码、公司名称和最近一次成交价等信息放到一个列表中输出。
"""
import requests
from bs4 import BeautifulSoup
import re

# 方法1：使用BeautifulSoup中的tag
def crawl(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'lxml')
	stocks = soup.find_all('tr') # 找到所有的tr标签
	stockList = []
	for stock in stocks:
		stock = [tag.text for tag in stock.find_all('td')] # 找到每一列的tag, 使用tag.text得到文本，使用列表表达式拼接
		stockList.append(stock)
	print(stockList[2:]) # 输出不含标题行的List


# 方法2：使用正则表达式
def retrieve_dji_list(url):
	r = requests.get(url)

	search_pattern = re.compile('class="wsod_symbol">(.*?)<\/a>.*<span.*">(.*?)<\/span>.*\n.*class="wsod_stream">(.*?)<\/span>.*\n.*class="wsod_stream"><span class="posData">(.*?)<\/span>.*\n.*span class="posChangePct">(.*?)<\/span>.*\n.*class="wsod_aRight">(.*?)<\/td>.*\n.*class="wsod_aRight"><span class="posData">(.*?)<\/span>.*')
	dji_list_in_text = re.findall(search_pattern, r.text)
	return dji_list_in_text

# 构建一个{[股票代码:股票最近一次成交价]}的Dict
def generate_stock_dict(sList):
	codeList = []
	priceList = []
	# 分别将code, price 循环拼接到List中，再通过zip函数将两个List打包成一一对应
	for i in range(30):
		codeStr = sList[i][0]
		priceStr = sList[i][2]
		codeList.append(codeStr)
		priceList.append(priceStr)
	stock_dict = dict(zip(codeList, priceList))
	return stock_dict

if __name__ == '__main__':
	# 测试方法1
	crawl('http://money.cnn.com/data/dow30/')
	print('\n')
	# 测试方法2
	print(retrieve_dji_list('http://money.cnn.com/data/dow30/'))
	# 生成字典
	# sList = retrieve_dji_list('http://money.cnn.com/data/dow30/')
	# print(generate_stock_dict(sList))
