import pymysql as p
c = p.connect(host = 'localhost',
              user = 'root',
              password = 'root',
              database = 'college')
a = c.cursor()
a.execute('insert into student values(4,"Shiv",36)')
c.commit()
print('Rows affected: ',a.rowcount)
