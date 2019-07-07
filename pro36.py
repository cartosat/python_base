

class car:

    wheels=4

    def __init__(self):
        self.com="BMW"
        self.mil=12


c1=car()
c2=car()

car.wheels=5

print(c1.com,c1.mil,c1.wheels)
print(c2.com,c2.mil,car.wheels)