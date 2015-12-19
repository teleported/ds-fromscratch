#!/usr/bin/python

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

dict1 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four'}
print dict1
print sorted(dict1, key=lambda x: dict1[x])
