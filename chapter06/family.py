#!/usr/bin/python
from __future__ import division
import random

def get_random_child():
	return random.choice(['boy', 'girl'])


both_girls = 0
older_girl = 0
either_girl = 0
random.seed(0)
for _ in range(1000000):
	older = get_random_child()
	younger = get_random_child()

	if older == 'girl':
		older_girl += 1
	if older == 'girl' and younger == 'girl':
		both_girls += 1
	if older == 'girl' or younger == 'girl':
		either_girl += 1
	

print "P(both | older)", both_girls / older_girl
print "P(both | either)", both_girls / either_girl
	
