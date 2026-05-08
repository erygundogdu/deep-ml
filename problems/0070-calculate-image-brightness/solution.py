import  numpy as np
def calculate_brightness(img):
	# Write your code here
	if img == []:
		return -1
	dct = {}
	for i in img:
		if len(i) in dct:
			dct[len(i)] += 1
		else:
			dct[len(i)] = 1
	if len(dct.keys()) != 1:
		return  -1
	img = np.array(img)
	mx = img.max()
	if mx > 255:
		return -1

	
	H = img.shape[0]
	W = img.shape[1]
	
	arr = img.reshape(H*W,1)
	mean = arr.mean()
	return mean
	
	pass
