#!/usr/bin/python

from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980]
gdp   = [1.22, 3.98, 4.98, 6.11]

plt.plot(years, gdp, color='green')
plt.show()
