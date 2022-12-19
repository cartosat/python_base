import mysql.connector as con

myob=con.connect(user='vsw',passwd='1272',database='db1')

mycur=myob.cursor()
mypri=myob.cursor()



mycur.execute("insert into teacher value(1,'Anarse.D.P','Comp')")

mypri.execute("select * from teacher")

for i in mypri:
    print(i)