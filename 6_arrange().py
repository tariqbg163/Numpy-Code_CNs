# arange fun is used to creat in numpy array
import numpy as  np

# arange(start , end, step,  dtype)  .. start is optional(default 0), end is must(excluded)
# step(space b/w two elements )  optional(default 1) , dtype is also optional

ar=np.arange(1, 10, 2, dtype=float)
print("ar = ", ar)

ar2=np.arange(3,30,2, dtype=int)
print("ar2 = ", ar2)

