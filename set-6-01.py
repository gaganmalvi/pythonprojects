import matplotlib.pyplot as plt
Math = [35,56,34,89,87,56,65]
Phy = [45,65,87,99,98,46,91,15]
Chem = [65,94,51,87,64,38,92]
plt.hist([Math,Phy,Chem], label = ['Math','Phy','Chem'], edgecolor = 'red')
plt.xlabel('Marks in subject')
plt.ylabel('Number of students')
plt.legend()
plt.title('Marks Analysis')
plt.grid()
plt.show()
