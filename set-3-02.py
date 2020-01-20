import pymysql as p
c = p.connect(host = 'localhost',
              user = 'root',
              password = 'Gaganmalvi@123',
              database = 'college')
a = c.cursor()
delval = input('Enter Roll Number of student whose record you want to purge. :')
a.execute('delete from student where rno = '+delval)
c.commit()
print('Successfully deleted. Exiting...')
