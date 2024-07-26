import pandas as pd
import numpy as np
d = {'col1': [1, 4, 3, 4, 4], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 8, 1]}
df = pd.DataFrame(data=d)
print("Original DataFrame")
print(df)
print('Rows for colum1 value == 4')
print(df.loc[df['col1'] == 4])

print()

# 1. print alle Datensätze mit ['col3'] = 8 
print(df.loc[df['col3'] == 8])

# 2. print alle Datensätze mit (['col3'] = 8) & (['col1'] = 4)

print(df.loc[(df['col3'] == 8 ) & (df['col1'] == 4)] )