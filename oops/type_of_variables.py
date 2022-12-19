class Car:
    wheel = 4

    def __init__(self, com = 'BMW', mil = 30):
        self.com = com
        self.mil = mil

c1 = Car('Hyudai', 25)
c1.wheel = 6
print(c1.com, c1.mil, c1.wheel)