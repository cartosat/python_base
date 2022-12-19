class Computer:
    def __init__(self):
        self.name = 'Navin'
        self.age = 28

    def update(self):
        self.age = 30


c1 = Computer()
c2 = Computer()
print(c1.name)
print(c1.age)
c1.update()
print(c1 == c2) # Comparing name value
print(c1.name is c2.name) # comparing memory address