import pymysql as p
c = p.connect(host = 'localhost',
              user = 'root',
              password = 'root',
              database = 'college')
a = c.cursor()
updrno = input('Enter the roll number of the student whose record you want to update. :')
updcol = input('Enter the field you want to change. :')
updval = input('Enter the final value which you want to update. :')
updquery = 'update student set '+updcol+' = '+updval+' where rno = '+updrno
a.execute(updquery)
c.commit()
print('Executed successfully. Exiting...')

