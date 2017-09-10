"""
通过https://finance.yahoo.com/quote/...
获得某公司的历史股票数据
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date

def crawlforhistory(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'lxml')
	stocks = soup.find_all('tr')
	stockList = []
	for stock in stocks:
		stock = [tag.text for tag in stock.find_all('td')]
		stockList.append(stock)

	# 整理数据发现无用数据，在此去除3项无用数据后放入DataFrame中
	stockList = stockList[2:len(stockList)-1]

	dateindexList = []
	for i in range(len(stockList)):
		date = stockList[i][0]
		dateindexList.append(date)

	# 添加到DateFrame中，设置columns和index，此处使用原Date世界作为df的index
	quotedf_ord = pd.DataFrame(stockList, columns=['Date','Open','High','Low','Close*','Adj Close*','Volume'],index=dateindexList)
	# 删除一列
	quotedf_befor = quotedf_ord.drop(['Adj Close*'],axis=1)
	# 删除原有的Date列
	quotedf = quotedf_befor.drop(['Date'],axis=1)

	print(quotedf)

if __name__ == '__main__':
	crawlforhistory('https://finance.yahoo.com/quote/AAPL/history?p=AAPL')


