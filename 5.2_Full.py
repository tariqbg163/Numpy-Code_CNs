# Creatin array using full method full((size), value, dtaype)
import numpy as np

# Creating 1-D array 
# full( size of an array  , value to be in array )
ar=np.full(8,2) # by default data type is int  .. 8(row) is size and  2 is value
print(" ar = " , ar)

ar2=np.full(6,3 , dtype=float) # 6(i.e (6,1)) is size and 3 is the value to be in the matrix
print("ar2 = ", ar2)

# Creating 2-D array  full( (dimension) , value , dtype)
ar3=np.full((4,3), 8, dtype=str) # (4,3) size and 8 is value
print("ar3 = ", ar3)