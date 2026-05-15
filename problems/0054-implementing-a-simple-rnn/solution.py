import numpy as np

def rnn_forward(input_sequence: list[list[float]], initial_hidden_state: list[float], Wx: list[list[float]], Wh: list[list[float]], b: list[float]) -> list[float]:
	# Your code here
	inp = np.array(input_sequence)
	init_hidden = np.array(initial_hidden_state)
	Wx = np.array(Wx)
	Wh = np.array(Wh)
	b = np.array(b)
	def tanh(x):
		exp = np.exp(x)
		exp1 = np.exp(-x)
		out = (exp-exp1) / (exp+exp1)
		return out
	for x_t in inp:
		v = Wx @ x_t + Wh @ init_hidden   + b 
		z = tanh(v)
		init_hidden = z
	final_hidden_state = z
	return final_hidden_state