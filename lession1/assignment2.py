
import re
import csv
import pickle
from collections import Counter

import jieba

CSV_FILE = 'files/lesson1/movie_comments.csv'
CUT_FILE = "files/lesson1/movie_cut.txt"
LIST_FILE = "files/lesson1/movie_list_obj.txt"


def csv_to_cut(csv_file, cut_file):
	with open(csv_file, 'r', encoding='utf8') as fp:
		lines = csv.reader(fp)
		for line in lines:
			sentence = ''.join(re.findall('\w+', line[3]))
			with open(cut_file, 'a', encoding='utf8') as f:
				cut_string = '|'.join(jieba.cut(sentence)) + '|'
				f.write(cut_string)


def pickle_cut_to_list(cut_file, list_file):
	with open(cut_file, 'r', encoding='utf8') as f:
		string = f.read()
		data = string.split('|')
		with open(list_file, 'wb') as f_obj:
			pickle.dump(data, f_obj)


def get_pickle_list(list_file):
	with open(list_file, 'rb') as f:
		my_list = pickle.load(f)
	return my_list


def prob_1():
	data = get_pickle_list(LIST_FILE)
	counter = Counter(data)
	in_word = input("请输入词语：")
	length = len(data)
	while in_word:
		if in_word in data:
			print("{}的概率是{:.5f}".format(in_word, counter[in_word]/length))
		else:
			print("{} 不属于该数据集！".format(in_word))
		in_word = input("请输入词语：")


def prob_2(list_file):
	data = get_pickle_list(list_file)
	token_2_data = [''.join(data[i:i+2]) for i in range(0, len(data)-2, 2)]
	length = len(token_2_data)
	counter = Counter(token_2_data)
	word1 = input("请输入第一个词语：")
	word2 = input("请输入第二个词语：")
	while word1 + word2:
		if word1 + word2 in token_2_data:
			print("{}的概率是{:f}".format(word1 + word2, counter[word1 + word2]/length))
		else:
			print("{} 不属于该数据集！".format(word1 + word2))
		word1 = input("请输入第一个词语：")
		word2 = input("请输入第二个词语：")


def prob_2_3(word1, word2):
	"""used by lesson1_assignment3"""
	data = get_pickle_list(LIST_FILE)
	token_2_data = [''.join(data[i:i+2]) for i in range(0, len(data)-2, 2)]
	length = len(token_2_data)
	counter = Counter(token_2_data)
	return counter[word1 + word2]/length





# csv_to_cut(CSV_FILE, CUT_FILE)
# pickle_cut_to_list(CUT_FILE, LIST_FILE)
# get_pickle_list(LIST_FILE)
# prob_1()
prob_2(LIST_FILE)