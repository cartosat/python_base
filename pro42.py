
class calcu:

    def __init__(self,r1,r2):

        self.m1  = r1
        self.m2 = r2

    def add(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s=a+b
        elif a!=None:
            s=a
        return s

sum=calcu(56,57)


print(sum.add(12,15))