#!/usr/bin/python
from __future__ import division
import sys
sys.path.append('../chapter04')
from collections import Counter
import vectorlib
import math

def mean(v):
	if v is None or len(v) == 0:
		return 0

	return sum(v)/len(v)

def median(v):
	if v is None or len(v) == 0:
		return 0

	n = len(v)
	sorted_v = sorted(v)
	mid = n // 2
	if not (n % 2): # Even
		return (sorted_v[mid] + sorted_v[mid-1]) / 2
	else:
		return sorted_v[mid]

def mode(v):
	c = Counter(v)
	max_count = max(c.values())
	return [x_i for x_i, count in c.iteritems() if count == max_count]

def quantile(v, p):
	p_index = int(p * len(v))
	return sorted(v)[p_index]

def interquantile_range(v):
	return quantile(v, 0.75) - quantile(v, 0.25)

def data_range(v):
	if v is None or len(v) == 0:
		return 0
	return max(v) - min(v)

def de_mean(v):
	m = mean(v)
	return [x - m for x in v]
	
def variance(v):
	n = len(v)
	return vectorlib.sum_of_squares(de_mean(v))/(n - 1)

def deviation(v):
	return math.sqrt(variance(v))

def covariance(v, w):
	if v is None or w is None or not len(v) or not len(w):
		return 0

	n = len(v)
	return vectorlib.dot(de_mean(v), de_mean(w)) / (n - 1)

def correlation(v, w):
	stddev_v = deviation(v)
	stddev_w = deviation(w)
	if stddev_v > 0 and stddev_w > 0:
		return covariance(v, w)/ stddev_v / stddev_w
	else:
		return 0 

if __name__ == '__main__':
	v = [1, 2, 3, 4, 4, 3, 50]
	w = [66, 3, 2, 5, 1, 5, 4]
	print v
	print mean(v)
	print median(v)
	print mode(v)
	print data_range(v)
	print variance(v)
	print deviation(v)
	print quantile(v, 0.2)
	print covariance(v, w)
	print correlation(v, w)
