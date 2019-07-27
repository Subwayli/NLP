"""
目前只做到第一题的前两个小问题；
关于梯度下降的作业，等第三次课程作业一起提交
"""


from sklearn.datasets import load_boston

import pandas as pd
pd.set_option('display.max_columns', None)

import matplotlib.pyplot as plt
import random


def price(rm, k, b):
	return k*rm + b


def draw(k, b):
	boston = load_boston()
	X, y = boston.data, boston.target
	X_rm = X[:, 5]
	price_by_random_k_and_b = [price(r, k, b) for r in X_rm]
	plt.scatter(X[:, 5], y)
	plt.scatter(X_rm, price_by_random_k_and_b)
	plt.show()


def loss(y, y_hat): # to evaluate the performance
	return sum((y_i - y_hat_i)**2 for y_i, y_hat_i in zip(list(y), list(y_hat))) / len(list(y))


def random_get_best_kb():
	times = 10000
	boston = load_boston()
	X, y = boston.data, boston.target
	X_rm = X[:, 5]  # room
	min_loss = float('inf')
	for i in range(times):
		k = random.random() * 200 - 100
		b = random.random() * 200 - 100
		y_hat = [price(r, k, b) for r in X_rm]
		current_loss = loss(y, y_hat)
		if current_loss < min_loss:
			min_loss = current_loss
			msg = "Trying_times:{times:<6d}, best_k: {k:<10.3f}, best_b: {b:<10.3f}, loss: {loss}"
			print(msg.format(times=i, k=k, b=b, loss=current_loss))


def adjusting_get_best_kb():
	times = 1000
	boston = load_boston()
	X, y = boston.data, boston.target
	X_rm = X[:, 5]  # room

	# init best_k, best_b
	k = random.random() * 200 - 100
	b = random.random() * 200 - 100

	# directions, adjusting k and b
	directions = [
		(+1, -1),
		(+1, +1),
		(-1, -1),
		(-1, +1)
	]
	next_direction = random.choice(directions)
	scalar = 0.0001

	min_loss = float('inf')
	for i in range(times):
		k_direction, b_direction = next_direction
		current_k, current_b = k + k_direction * scalar, b + b_direction * scalar
		y_hat = [price(r, current_k, current_b) for r in X_rm]
		current_loss = loss(y, y_hat)
		if current_loss < min_loss:
			k, b = current_k, current_b
			min_loss = current_loss
			msg = "Trying_times:{times:<6d}, best_k: {k:<10.3f}, best_b: {b:<10.3f}, loss: {loss}"
			print(msg.format(times=i, k=k, b=b, loss=current_loss))
		else:
			next_direction = random.choice(directions)



draw(8.351, -29.747)
random_get_best_kb()
adjusting_get_best_kb()

