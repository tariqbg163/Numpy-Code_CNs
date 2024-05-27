# Creating array using once function
import numpy as np
ar=np.ones(3) # default it creat float type i.e ones(3, dtype=float)
print("ar = ", ar)
print("Dimension(Shape) of ar = ", np.shape(ar))

ar2=np.ones(4, dtype=int)
print("ar2 = ", ar2)
print("Dimension of ar2 = ", np.shape(ar2))

# Creating 2D array  np.ones((dimension), dtype=int,float,str)
ar3=np.ones((3,2), dtype=int)
print("ar3 = ", ar3)
print("Dimension of ar3 = ", np.shape(ar3))
ar4=np.identity(4) # return a squar matrix
print("ar4= ", ar4)