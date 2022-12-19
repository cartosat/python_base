name = input("enter name for which u update SID")
SID = input("enter new SID:-")

update = 'UPDATE student SET SID=' + SID + ' WHERE name="' + name + '"'
print('Record Updated!!')
print(update)