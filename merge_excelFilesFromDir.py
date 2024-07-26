import pandas as pd
import os

# use below command to install pandas
# pip install --upgrade pandas openpyxl

directory="ExcleFiles"
outputfile="NewExcelMerged.xlsx"

arr = os.listdir(directory)
df_all=pd.DataFrame()

for file1 in arr:
    print("lese File:", file1)
    df_tmp=pd.read_excel(file1)
    df_all=df_all.append(df_tmp)

outputfileWithDir=directory+"\\"+outputfile

print("schreibe File nach: ", outputfileWithDir)
df_all.to_excel(outputfileWithDir, index=False)


