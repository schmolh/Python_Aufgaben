import pandas as pd
import os

# use below command to install pandas
# pip install --upgrade pandas openpyxl

directory="ExcleFiles"
outputfile_append="NewExcelConcat.xlsx"
outputfile_merge="NewExcelMerged.xlsx"

arr = os.listdir(directory)
df_all=pd.DataFrame()
df_both_col=pd.DataFrame()

for file1 in arr:
    print("lese File:", file1)
    if file1.startswith("pd"):
        df_tmp=pd.read_excel(directory+"\\"+file1)
        #df_all=df_all.append(df_tmp)
        df_all=pd.concat([df_all,df_tmp])
        if df_both_col.empty:
            df_both_col=df_tmp
        else:
            df_both_col=pd.merge(df_both_col, df_tmp, on='Name', how='inner')


print(df_all)
print()
print(df_both_col)


#print("schreibe File nach: ", outputfileWithDir)
df_all.to_excel(directory+"\\"+outputfile_append, index=False)
df_both_col.to_excel(directory+"\\"+outputfile_merge, index=False)


