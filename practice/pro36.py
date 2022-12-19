

class car:

    wheels=4
    com="BMW"
    mil=12

    def __init__(self):
        self.com="BMW"
        self.mil=12

    def faci(self):

        print("car has audio tape")




c1=car()
c2=car()

car.wheels=5

print(c1.com,c1.mil,c1.wheels,c1.faci())
print(c2.com,c2.mil,car.wheels)