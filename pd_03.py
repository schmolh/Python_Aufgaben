import pandas as pd
# Bitte noch folgende Module installieren
# pip install matplotlib
# pip install openpyxl

df = pd.read_csv('data.csv')

x = df["Calories"].mode()[0]

df["Calories"].fillna(x, inplace = True)

print(df.to_string())

#As you can see in row 18 and 28, the empty value from "Calories" was replaced with the mode: 300.0