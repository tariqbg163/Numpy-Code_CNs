# size function in numpy 
import numpy as np
ar=np.random.randint(1,20, (2,3))
print("before Resize  ar= ", ar)

# resize fun return a new array  .. original array is not change
ar2=np.resize(ar, (3,2))   # (3,2) new dimension of the array
print("After Resize() ar2 = " , ar2)


