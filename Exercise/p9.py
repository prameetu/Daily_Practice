import numpy as np
import pandas as pd

df = pd.read_csv('example')
print(df)

df.to_csv('My_output.csv',index=False)
print(pd.read_csv('My_output.csv'))
