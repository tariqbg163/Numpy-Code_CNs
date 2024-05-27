import numpy as np

# Creating numpy array

li_arr=[11,22,33,"a",66.78, "c"]
print("li = ", type(li_arr))
print("list = ", li_arr , " \n" )

# numpy array is consist of only of time of data
np_arr=np.array(li_arr)  # As li is consist of d/f types  so numpy arr convets to string
print("np arr = ", type(np_arr))
print("np arr= ", np_arr)
print("\n")

# To create user want type numpy array add a data type argumets
# it will not change( convert the sting element) into change int and float
li_arr2=[11,22,"333",55,78.6666]
np_arr2=np.array(li_arr2, dtype=int)  # dtype=int , float, str, bool(true or false)
print("np arr = ", np_arr2)


# arr =np.array(any iterable or sequnce) # list,tuple, set ,dictionary
a=np.array({11:"Khan", 22:"Ku"})
print(a)