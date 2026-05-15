import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code here
	scores = np.array(scores)
	scores = scores - max(scores)
	exp = np.exp(scores)
	sm = np.sum(exp)
	out = exp / sm
	out = np.log(out)

	return out.tolist()
	pass