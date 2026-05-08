import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	mean = data.mean(axis=0)
	std = data.std(axis=0)
	feat = data.shape[1]
	
	standardized_data = (data -mean) / std
	mx = data.max(axis=0)
	mn = data.min(axis=0)
	normalized_data = (data -mn) / (mx-mn)
	return standardized_data.tolist(), normalized_data.tolist()