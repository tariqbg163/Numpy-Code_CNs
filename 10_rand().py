# Creating a rand\(number of elements) array
# every time it generate rand(size) when we execute it

import numpy as np

# Creating 1-D numpy random array
ar=np.random.rand(3) # it will generate 3 elements array with random values b/2 0 and 1
print("ar = ", ar) # every time we execute we get a new random numpy array


# Creating 2-D random array  
ar2=np.random.rand(3,2)  # rand(rows, columns)
print("ar2 = ", ar2)


# generating one random  foat value
random_value=np.random.rand() # on every execution it gives d/f float value
print("random_value = ", random_value)

#  randint(sigle value) i.e randint(4) but randint(3,5) gives error
value=np.random.randint(8) # on every executio it give d/f int value
print("value = ", value)