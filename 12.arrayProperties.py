# 1-D arrays properties
#1) array.data --> represent the ist byte(element)  address of an array
#2) array.shape--> represent the size of an array
#3) dtype--> represent the data type of an element in the array
#4) strides-->represent the number of bytes to be skipped to move from one element to another
#5) size---> represent the size of the array i.e number of elements
import numpy as np
ar=np.array([11,22,33,44,55])
print("ar ist element  index = ", ar.data) # index of ist element of an array
print("Size(number of elements) of ar = ", ar.size) # len(ar)
print("ar size = ", ar.shape) # show dimension of  an array
print("ar data type = ", ar.dtype) # return data type of an array and its size in bytes 
print("no of bytes need to move to another element = ", ar.strides)
""" no of bytes need to move to another element =  (4,)  .. mean 4 bytes is to be 
skipped to move to another element of the same row """


