# importing pandas package
import pandas as pd

# assign dataset
df1 = pd.read_csv("forcleaning.csv")

# split column and add new columns to df
df1[['line 1', 'line 2', 'line 3', 'line 4']
    ] = df1['ADDRESS'].str.split('\n', expand=True)

df1.to_csv("forcleaning.csv", index=False)
# display the dataframe
print(df1)
