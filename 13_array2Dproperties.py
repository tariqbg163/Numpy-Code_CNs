# Array 2-D properties
import numpy as np
ar=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("index of ist element(byte) = ", ar.data) # ist byte index of an array
print("Dimension of ar = ", ar.shape)
print("Numbe of elments in the ar = ", ar.size)
print("Data type and size in bytes of ar = ", ar.dtype)
print("Number bytes skipped to access the next element of ar = ", ar.strides)
""" Out Put..
Number bytes skipped to access the next element of ar =  (12, 4)
12 represent--> 12 bytes need to be skipped to access the next from elements 
or 12 bytes need to access the next element in the same column

4 represent --> 4 bytes need to be skipped to access the next element in the same row
or 4 bytes need to be skipped to access the next column element 
"""