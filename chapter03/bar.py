#!/usr/bin/python

import matplotlib
matplotlib.use('Qt4Agg')

from matplotlib import pyplot as plt

days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat']
sale = [110, 40, 60, 50, 70, 80, 90]

xs = [i + 0.1 for i, _ in enumerate(days)]
plt.bar(xs, sale)

plt.xticks([i + 0.5  for i, _ in enumerate(days)], days)

plt.ylabel("Avg Sales")
plt.xlabel("Day of week")
plt.title("Average sale across days of week")

plt.show()
