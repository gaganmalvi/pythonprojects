#Set-5-Q1
import numpy as np
list1 = [[2,4,6,8],
         [12,14,16,18],
         [22,24,26,28],
         [32,34,36,38]]
arr1 = np.array(list1)
print('The given array is:\n',arr1)
print("\nThe given array's sum is:",np.sum(arr1))
print('\nRow-wise sum is:')
r = np.sum(arr1,axis=1)
count = 1
for i in r:
    print('row ',count,' sum = ',i)
    count += 1
print('\n Columnwise sum is:')
c = np.sum(arr1,axis=0)
count = 1
for i in c:
    print('Column ',count,' sum = ',i)
    count += 1
