#Q1
import numpy as np
print('1D NumPy Array')
print('==============')
print('1. Display in Reverse Order')
print('2. Display Only in Even Ordered Index')
x = input ('Enter your choice!:')
if x == '1':
    list1 = [1,2,3,4,5,6]
    ar1 = np.array(list1)
    ar2 = ar1[::-1]
    print('Actual array:\n',ar1)
    print('Reverse array:\n',ar2)
elif x == '2':
    l1 = [1,2,3,4,5,6]
    ar1 = np.array(l1)
    ar2 = ar1[::2]
    print('Actual array:\n',ar1)
    print('Even Ordered Index:\n',ar2)

    
