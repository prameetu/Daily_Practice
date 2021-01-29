import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5, 4),['A','B','C','D','E'],['w','x','y','z'])
print(df)

bool_df =(df > 0)
print(bool_df)

print(df[bool_df])

print(df[df['w'] > 0 ])

print(df[ df['w'] > 0 ]['y'])

print(df[(df['y'] > 1) | (df['w'] > 0)])

print(df.reset_index())

#SETTING NEW INDEX AS A COLUMN
states = "AP PJ OR UP MP".split()
df['STATES']= states
print(df)
print(df.set_index('STATES'))