import jieba

from lesson1_assignment2 import prob_2_3


def get_probability(sentence):
	words = jieba.cut(sentence)
	sentence_pro = 1
	for i in range(0, len(words)-1, 2):
		probability = prob_2_3(words[i], words[i+1])
		sentence_pro *= probability
	return sentence_pro