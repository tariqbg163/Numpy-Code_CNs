import numpy as np
#  randint(sigle value) i.e randint(4) but randint(3,5) gives error

#randint(low(start->include,optional), high(end->exclude,must), size)

#randint(8) it generate a single value b/w 0 to 8(exclude) on every execution
value=np.random.randint(8) # on every executio it give d/f int value
print("value = ", value)

# Creating random int arry of size 2rows , 3columns b/w 0 to 10(excluded)
ar=np.random.randint(10 , size=(2,3)) 
print("ar = ", ar)

#          low(optional), high  size
# randint( start, endt , size) # if single then it is number of rows
ar2=np.random.randint(1, 20, 5) # size is 5 and it is  1-D array
print("ar2 = ", ar2)

ar3=np.random.randint(2,8, (3,4))  # low=2, high=8 size=(3,4) and 2-D array
print("ar3 = ", ar3)

