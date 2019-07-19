BigBand = """
rules = 男孩 动作 女孩 
男孩 = Leonard | Sheldon | Howard 
动作 = like | love | hate
女孩 = Penny | Bernadette | Amy
"""
import random


def generate(obj_string):
	words_list = [i for i in obj_string.split('\n') if i != '']
	parser = words_list.pop(0)
	words_dict = {i.split(' = ')[0]: i.split(' = ')[1].split(' | ') for i in words_list}
	words_dict['rules'] = parser.split(' = ')[1].split()
	while True:
		yield ' '.join([random.choice(words_dict[parse]).strip() for parse in words_dict['rules']])


def generate_n(n, obj_string):
	g = generate(obj_string)
	sent_list = []
	for i in range(n):
		sent_list.append(next(g))
	return sent_list

print(generate_n(3, BigBand))
