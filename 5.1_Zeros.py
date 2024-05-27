# Creating zeros array
import numpy as np

ar=np.zeros(3) # default it elements is float
print("ar = ", ar)
print(" shape ar = ", np.shape(ar))

ar2=np.zeros(4, dtype=str)
print("ar2 = ", ar2)
print("Shape ar2 = ", np.shape(ar2))

ar3=np.zeros(5, dtype=int)
print("ar3 = ", ar3)
print("Shape ar3 = ", np.shape(ar3))

# Creating 2D array  zeros((dimension), dtype=int,float,str)
ar4=np.zeros((2,3) , dtype=int)
print("ar4 = ", ar4)
print("Shape ar4 = ", np.shape(ar4))
