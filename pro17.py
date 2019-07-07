


def update():
    name='vaibhav'
    age=21
    designation='programmer'

    print(name)
    print(age)
    print(designation)
    print("\nwhat u want to update:-\n1.name \n2.age\n3.designation")
    key=int(input())

    if key==1:
        print("Enter new name:-")
        name=input()

    elif key==2:
        print("Enter new age:-")
        age=input()

    elif key==3:
        print("Enter new designation:-")
        designation=input()

    print("updated data is:-")
    print(name)
    print(age)
    print(designation)


update()