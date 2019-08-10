from opencc import OpenCC


IN_FILE_PATH = "../files/lesson4/zhwiki.txt"
OUT_FILE_PATH = "../files/lesson4/zhwiki_trans.txt"


def translate():
	cc = OpenCC('t2s')
	source = open(IN_FILE_PATH, 'r', encoding='utf-8')
	result = open(OUT_FILE_PATH, 'w', encoding= 'utf-8')

	count=0
	while True:
		line = source.readline()
		line = cc.convert(line)
		if not line:
			break
		count = count + 1
		result.write(line)
	source.close()
	result.close()


translate()