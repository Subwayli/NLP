
from functools import lru_cache


solution = {}


@lru_cache(maxsize=2**5)
def edit_distance(sentence_a, sentence_b):
	if len(sentence_a) == 0: return len(sentence_b)
	if len(sentence_b) == 0: return len(sentence_a)
	tail_a = sentence_a[-1]
	tail_b = sentence_b[-1]
	candidates = [
		(edit_distance(sentence_a[:-1], sentence_b) + 1, "delete {}".format(tail_a)),
		(edit_distance(sentence_a, sentence_b[:-1]) + 1, "add {}".format(tail_b)),
		(edit_distance(sentence_a[:-1], sentence_b[:-1]) + 1, 'SUB {} => {}'.format(tail_a, tail_b))
	]
	if tail_a == tail_b:
		return edit_distance(sentence_a[:-1], sentence_b[:-1])
	min_distance, operation = min(candidates, key=lambda x: x[0])
	solution[(tail_a, tail_b)] = operation
	return min_distance


sentence_a = "execution888"
sentence_b = "intention"
print(edit_distance(sentence_a, sentence_b))
for x in solution: print(x)
