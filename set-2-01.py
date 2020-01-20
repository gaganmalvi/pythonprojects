import pandas as pd
import numpy as np
df = pd.DataFrame({'Set1':[4,16,25,36],
                   'Set2':[16,25,36,64],
                   'Set3':[36,49,64,81]})
df1 = df.applymap(np.sqrt)
print('Original DataFrame: \n',df)
print('After applying applymap(np.sqrt) function to find the square root of the\noriginal dataframe, resulting dataframe is: \n',df1)
