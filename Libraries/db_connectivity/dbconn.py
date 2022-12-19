import mysql.connector as con

mydb=con.connect(user="vsw",passwd="1272",database="db1")

mycursor=mydb.cursor()

mycursor.execute("select * from student")


for i in mycursor:
    print(i)