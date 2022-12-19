

def calc():
    a=int(input("Enter a:-"))
    b = int(input("Enter b:-"))
    print("what operation:-\n1.Add\n2.Sub\n3.Mul\n4.Div")
    ch=int(input())

    if ch==1:
        c=a+b
        print(c)
    elif ch==2:
        c = a - b
        print(c)
    elif ch==3:
        c = a * b
        print(c)
    elif ch==4:
        c = a / b
        print(c)

calc()