import pandas as pd
import numpy as np

# Bitte noch folgende Module installieren
# pip install pandas
# pip install numpy

exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data , index=labels)
print("First three rows of the data frame:")
print(df)
print()
print(df.iloc[2:5])

print(df['name'])

df=df.set_index("name")

print(df.loc["Michael"])

# 1. kopiere Zeile 2:5 in ein neues DataFrame df_new
df_new = df.iloc[2:5]
# 2. Schaue mit einer for Schleife ob sich 'James' in der neuen df_new befindet?

for index, row in df.iterrows():
    print()

    if index=='James':
        print("Found ", index)

        print(row)
    else:
        print("not James , is ", index)

