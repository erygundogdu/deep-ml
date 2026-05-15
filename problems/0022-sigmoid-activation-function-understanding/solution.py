import math
import numpy as np

def sigmoid(z: float) -> float:
	#Your code here
	exp = np.exp(z)
	result = exp / (1+exp)
	return result