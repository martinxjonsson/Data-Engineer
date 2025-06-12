import numpy as np 
arr_12d = np.array([[1, 2], [3, 4]])    
arr_22d = np.array([[5, 6], [7, 8]])

result = np.matmul(arr_12d, arr_22d)
print(result)
