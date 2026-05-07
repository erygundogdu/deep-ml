def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	pass
	##b is the vector 
	

	r = len(a) ##num of row
	c = len(a[0])
	lst = []
	if c != len(b):
		return -1
	for i in range(r):
		sm = 0
		for k in range(len(a[i])):
			sm += a[i][k] * b[k]
		lst.append(sm)
	return lst

	return sm
	#col_lst = []
	#for i in range(c):
		#cols = []
		#for k in range(r):
			#val = a[i][k]
			#cols.append(val)
		#col_lst.append(cols)
	
