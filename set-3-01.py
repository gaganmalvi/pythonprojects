import numpy as np
import pandas as pd
df = pd.DataFrame({'item_category':[1,2,2,1,3],
                   'item_name':['red','blue','green','orange','yellow'],
                   'expenditure':[20,30,40,50,60]})
x = df.groupby('item_category')
df1 = x.agg(np.sum)
print(df1)
