import numpy as np
import pandas as pd

data = {'Company':"GOOG GOOG FB FB MSFT MSFT".split(),
        'Person':'Sam Charlie Amy Vanessa Carl Sarah'.split(),
        'Sales':[220, 120, 340, 124, 243, 350]}

df = pd.DataFrame(data)
print(df)

byComp = df.groupby('Company')
print(byComp.mean())

print("\n")
print(df.groupby('Company').sum().loc['FB'])

print(df.groupby('Company').count())
print(df.groupby('Company').max()['Sales'])
print("--------------------------------------------------\n")
print(df.groupby('Company').describe())
print("--------------------------------------------------\n")

print(df.groupby('Company').describe().loc['FB'])
