import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	if new_shape[0] * new_shape[1] != len(a) * len(a[0]):
		return []
	arr = np.array(a)
	arr = arr.reshape(new_shape[0],new_shape[1])
	return arr.tolist()
	
