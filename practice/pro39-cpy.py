

class a:

    def fea1(self):
        print('f1 here')

    def fea2(self):
        print('f2 here')

class b:

    def fea3(self):
        print('f3 here')

    def fea4(self):
        print('f4 here')

class c(a,b):

    def fea5(self):
        print('f5 here')




f=c()

f.fea5()
f.fea1()
