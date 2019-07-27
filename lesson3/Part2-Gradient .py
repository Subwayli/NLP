import random
from sklearn.datasets import load_boston
import pandas as pd
import matplotlib.pyplot as plt


def loss(y, y_hat):  # to evaluate the performance
	return sum(abs(y_i - y_hat_i) for y_i, y_hat_i in zip(list(y), list(y_hat))) / len(list(y))


def draw(k, b):
	boston = load_boston()
	X, y = boston.data, boston.target
	X_rm = X[:, 5]
	price_by_random_k_and_b = [price(r, k, b) for r in X_rm]
	plt.scatter(X[:, 5], y)
	plt.scatter(X_rm, price_by_random_k_and_b)
	plt.show()


def price(rm, k, b):
	return k * rm + b


def partial_k(x, y, y_hat):
	n = len(y)
	return -2 / n * sum((y_i - y_hat_i) * x_i for x_i, y_i, y_hat_i in zip(list(x), list(y), list(y_hat)))


def partial_b(y, y_hat):
	n = len(y)
	return -2 / n * sum(y_i - y_hat_i for y_i, y_hat_i in zip(list(y), list(y_hat)))



def gradient_get_best_kb():
	times = 10000
	boston = load_boston()
	X, y = boston.data, boston.target
	X_rm = X[:, 5]  # room

	# init best_k, best_b
	k = random.random() * 200 - 100
	b = random.random() * 200 - 100

	learning_rate = 1e-04

	min_loss = float('inf')
	for i in range(times):
		y_hat = [price(r, k, b) for r in X_rm]
		current_loss = loss(y, y_hat)
		if current_loss < min_loss:
			min_loss = current_loss
			if i % 100 == 0:
				msg = "Trying_times:{times:<6d}, best_k: {k:<10.3f}, best_b: {b:<10.3f}, loss: {loss_f}"
				print(msg.format(times=i, k=k, b=b, loss_f=current_loss))
		k_direction = partial_k(X_rm, y, y_hat)
		b_direction = partial_b(y, y_hat)
		k = k + -1 * k_direction * learning_rate
		b = b + -1 * b_direction * learning_rate
	draw(k, b)



gradient_get_best_kb()
