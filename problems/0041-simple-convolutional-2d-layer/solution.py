import numpy as np

def simple_conv2d(input_matrix: np.ndarray, kernel: np.ndarray, padding: int, stride: int):
	input_height, input_width = input_matrix.shape
	kernel_height, kernel_width = kernel.shape

	# Your code here
	p = padding
	s = stride
	k = kernel_height
	input_matrix = np.pad(input_matrix, pad_width=p, mode="constant", constant_values=0)

	result = []
	for i in range(0,input_matrix.shape[1]-k+1,s):
		horz = []
    	for j in range(0,input_matrix.shape[1]-k+1,s):

        	win = input_matrix[i:i+k,j:j+k]
			res = (win * kernel).sum()
			horz.append(res.tolist())
		result.append(horz)
    
	return result
