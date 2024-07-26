import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({"area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] },
        index=["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"])

print(df)

df.to_excel("pd_04_to_excel.xlsx")

df.plot(kind = 'bar')
#df["population"].plot(kind = 'bar')
plt.gcf().set_size_inches(10,8)

plt.show()

