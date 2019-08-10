# Copyrigh 2017

from __future__ import print_function

import logging
import os.path
import six
import sys

from gensim.corpora import WikiCorpus

IN_FILE_PATH = "../files/lesson4/zhwiki.xml.bz2"
OUT_FILE_PATH = "../files/lesson4/zhwiki.txt"

if __name__ == '__main__':
	program = os.path.basename(sys.argv[0])
	logger = logging.getLogger(program)

	logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
	logging.root.setLevel(level=logging.INFO)
	logger.info("running %s" % ' '.join(sys.argv))

	space = " "
	i = 0

	output = open(OUT_FILE_PATH, 'w', encoding='utf-8')
	wiki = WikiCorpus(IN_FILE_PATH, lemmatize=False, dictionary={})
	for text in wiki.get_texts():
		if six.PY3:
			output.write(bytes(' '.join(text), 'utf-8').decode('utf-8') + '\n')
		#   ###another method###
		#    output.write(
		#            space.join(map(lambda x:x.decode("utf-8"), text)) + '\n')
		else:
			output.write(space.join(text) + "\n")
		i = i + 1
		if (i % 10000 == 0):
			logger.info("Saved " + str(i) + " articles")

	output.close()
	logger.info("Finished Saved " + str(i) + " articles")