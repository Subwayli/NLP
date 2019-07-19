import os
import time
import pickle

import requests

LINES_COOR_PATH = '../files/lesson2/lines_coor.txt'


def get_map_coordinate():
	url = "http://map.baidu.com/?qt=bsi&c={city}&t={time}"
	null = None
	r = requests.get(url.format(city=131, time=int(time.time() * 1000)))
	data = eval(r.content)
	return data['content']


def get_lines_coor():
	if os.path.exists(LINES_COOR_PATH):
		with open(LINES_COOR_PATH, 'rb') as f:
			lines_coor = pickle.load(f)
	else:
		lines_coor = get_map_coordinate()
		with open(LINES_COOR_PATH, 'wb') as f:
			pickle.dump(lines_coor, f)
	return lines_coor


if __name__ == '__main__':
	print(get_lines_coor())
