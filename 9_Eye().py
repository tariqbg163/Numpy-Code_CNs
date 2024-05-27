# eye() reurn a rectangular matrix if size m=n i.e n*m then it return the square matrix
import numpy as np
ar=np.eye(4, dtype=int) # if single value  is pass then it return a square matrix
print("ar = ", ar)

# if size m!=n then it return a rectangular matrix
# eye(rows,columns , dtype)
ar2=np.eye(2,5 ,dtype=int) # dtype=float by default
print("ar2 = ", ar2)