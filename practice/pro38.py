


class stud:

    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        self.lap=self.laptop()

    def show(self):
        print(self.name,self.roll)
        self.lap.show()

    class laptop:
        def __init__(self):
            self.brand='HP'
            self.cpu='i5'
            self.ram='2'

        def show(self):
            print(self.brand,self.cpu,self.ram)


s=stud('vaibhav',22)

s.show()