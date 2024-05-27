import numpy as np
import sys
# finding size of list
list_ar=[11,22,33,44,55]   # each element size of list array is 28 byte
print("List ar = ", sys.getsizeof(list_ar))

ar=np.array([11,22,33,44,55,66,77,88])
print(ar)                         # each element size of numpy array is 4 byte
# finding size of an numpy array
print("size on numpy array = ", len(ar) * ar.itemsize)