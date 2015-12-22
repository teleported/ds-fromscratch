#!/usr/bin/python

import matplotlib
matplotlib.use('Qt4Agg')

from collections import Counter
from matplotlib import pyplot as plt
import random

grades = random.sample(range(100), 10)
deciles = [i // 10 * 10 for i in grades]
histogram = Counter(deciles)

plt.bar([k - 4 for k in histogram.keys()], histogram.values(), 8)
plt.axis([-5, 105, 0, 5])
plt.xticks([10 * i for i in range(11)])
plt.xlabel('Decile')
plt.ylabel('# Students')
plt.title('Histogram')
plt.show()
