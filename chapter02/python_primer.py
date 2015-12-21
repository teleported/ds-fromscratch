#!/usr/bin/python

from __future__ import division
from collections import defaultdict
from collections import Counter

import random
import time

print ('Hello World')

# White space
line1 = (1 + 2 + 3
    + 4 + 5)
print (line1)

multi_line = """This is an arbritraty adhoc
 line"""
print (multi_line)

# List of lists
list1 = [[1, 2], [3, 4], [5, 6]]
print(list1)

# Arithmetic
d = 4  / 3
print (d)
d1 = 4 // 3
print (d1)

# Functions and Lambda

def double(val=7):
	return val * 2

print (double())

def execute(fn, val):
	return fn(val)

print (execute(double, 4))

triple = lambda x: x*3

print (execute(triple, 4))

# Strings

s1 = 'data science'
s2 = "Data Science"
s3 = "\tRaw"
s4 = r"\tRaw"

print (s1)
print (s2)
print (s3)
print (s4)



# Exceptions

try:
	print 0/0
except ZeroDivisionError:
	print "Cannot divide by zero"

# Lists
list1 = []
list1.append(1)
list1.append(2)
list1.append(3)
list1[2] = 33
list2 = [4, 5, 6]
list1.extend(list2)
print list1
print list1[:]
print list1[1:]
print list1[:-1]
print list1[1:-1]

contains = lambda l, x: x in l
print contains(list1, 4)
print contains(list1, 41)

_, y = [1, 2]
print y

# Tuples
t1 = (1, 2)
print t1
try:
	t1[0] = 3
except TypeError:
	print "Cannot modify tuple"

def return_tup(a, b):
	return (a, b)

c, d = return_tup(55, 66)
print c
print d

# Dictionary
d1 = {}
print d1
d2 = {1:'Sunday', 2:'Monday'}
d2[3] = 'Tuesday'
print d2
try:
	val = d2[4]
except KeyError:
	print "Key not in dict"

print 1 in d2
print 100 in d2
print d2.get(100)
print d2.get(100, 'NA')

tweet = {
	"user":	"anand",
	"text": "hello world",
	"retweet_count": 101,
	"hashtags": ['#first', '#program', '#test']
}
print tweet
print tweet.keys()
print tweet.values()
print tweet.items()


# List
l = [5, 7, 2, 6, 1]
# lists can sort inplace
l.sort()
print l

# Tuple
t = (5, 7, 2, 6, 1)
print t
# a new sorted tuple is created
t = sorted(t)
print t

# Sort by key
str1 = "My name is Albert Einstein"
print sorted(str1.split())
print sorted(str1.split(), key=str.lower)
# Inefficient
dict1 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four'}
print dict1
print sorted(dict1, key=lambda x: dict1[x])
# Efficient



# defaultdict

f = open('sherlock.txt','r')

# Not using default dict
# Approach 1
word_count1 = {}
for line in f:
        for word in line.split():
                if word.strip() == "":
                        continue
                if word in word_count1:
                        word_count1[word] += 1
                else:
                        word_count1[word] = 1

s = sorted(word_count1, key=lambda x: word_count1[x], reverse=True)
count = 0
for item in s:
        print item, word_count1[item]
        count += 1
        if count > 5:
                break

# Approach 2

f2 = open('sherlock.txt','r')

word_count2 = {}
for line in f2:
	for word in line.split():
		try:
			word_count2[word] += 1
		except KeyError:
			word_count2[word] = 1

s = sorted(word_count2, key=lambda x: word_count2[x], reverse=True)
count = 0
for item in s:
        print item, word_count2[item]
        count += 1
        if count > 5:
                break


# Approach 3

f3 = open('sherlock.txt', 'r')

word_count3 = {}
for line in f3:
	for word in line.split():
		previous_count = word_count3.get(word, 0)
		word_count3[word] = previous_count + 1

s = sorted(word_count3, key=lambda x: word_count3[x], reverse=True)
count = 0
for item in s:
        print item, word_count3[item]
        count += 1
        if count > 5:
                break

# Using defaultdict
f4 = open('sherlock.txt', 'r')

word_count4 = defaultdict(int)
for line in f4:
	for word in line.split():
		word_count4[word] += 1

s = sorted(word_count4, key=lambda x: word_count4[x], reverse=True)
count = 0
for item in s:
        print item, word_count4[item]
        count += 1
        if count > 5:
                break

# Counter
c = Counter([1,2,3,4,5,6,7,8,9,2,5,8,1])
print c

# Set
s = set([3,3,4,4])
s.add(1)
s.add(1)
s.add('Anand')
print s

# And
i = None
j = 1

print (i or 0)
print (j and 2) 


# all/any

print all([True, 1, "Anand"])
print all([True, 1, ""])
print any([True, 1, ""])


# List comprehensions
even_numbers = [x for x in range(10) if x % 2 == 0]
print even_numbers
squares = [x * x for x in range(10)]
print squares

increasing_pairs = [(x, y) for x in range(10) for y in range(x+1, 10)]
print increasing_pairs


def lazy_range(n):
	i = 0
	while i < n:
		# print "About to yield {0}".format(i)
		yield i
		i += 1

for i in lazy_range(10):
	print i


lazy_evens_below_20 = (i for i in lazy_range(20) if i % 2 == 0)

for i in lazy_evens_below_20:
	print i

# Randomness
random.seed(int(time.time()))
print random.random()
print random.randrange(3, 6)
r1to10 = range(10)
random.shuffle(r1to10)
print r1to10
print random.choice(r1to10)
