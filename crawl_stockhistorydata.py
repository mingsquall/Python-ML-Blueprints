"""
通过https://finance.yahoo.com/quote/...
获得某公司的历史股票数据
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

def crawlforhistory(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'lxml')
	stocks = soup.find_all('tr')
	stockList = []
	for stock in stocks:
		stock = [tag.text for tag in stock.find_all('td')]
		stockList.append(stock)
	# 去除前两个无用元素后放入DataFrame中
	quotedf = pd.DataFrame(stockList[2:], columns=['Data','Open','High','Low','Close*','Adj Close*','Volume'])
	print(quotedf)
if __name__ == '__main__':
	crawlforhistory('https://finance.yahoo.com/quote/AAPL/history?p=AAPL')


