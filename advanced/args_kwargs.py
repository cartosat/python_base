

def summ(a, b, *prg):
    print(a+b)
    print(prg)
    print(type(prg))
    for i in prg:
        print(i)

summ(1,2,3, 4,5)

print("===========================")
def summ_(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, ":", value)

summ_(a=5,b=6,d=7)
