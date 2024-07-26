import pandas as pd
import numpy as np

# Bitte noch folgende Module installieren
# pip install pandas
# pip install numpy

exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}


# 1. create DataFrame df

# 2. set index of df to "name"

# 3. print DataFrame 

# 4. save df to excel into file 'pd_06_self.xlsx'