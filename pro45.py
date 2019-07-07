def itee():
    n=1

    while n<=10:
        sq=n*n
        n+=1
        yield sq


it=itee()
print(it.__next__())

for i in it:
    print(i)