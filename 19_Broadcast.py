# Broadcast --> How Numpy will treat the unequal dimension array during operations
# a=(2,3) and b=(2,3) operations are ok
# a=(2,3) and b=(3,2) not possible operations
# a=(2,3) and b=(3) i.e (1,3) 1 is hide so it looks like (3,) and we use Broadcasting.
# Note.. if A(n*m) and B(n*m) is compatible of if m=n if column of first= rows of 2nd
# (1,n) is represented as (n) e.g (1,4) = (4) 

import numpy as np
# Creating same size array and Mathematical Operations on it
ar1=np.random.randint(1,10, (3,4))
ar2=np.random.randint(1,10, (3,4))

ar_reslut= ar1 - ar2   # +, *, / , // , **(square)
print("ar_result = ", ar_reslut)

# Creating (1,n)=(n) array
ar3=np.random.randint(1,10 , (3,3)) #creating array from 1 to 10(exclute) size= (3,3)
ar4=np.random.randint(1,10, (3))   # size=(1,3)=(3)
ar5= ar3-ar4
print("ar5 = ", ar5)
""" Actually What happen .a suppose (1,3) is an arrray size of [1,2,3] which is treated
is (3) and the array is converted to [[1,2,3] ,[1,2,3], [1,2,3]] i.e (3,3)"""

# Creating different size arrays
arr1=np.random.randint(1,20, (2,3)) 
arr2=np.random.randint(1,20, (3,2))
# arr3=arr1-arr2    it gives error b/c of size (2,3) and (3,2) non of the row=row or clm=clm 
# so we take the transpose of one of the array

arr3=np.transpose(arr2)  # (3,2) after transpose it converts to (2,3)
arr4= arr1-arr3
print("arr4 = ", arr4)