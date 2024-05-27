# Relational operator on each element of an array
import numpy as np
ar=np.array([11,22,33,44,55,66,77])
ar2=np.array([11,22,44,33,11,77,88])

# campare each element if <= then it is false   if > the it is true
print("ar < ar2 = ", ar < ar2)  # return a boolean array
print(" ar > ar2 = ", ar > ar2) 
print(" ar == ar2 = ", ar==ar2)
print("ar != ar2 = ", ar != ar2)
