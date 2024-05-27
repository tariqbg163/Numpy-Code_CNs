# We can also used logical operator work one each element
# ar. logical_or(ar1,ar2.,..arn)  binary operator
# ar. logical_and(ar1,ar2,...arn)  binary operator
# ar.logical_not(ar1)        unary operator   

import numpy as np
ar=np.array([11,22,33,44,55,66,77])
ar2=np.array([11,22,44,33,11,77,88])

# campare each element if 
print("logical_or = ", np.logical_or(ar,ar2)) # return true array b/c all are non zero values
print("logical_and = ", np.logical_and(ar, ar2))
print("logical_not = ", np.logical_not(ar))  # unary operator
