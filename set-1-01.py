import pandas as pd
d1 = {'name':['Tahira','Gurjyot','Anusha','Jacob'],
      'marks':[70,60,40,50]
      'class':[28,36,41,32]}
dfd = pd.DataFrame(d1)
d2 = dfd.pivot(index = 'name',columns = 'marks',values = 'class')
print(d1)
