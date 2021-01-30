import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)

outside = 'G1 G1 G1 G2 G2 G2'.split()
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))

hier_index = pd.MultiIndex.from_tuples(hier_index)

print(hier_index)

df = pd.DataFrame(randn(6,2),hier_index,['A','B'])
print(df)

df.index.names = ['groups', 'nums']
print(df)

print(df.xs('G1'))
print(df.xs(1,level='nums'))
