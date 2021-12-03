#python code to demonstrate matrics add,substract and division

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6],[2,3,5]])
arr1 = np.array([[1,2,3],[2,3,4],[1,1,1]])
print('Array1 =',arr)
print('Array2 = ',arr1)
add = np.add(arr,arr1)
print('addition of two matrics :',add)
sub = np.subtract(arr,arr1)
print('substraction of two matrics :',sub)
div = np.divide(arr,arr1)
print('division of two array', div)
