import numpy as np

def adam_optimizer(f, grad, x0, learning_rate=0.001, beta1=0.9, beta2=0.999, epsilon=1e-8, num_iterations=10):
	# Your code here
	mt = 0
	vt = 0
	for t in range(1,num_iterations+1):
		g = grad(x0)
		mt = beta1 * mt + (1-beta1)*g
		vt = beta2 * vt + (1-beta2)*(g**2)
		mt_hat = mt / (1-beta1**t)
		vt_hat = vt / (1-beta2**t)
		x0 = x0 -learning_rate * (mt_hat / (np.sqrt(vt_hat)+epsilon))
	return x0


	pass
