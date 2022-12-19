


class Student:

    school="Z.P.P"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):
        return self.m1
    def set_m1(self,value):
        self.m1=value
    @classmethod
    def info(cls):
        return cls.school



s1=Student(65,84,74)
s2=Student(52,55,98)
s1.set_m1(75)


print(s2.avg())
print(s1.m1)
print(s1.get_m1())
print(s1.info())
print(Student.info())
