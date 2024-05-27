import numpy as np
import sys  #  to find the size of  variable
# Numpy is numerical python ..use for creating multiple dimension array
# Numpy array have only homogenous type elements
# Why Numpy over list   
   # 1)  Memory Consumption 
list=[11,22,33,44,]
a=55
list.append(a)  # a is added to the list
print("Size one element of list_array = ", sys.getsizeof(a))
print("Total size o 5 elements of list_array = ", len(list) * sys.getsizeof(a))

# size of numpy array.
np_array=np.array([11,22,33,44,55])
print("Size of each element of np_array = ", np_array.itemsize) 
# total size of np_array is = total no of elements * size of one element
print("Total size of 5 elements of numpy array = ", len(np_array)*np_array.itemsize)

list_size= len(list)*sys.getsizeof(a)
np_size= len(np_array) * np_array.itemsize
dif_size=list_size - np_size

print(f"List_array occupy extra {dif_size} byte then numpy_array of same size.")

""" 
import numpy as np
import sys
# finding size of list
list_ar=[11,22,33,44,55]   # each element size of list array is 28 byte
print("List ar = ", sys.getsizeof(list_ar))

ar=np.array([11,22,33,44,55,66,77,88])
print(ar)                         # each element size of numpy array is 4 byte
# finding size of an numpy array
print("size on numpy array = ", len(ar) * ar.itemsize)

"""