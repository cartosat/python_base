


a=6
b=3


try:
    print("port is open")
    print(a/b)
    k = int(input("Enter value:-"))
    print(k)

except ZeroDivisionError as e:
    print(" division by zero error")

except ValueError as e:
    print("Invalid input")

except Exception as e:
    print("unknown error")

finally:
    print("port is closed")


