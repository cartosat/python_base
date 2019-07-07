

def search(list,n):
    i=0
    if i<len(list):
        return True
    i+=1
    return False




list=[1,2,3,4,5,6,7,8,9,10]

n=int(input("Enter nu to search:-"))

if search(list,n):
    print("Found")
else:
    print("Not found")