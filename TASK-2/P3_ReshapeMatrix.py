#TRY-1 3/4 Test Cases Passed
# import numpy as np

# def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
# 	reshaped_matrix=np.reshape(a,new_shape)
# 	return reshaped_matrix

#TRY-2
import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	# original=sum(len(row) for row in matrix)
	# valid=new_shape[0] * new_shape[1]
	# if original==valid:
	if  sum(len(row) for row in a)==new_shape[0] * new_shape[1]:
		reshaped_matrix=np.reshape(a,new_shape)
		return reshaped_matrix
	else:
		return []
