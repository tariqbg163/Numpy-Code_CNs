# Creating empty array
import numpy as np

# 1-D array
ar=np.empty(3)   # by default it return float but it can be int, str also
print("ar = ", ar) # return an array of aritrary values in it

# Creating 2-D array
ar2=np.empty((5,2) , dtype=int)  # it return an arbitrary element array
print("ar2 = ", ar2)

ar3=np.empty((5,2) , dtype=str)
print("ar2 = ", ar3)