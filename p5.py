#Dealing witha na values in DATA FRAMES

import numpy as np
import pandas as pd

d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[5,6,7]}
df = pd.DataFrame(d)
print(df)

#df.dropna(axis=1,inplace=True)
#Drppoin na values along the columns and also in place

print(df.dropna())#along rows
print(df.dropna(axis=1))
print(df.dropna(thresh=2))