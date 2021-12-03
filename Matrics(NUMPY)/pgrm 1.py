#get the max and min value from given matrics.

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6],[12,4,32],[22,12,11]])
maxValue = np.amax(arr)
print('Max value from the array : ', maxValue)
minValue = np.amin(arr)
print('minimum value from the array :',minValue)