import os
import pickle
from subway_map import get_transfer

def get_trans():
	trans_path = "../files/lesson2/lines_tran.txt"
	if os.path.exists(trans_path):
		with open(trans_path, 'rb') as f:
			stations_trans = pickle.load(f)
	else:
		with open(trans_path, 'wb') as f:
			stations_trans = get_transfer()
			pickle.dump(stations_trans, f)
	return stations_trans



def search_dfs(start, destination, stations_trans):
	paths = [[start]]
	visitied = set()
	while paths:
		path = paths.pop()
		station = path[-1]
		for t in stations_trans[station]:
			new_path = list(path)
			if t not in visitied:
				new_path.append(t)
				paths.append(new_path)
			if t == destination:
				return new_path
		visitied.add(station)


def search_shortest(start, destination, stations_trans):
	paths = [[start]]
	visitied = set()
	while paths:
		path = paths.pop()
		station = path[-1]
		for t in stations_trans[station]:
			new_path = list(path)
			if t not in visitied:
				new_path.append(t)
				paths.append(new_path)
			if t == destination:
				return new_path
		visitied.add(station)
		paths = sorted(paths, key=len, reverse=True)


def search_bfs(start, destination, stations_trans):
	paths = [[start]]
	visitied = set()
	while paths:
		path = paths.pop()
		station = path[-1]
		for t in stations_trans[station]:
			new_path = list(path)
			if t not in visitied:
				new_path.append(t)
				paths.insert(0, new_path)
			if t == destination:
				return new_path
		visitied.add(station)


start = '和平门'
destination = '安贞门'
stations_trans = get_trans()

shortest_path = search_shortest(start, destination, stations_trans)
dfs_path = search_dfs(start, destination, stations_trans)
bfs_path = search_bfs(start, destination, stations_trans)
print("最短路径优先：", len(shortest_path), shortest_path)
print("深度优先：", len(dfs_path), dfs_path)
print("广度优先：", len(bfs_path), bfs_path)

