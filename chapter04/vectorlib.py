#!/usr/bin/python
from __future__ import division
import math

def vector_add(v, w):
	return [v_i + w_i for v_i, w_i in zip(v, w)]

def vector_sub(v, w):
	return [v_i - w_i for v_i, w_i in zip(v, w)]

def vector_sum(vectors):
	return reduce(vector_add, vectors)

def scalar_multiply(c, v):
	return [c * v_i for v_i in v]

def vector_mean(vectors):
	n = len(vectors)
	return scalar_multiply(1/n, vector_sum(vectors))

def dot(v, w):
	return  sum( [v_i * w_i  for v_i, w_i in zip(v, w)])

def sum_of_squares(v):
	return dot(v, v)

def magnitude(v):
	return math.sqrt(sum_of_squares(v))

def distance(v, w):
	return magnitude(vector_sub(v, w))

def shape(A):
	num_rows = len(A)
	num_cols = len(A[0]) if A else 0
	return num_rows, num_cols

def get_row(A, i):
	return A[i]

def get_col(A, j):
	return [A_[j] for A_ in A] 

def gen_matrix(num_rows, num_cols, entry_fn):
	return [[entry_fn(i, j) 
		for j in range(num_cols)]
		for i in range(num_rows)]

def is_diagonal(i, j):
	return 1 if i == j else 0

def print_matrix(A):
	# rows, cols = shape(A)
	print '['
	for row in A:
		print ' ' + str(row)
	print ']'
if __name__ == '__main__':

	# Test the functions
	u = [7, 8, 9]
	v = [1, 2, 3]
	w = [4, 5, 6]
	x = [11, 22, 33]
	mat = [u, v, w, x]
	print 'u, v, w, mat:'
	print u
	print v
	print w
	print mat
	print ''
	print vector_add(v, w)
	print vector_sub(v, w)
	print vector_sum([u, v, w])
	print scalar_multiply(5, v)
	print vector_mean([u, v, w])
	print dot(v, w)
	print sum_of_squares(v)
	print magnitude(v)
	print distance(u, v)
	print shape(mat)
	print get_row(mat, 1)
	print get_col(mat, 1)
	print_matrix(mat)
	print_matrix (gen_matrix(3, 3, is_diagonal))
