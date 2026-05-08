import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	y = np.array(y)
	X = np.array(X)
	cross = X.T @ y
	auto = X.T @ X
	psedu_inv = np.linalg.inv(auto)
	theta = psedu_inv @ cross
	return theta.astype(np.float32)