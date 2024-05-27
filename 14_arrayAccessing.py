# Accessing array element
import numpy as np

# accessing 1-D array elements
ar=np.array([11,22,33,44,55,66,77,88,99,10,20])
print("2nd element of ar = ", ar[1])
print("4th element of ar = ", ar[3])

# Accessing through slicing operator
print("2 to 6th elment = ", ar[1:6]) # 1 include , 6 exclude 

# Accessing 2-D array elements  arrayName[rowNumber][elementNumber]
ar2=np.array([[11,22,33,67,54], [44,55,66,85,89], [77,88,99,61, 42]])
print("Ist row 2nd element = ", ar2[0][1])  # first row 2nd element
print("2nd row 3rd element = ", ar2[1][2]) # this same as for list
# another method which is not supported by list
print("3rd row ist element = ", ar2[ 2, 0]) # ar[ row_No , element_No]


# slicing operator in 2-D array..> arrayName[row_No][slicing_Operator]
print("3rd row ,2 to 4 elements = ", ar2[2][2:5])   # or below also same for array only
print("2nd row 3 to 5th element = ", ar2[1, 2:6])

