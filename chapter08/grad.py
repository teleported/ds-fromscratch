#!/usr/bin/python

from __future__ import division
import matplotlib
matplotlib.use('Qt4Agg')
import sys

sys.path.append('../chapter04')

from functools import partial
from matplotlib import pyplot as plt
import vectorlib
import random

def difference_quotient(f, x, h):
	return ((f(x + h) - f(x))/h)

def square(n):
	return n * n

def derivative_square(n):
	return 2 * n

def sum_of_squares_gradient(v):
	return [2 * v_i for v_i in v]	

def partial_difference_quotient(f, v, i, h):
	w = [v_j +  (h if j == i else 0)  for j, v_j in enumerate(v)]	
	return (f(w) - f(v))/h

def estimate_gradient(f, v, h=0.00001):
	return [partial_difference_quotient(f, v, i, h)  for i, _ in enumerate(v)]

def step(v, direction, step_size):
	return [v_i + step_size * direction_i for v_i, direction_i in zip(v, direction)]

if __name__ == '__main__':
	x = range(-10, 10)
	
	plt.plot(x, map(derivative_square, x), 'r+', label='Actual')
	plt.plot(x, map(partial(difference_quotient, square, h=0.00001), x), 'g.', label='Estimated')
	plt.legend(loc=9)
	# plt.show()
	
	v = [random.randint(-10,10) for i in range(3)]
	tolerance = 0.00001

	while True:
		gradient = sum_of_squares_gradient(v)
		next_v = step(v, gradient, -0.1)
		print next_v
		if vectorlib.distance(next_v, v) < tolerance:
			break
		v = next_v

