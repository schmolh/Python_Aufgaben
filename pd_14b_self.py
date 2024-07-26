import pandas as pd

df=pd.read_excel("pd_14a.xlsx")
df=df.set_index("Name")
print(df)
print()

df1=pd.read_excel("pd_14b.xlsx")
df1=df1.set_index("Name")
print(df1)

df_merged=pd.merge(df, df1, left_on=['Name'], right_on=['Name'], how='left')

print(df_merged)

df_merged.to_excel("pd_14b_merge_result.xlsx")

# schauen sie sich die Datei pd_14b_merge_result.xlsx und erklären sie was passiert ist