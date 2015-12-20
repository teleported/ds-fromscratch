#!/usr/bin/python

f = open('sherlock.txt','r')

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
	if count > 10:
		break
