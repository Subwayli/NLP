import re
import os
import urllib
import pickle

import requests
from bs4 import BeautifulSoup as bs


HEADERS = {
	"Host": "baike.baidu.com",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
	"Accept-Language": "zh-CN,zh;q=0.9",
	"Accept-Encoding": "gzip, deflate, br"
}
LINES_PATH = "../files/lesson2/lines.txt"


def get_table_lines(url):
	r = requests.get(url, headers=HEADERS)
	soup = bs(r.content, features="html.parser")
	tables = soup.select("div[class = 'main-content']")[0].find_all('table')
	for table in tables:
		if table.tr.text == '线路起止点首班末班':
			return table


def get_lines():
	url = "https://baike.baidu.com/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%81/408485"
	table = get_table_lines(url)
	lines = {}
	for elem in table.select("a[target = '_blank']"):
		line = elem.text[4:]
		station_url = urllib.request.unquote(urllib.parse.urljoin(url, elem["href"]))
		lines[line] = get_stations(station_url)
	return lines


def get_table_stations(url):
	r = requests.get(url, headers=HEADERS)
	soup = bs(r.content, features="html.parser")
	tables = soup.select("div[class = 'main-content']")[0].find_all('table')
	for table in tables:
		try:
			if '首末车' in table.caption.text:
				return table
		except AttributeError:
			if '首末车' in table.tr.text:
				return table
	for table in tables:
		try:
			if table.tr.td.text == '车站名称':
				return table
		except AttributeError:
			continue
	for table in tables:
		try:
			if '车站信息' in table.caption.text:
				return table
		except AttributeError:
			continue


def get_stations(url):
	table = get_table_stations(url)
	stations = []
	for index, tr in enumerate(table.children):
		if index == 0:
			continue
		try:
			station = tr.td.text.replace('\n', '')
		except AttributeError:
			continue
		if re.match('.*(【|首末车|首车时间|车站名称|全程|—|-|参考资料|暂缓开通|时间|备注).*', station) or re.match('\d+:\d+', station) or len(station)>10:
			continue
		if station:
			stations.append(station)
	if len(stations) <= 2:
		stations = []
		for index, tr in enumerate(table.children):
			if index == 0:
				continue
			try:
				station = tr.th.text
			except AttributeError:
				continue
			if re.match('.*(【|首末车|首车时间|车站名称|参考资料|备注).*', station):
				continue
			if station:
				stations.append(station)
	for index, station in enumerate(stations):
		if station.endswith('站'):
			stations[index] = station[:-1]
	return stations


def get_baike_lines():
	if os.path.exists(LINES_PATH):
		with open(LINES_PATH, 'rb') as f:
			lines = pickle.load(f)
	else:
		lines = get_lines()
		with open(LINES_PATH, 'wb') as f:
			pickle.dump(lines, f)
	return lines


if __name__ == '__main__':
	print(get_baike_lines())