import numpy as np
def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
	if sum(a[0])==sum(b):
		c=np.matmul(a, b)
		return c
	else:
		return -1
