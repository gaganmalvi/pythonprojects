import pymysql as p
c = p.connect(host = 'localhost',
              user = 'root',
              password = 'root',
              database = 'college')
a = c.cursor()
fetchop = 'select * from student;'
a.execute(fetchop)
z = a.fetchall()
print('RollNo\tName\tMarks')
for i in z:
    for j in i:
        print(j,end='\t')
    print()
