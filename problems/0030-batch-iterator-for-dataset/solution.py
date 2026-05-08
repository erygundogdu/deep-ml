import numpy as np

def batch_iterator(X, y=None, batch_size=64):
	# Your code here
	k = batch_size
	lst = []
	for i in range(0,len(X),k):
		if i+k > len(X) - 1:
			X_batch = X[i:]
			if y is not None:
				y_batch = y[i:]
				lst.append([X_batch,y_batch])
			else:
				lst.append(X_batch)

		else:
			X_batch = X[i:i+k]
			if y is not None:
				y_batch = y[i:i+k]
				lst.append([X_batch,y_batch])
			else:
				lst.append(X_batch)
	return lst
	pass