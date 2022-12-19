
class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = "8GB"

        def show(self):
            print(self.brand, self.cpu, self.ram)



s1 = Student('Navin', 2)
s2 = Student('Jenny', 3)

print(s1.show())
print(s1.lap.brand)
lap1 = Student.Laptop()
print(lap1.show())
