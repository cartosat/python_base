import mysql.connector

myob=mysql.connector.connect(host='192.168.43.226',user="vsw",passwd="1272",database="db1")

mycursor=myob.cursor()

print("Hiii Buddy, BOT3 is at u r Service")
print("What u want to do:-\n1.insert record.\n2.update record.")
choi=int(input())

if choi==1:
    print("We have two tables:-\n1.department.\n2.students.\nEnter u r choice:-")
    choice=int(input())
    if choice==1:
        id=input("enter id:-")
        name=input("enter name of dept:-")
        hod=input("HOD name:-")
        str1="insert into department value("+id+',"'+name+'","'+hod+'")'
        mycursor.execute(str1)
    if choice==2:
        SID=input("enter SID:-")
        name=input("student name:-")
        dept=input("dept name:-")
        str2="insert into department value(" + SID + ',"' + name + '","' + dept + '")'
        mycursor.execute(str2)
if choi==2:
    print("We have two tables which u want to update:-\n1.department.\n2.students.\nEnter u r choice:-")
    choice = int(input())
    if choice == 1:
        print("here is department table:-")
        print("dept_id, name ,hod")
        show="select * from department"
        mycursor.execute(show)
        for i in mycursor:
            print(i)
        feild=input("which field u want to update:-")
        if feild=='dept_id':
            name=input("enter name for which u update id")
            id=input("enter new id:-")

            update='UPDATE department SET dept_id='+id+' WHERE name="'+name+'"'
            mycursor.execute(update)
            print('Record Updated!!')

        if feild == 'name':
            id = input("enter id for which u update name")
            name=input("enter new name:-")

            update = 'UPDATE department SET name="' + name + '" WHERE dept_id='+ id

            mycursor.execute(update)
            print('Record Updated!!')

        if feild == 'hod':
            id = input("enter id for which u update hod")
            hod=input("enter new hod name:-")

            update = 'UPDATE department SET hod="' + hod + '" WHERE dept_id='+ id
            mycursor.execute(update)
            print('Record Updated!!')

    if choice== 2:
        print("here is Student table:-")
        print("SID , name , dept")
        show = "select * from student"
        mycursor.execute(show)

        feild = input("which field u want to update:-")
        if feild == 'SID':
            name = input("enter name for which u update SID")
            SID = input("enter new SID:-")

            update='UPDATE student SET SID=' + SID + ' WHERE name="' + name + '"'


            mycursor.execute(update)
            print('Record Updated!!')



        if feild == 'name':
            SID = input("enter SID for which u update name")
            name = input("enter new name:-")


            update = 'UPDATE student SET name="' + name + '" WHERE SID=' + SID

            mycursor.execute(update)
            print('Record Updated!!')


        if feild == 'dept':
            SID = input("enter SID for which u update dept")
            dept = input("enter new dept name:-")

            update = 'UPDATE department SET dept="' + dept + '" WHERE SID=' + SID

            mycursor.execute(update)
            print('Record Updated!!')


