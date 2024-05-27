# shane() in numpy 
import numpy as np
ar=np.random.randint(1,10, (3,4))
print("before reshape ar = ", ar , "shape = ", ar.shape)

ar2=np.reshape(ar, (4,3))   # ar2= ar.reshape(4,3)   4,3 is new shape

print("after reshape ar2 = ", ar2 , " shape = ", ar2.shape)
 