#!/usr/bin/python

import matplotlib
matplotlib.use('Qt4Agg')

import random
from matplotlib import pyplot as plt

variance = random.sample(range(100), 10)
variance.sort()

bias = random.sample(range(100), 10)
bias = sorted(bias, reverse=True)

xs = [i for i, _ in enumerate(variance)]

plt.plot(xs, variance, 'g-', label='variance')
plt.plot(xs, bias, 'r.', label='bias')


plt.legend(loc=9)
plt.axis([0, 11, 0, 110])
plt.show()
