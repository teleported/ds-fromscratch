#!/usr/bin/python
import matplotlib
matplotlib.use('Qt4Agg') 

import random
from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980]
gdp   = [1.22, 3.98, 4.98, 6.11]

plt.plot(years, gdp, color='red', marker='o', linestyle='solid')

num1 = range(2000)
num2 = range(40)

plt.plot(random.sample(num1, 10), random.sample(num2, 10), color='green')

plt.title("This is a demo")

plt.xlabel("The year")
plt.ylabel("Bunch of numbers")


plt.show()
