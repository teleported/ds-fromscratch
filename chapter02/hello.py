#!/usr/bin/python

from __future__ import division

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

