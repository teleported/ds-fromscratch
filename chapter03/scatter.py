#!/usr/bin/python

import matplotlib
matplotlib.use('Qt4Agg')

from matplotlib import pyplot as plt
import random

friends = random.sample(range(100), 10)
minutes = random.sample(range(100), 10)
labels  = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


plt.scatter(friends, minutes)
for l, f, m in zip(labels, friends, minutes):
	plt.annotate(l, xy=(f, m), xytext=(5, -5), textcoords='offset points')

plt.show()
