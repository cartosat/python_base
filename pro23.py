

i=int(input("Enter number:-"))
k=(2,3,5,7)
while i==1:
    print("Prime")
    break
for j in k:

    if i%j==0:
        print("Number is not prime")
        break
else:
    print("number is prime")
