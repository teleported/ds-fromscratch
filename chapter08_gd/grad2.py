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


def step(v, slope, step_size):
	return [v_i + slope_i * step_size for v_i, slope_i in zip(v, slope)]

def safe(f):
	def safe_f(*args, **kwargs):
		try:
			return f(*args, **kwargs)
		except:
			return float('inf')
	return safe_f

def minimize_batch(target_fn, gradient_fn, theta_init, tolerance=0.00000001):
	step_sizes = [100, 10, 1, 0.1, 0.001, 0.0001]
	theta = theta_init
	target_fn = safe(target_fn)
	# Out first value
	value = target_fn(theta)

	while True:

		gradient = gradient_fn(theta)
		next_thetas = [step(theta, gradient, -step_size) for step_size in step_sizes]

		next_theta = min(next_thetas, key=target_fn)
		next_value = target_fn(next_theta)
		if abs(value - next_value) < tolerance:
			return theta
		else:
			theta, value = next_theta, next_value

def sum_of_squares(v):
	return sum([v_i * v_i for v_i in v])

def sum_of_squares_gradient(v):
	return [2 * v_i for v_i in v]

def test_fn(v):
	return v[0] * v[0] + v[1]

def test_fn_grad(v):
	return [2* v[0], 0]

if __name__ == '__main__':
	print minimize_batch(sum_of_squares, sum_of_squares_gradient, [3, 6, -10])	
	print "---------------------------------------------"
	print minimize_batch(test_fn, test_fn_grad, [300, 61])	
