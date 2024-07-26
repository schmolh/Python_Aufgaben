import pandas as pd

# Bitte noch folgende Module installieren
# pip install matplotlib
# pip install openpyxl

df = pd.read_csv('Data_dup.csv')
df_dupResul=df.duplicated()
i=0
print(df_dupResul)

#dies ist die Lösung
df=df.drop_duplicates(keep='first')
'''
for Ergebnis in df_dupResul:
    print(Ergebnis)

    i=i+1
'''

df_dupResul=df.duplicated()
print(df_dupResul)
df.to_excel("Data_dup.xlsx")


