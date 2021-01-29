#DATA FRAMES
import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5,4),['a','b','c','d','e'],['w','x','y','z'])
print(df)

#Selecting a column
print(df['w'])
print(df[['w','x','z']])

#creating a new column

df['sum of W&Y'] = df['y']+df['w']
print(df)

#deleting a column
print(df)
df.drop('sum of W&Y',axis=1)
print(df)
df.drop('sum of W&Y',axis=1,inplace=True)
print(df)

#deleting a row
#print(df)
#df.drop('e',axis=0,inplace=True)
#print(df)

#Selecting row based on labeled index
print(df.loc['c'])

#Selecting row based on inddex(numerical)
print(df.iloc[2])

#Selcting a paticular value of df
print(df.loc['b','y'])

#Selecting a subset of df
print(df.loc[['a','b'],['w','y']])