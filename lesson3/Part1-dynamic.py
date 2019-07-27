import time
from collections import defaultdict
from functools import lru_cache


price = defaultdict(int)
original_price = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
for i, p in enumerate(original_price):
	price[i+1] = p


def memo(func):
	cache = {}
	def wrapper(n):
		if n in cache:return cache[n]
		result = func(n)
		cache[n]=result
		return result
	return wrapper


@memo
def r(n):
	return max([price[n]] + [r(i) + r(n-i) for i in range(1, n)])


@lru_cache(maxsize=128)
def r1(n):
	return max(
		[price[n]] + [r(i) + r(n-i) for i in range(1, n)]
	)


start = time.time()
print(r(15))
print("elapsed is :{}s. ".format(time.time() - start))