## Activation function
# data will be improted as an array

array = [0,1,2,3,4,5,6,7]

def activation(self,array):
	actv_array = []

	for i in range(8):
		actv_val = (array[i]-5) / 5.0
		if actv_val > 0:
			actv_val = 0 
		else:
			actv_val = (abs(actv_val))**2
		actv_array.append(actv_val)
	return np.asarray(actv_array)
    