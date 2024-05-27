import numpy as np
height=np.array([5.60,5.63,5.70,5.66,5.64])
mean=np.mean(height)
print(f"mean of height is {mean}")

height=height.sort()

median=np.median(height)

print(f"Medain of height is {median}")

# mode==np.mod()