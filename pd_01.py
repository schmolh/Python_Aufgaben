import pandas as pd

df = pd.read_csv('data1.csv')

df.dropna(inplace = True)

#print(df.to_string)


for index,row in df.iterrows():
    print(index,row.Duration, row.Calories)
    print()
    if index == 5:
        df.loc[index, 'Calories'] = 45

print(df.to_string)
df.to_excel("data1_new.xlsx")


