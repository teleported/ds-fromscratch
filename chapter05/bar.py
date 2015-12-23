#!/usr/bin/python
import matplotlib
matplotlib.use('Qt4Agg')
import random
from collections import Counter
from matplotlib import pyplot as plt


num_friends = [random.choice(range(20)) for _ in range(200)]
friend_counter =  Counter(num_friends)

xs = range(21)
ys = [friend_counter[x] for x in xs]

plt.bar(xs, ys)
plt.axis([0, 25, 0, 30])
# plt.xticks(xs , xs)
plt.show()

