# it another way to create numpy array
# linspace method is controll over the number of simple generated

import numpy as np
ar=np.linspace(4,12) # linspace(start,end ,dtype) , start,end is included dtype is float
print("ar = ", ar)  # default data type is float

# linspace(start,stop(end), numbe of simple to be generated , dtype,  endpoint=True,False)
# endpoint= false then last number is not included i.e excluded else default true and included
ar2=np.linspace(3,15, 8 , dtype=int)  # default endpoint=True i.e last number is included
print("ar2 = ", ar2)

ar3=np.linspace(4,18 , endpoint=False, dtype=int) # endpint=False 18 exclude
print("ar3 = ", ar3)

# linspace(restep=True) then it show the array with step(incremental value) value
# By defalut restep =Fasle which only show the array not the step value
ar4=np.linspace(2,16, 8, endpoint=True, dtype=int, retstep=True)
print("ar4 = ", ar4)