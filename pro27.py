
import sys
print(sys.getrecursionlimit())

i=0
def greet():
    global i
    i+=1
    print("Hellooo!!",i)
    greet()


greet()