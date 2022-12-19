class A:
    def show(self):
        print("I am in class A show")

    def read(self):
        print("i am reading in class A")

class B(A):
    def run(self):
        print("I am running in class B")




a = A()
b = B()

b.show()