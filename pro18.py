
def person(name, **data):
    print(name)
    for i, j in data.items():
        print(i, j)

person('navin',age=28,city='mumbai',mob=976373)

