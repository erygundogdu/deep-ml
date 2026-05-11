import numpy as np
def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
	# Your code here
	x = features
	y = labels
	W = initial_weights
	b = initial_bias
	lr = learning_rate
	m,n = x.shape[0],x.shape[1]
	scale = 2 / m
	mse_lst = []
	def sigmoid(x):
		return np.exp(x) / (np.exp(x) + 1)
	for epoch in range(epochs):
		v = x @ W.T + b # 3,1
		y_hat = sigmoid(v) #3,1
		mse = np.mean((y-y_hat) ** 2).item()
		mse_lst.append(mse)
		d_y_hat = scale * (y_hat-y)
		d_v = (1-sigmoid(v))*sigmoid(v)
		dw = (d_y_hat * d_v).T @ x
		db = np.sum(d_y_hat * d_v)

		W = W - lr*dw
		b = b -lr*db
	
	mse_values = mse_lst
	updated_weights = W.tolist()
	updated_bias = b

	return updated_weights, updated_bias, mse_values