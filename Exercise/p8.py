import pandas as pd

df = pd.DataFrame({'col1':[1,2,3,4],
                   'col2':[444,555,666,444],
                   'col3':['abc','def','ghi','xyz']})
print(df['col2'].unique())
print(df['col2'].nunique())
print(df['col2'].value_counts())

#applying a custom or bulit in function to pandas data frames

print(df['col3'].apply(len))
print(df['col2'].apply(lambda x: x*2))

#retriving columns and index of data frames

print(df.columns)
print(df.index)

#sorting coulumns
print(df.sort_values(by='col2'))

#

print(df.isnull())

#pivot_tables i.e. creating sub dataframe out of a datframe

data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)
print(df)

print(df.pivot_table(values='D',index=['A','B'],columns='C'))
