
class Student:
    school = 'Telusko'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def average(self):
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def get_school(cls):
        return cls.school

    @staticmethod
    def info():
        print("this is Student class.")


s1 = Student(44, 45, 46)
s2 = Student(35, 66, 87)

print(s2.average())
print(Student.get_school())
print(Student.info())