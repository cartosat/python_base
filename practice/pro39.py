



class a:

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

class b:
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")


class c(a,b):

    def feature5(self):
        print("Feature 5 working")



v=c()

v.feature1()
v.feature2()
v.feature3()
v.feature4()
v.feature5()