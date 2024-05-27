# Numpy Operations i
import numpy as np

ar=np.array([[1,2,3], [4,5,6],[7,8,9]])
ar2=ar*2 # duble the values of an array  .. in list it repeat the elements
print("ar2 = ", ar2)

# adding scalar to every elements of an array
ar3=ar+1
print("ar3 = ", ar3)

# a +b, a-b,  it is done element by element when a and b have same dimension
ar4=np.array([2,3,4])
ar5=np.array([5,6,7])
ar6= ar4 * ar5             # also / division
print("ar6 = ", ar6)