# Numpy over list 2) Time Execution
import numpy as np
import time

size=100
def add_List():
    start_t=float(time.time())
    list1=range(size)
    list2=range(size)
    list3=[(list1[i]+list2[i])  for i in range(size) ]
   
    end_t=float(time.time())
    return(end_t - start_t)
list_time=add_List()
print("List_Time = ", list_time * 1000 , "\n")

def add_Np_Array():
    t1=float(time.time())
    np_arr1=np.array(size)
    np_arr2=np.array(size)
    np_arr3= np_arr1+np_arr2
    t2=float(time.time())
    return( t2-t1)

np_arr_time=add_Np_Array()
print("Nump Array exection time = ", np_arr_time ,"\n")

print(f"List_Arr take extra {list_time-np_arr_time} time the nump array of same size.")
