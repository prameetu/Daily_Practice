#UNDERSTANING SERIES IN PANDAS
import  numpy as np
import pandas as pd

labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30}

a = (pd.Series(data=my_data))
print(pd.Series(data=my_data,index=labels))
print(a)

a = pd.Series(arr,labels)
print(a)

#Grabbing information from series

ser1 = pd.Series([1,2,3,4],['USA','GERMANY','USSR','JAPAN'])
ser2 = pd.Series([1,2,5,4],['USA','GERMANY','Italy','JAPAN'])
print(ser1)
print(ser2)
print(ser1['USA'])
ser3 = pd.Series(labels)
print(ser3)
print(ser3[2])
