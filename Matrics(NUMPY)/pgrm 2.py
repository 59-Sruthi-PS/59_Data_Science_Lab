#find the no of rows and colums of a given matrics using numpy.

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6],[12,4,32],[22,12,11]])
print('A =',arr)
shape = np.shape(arr)
rows,columns =  arr.shape
print('no of rows: ', rows)
print('no of columns :',columns)