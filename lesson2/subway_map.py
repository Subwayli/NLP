from collections import defaultdict

import networkx as nx
from pyproj import Proj, transform
import matplotlib.pyplot as plt

from assignment3_map_lines import get_lines_coor
from assignment3_baike_lines import get_baike_lines


#以下两句是显示中文的方法
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']   #有效的方法


UNOPEN_STATIONS = ['通运门', '明光桥西', '清河', '建材城东路', '来广营西', '望和桥']


def tran_coor(x, y):
	inProj = Proj(init='epsg:3857')
	outProj = Proj(init='epsg:4326')
	return transform(inProj, outProj, x, y)


def get_station_coordidate():
	lines = get_lines_coor()
	d_coor = {}
	for line in lines:
		line = line['stops']
		for station in line:
			name = station['name']
			if name.endswith('站'):
				name = name[:-1]
			# coor = tran_coor(station['x'], station['y'])
			coor = (station['x'], station['y'])
			d_coor[name] = coor
	return d_coor


def get_transfer():
	lines = get_baike_lines()
	d_stations = defaultdict(list)
	for line, stations in lines.items():
		pre = ''
		for index, station in enumerate(stations):
			if station in UNOPEN_STATIONS:
				continue
			if pre and pre not in d_stations[station]:
				d_stations[station].append(pre)
			if index < len(stations) - 1 and stations[index + 1] not in d_stations[station] and stations[index + 1] not in UNOPEN_STATIONS:
				d_stations[station].append(stations[index + 1])
			pre = station
	return d_stations


def test_graph():
	"""画图不成功，原因未知"""
	station_coor = get_station_coordidate()
	station_tran = get_transfer()
	station_with_road = nx.Graph(station_tran)
	nx.draw(station_with_road, station_coor, with_labels=True, node_size=len(station_coor))
	plt.show()







