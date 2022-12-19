import math,random

def otp():
    digit="0123456789"
    OTP=""
    for i in range(6):
        OTP+=digit[math.floor(random.random()* 10)]

    return OTP

OTP=otp()
print("OTP is:-",OTP)

otp=input("enter OTP:-")
if otp==OTP:
    print("Succesful!!")
else:
    print("Wrong OTP")

