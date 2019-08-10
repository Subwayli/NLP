import jieba


IN_FILE_PATH = "../files/lesson4/zhwiki_trans.txt"
OUT_FILE_PATH = "../files/lesson4/zhwiki_jieba.txt"


def translate():
	source = open(IN_FILE_PATH, 'r', encoding='utf-8')
	result = open(OUT_FILE_PATH, 'w', encoding= 'utf-8')

	while True:
		line = source.readline()
		if not line:
			break
		result.write(' '.join([key for key in jieba.cut(line) if key and key != ' ']))
	source.close()
	result.close()


translate()