import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="Surodi@12")

mycursor=mydb.cursor()

mycursor.execute("show databases")

for i in mycursor:
    print(i)