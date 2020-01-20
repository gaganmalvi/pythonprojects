import matplotlib.pyplot as plt
school = [2014,2015,2016,2017,2018]
result = [20,30,70,90,60]
plt.bar (school,result,edgecolor = 'red')
plt.xlabel('School')
plt.ylabel('Result')
plt.title('School Result')
plt.show()
