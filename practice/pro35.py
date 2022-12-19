


class computer:
    def __init__(self):
        self.name="Vaibhav"
        self.age=21
    def update(self):
        self.age=25

    def campare(self,other):
        if self.age==other.age:
            return True
        else:
            return False





c1=computer()
c2=computer()

c1.name="kiran"
c1.age=27

if c1.campare(c2):
    print("They are same")
else:
    print("Not same")



c1.update()

print(c1.name,c1.age)
print(c2.name,c2.age)