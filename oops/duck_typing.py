
class Pycharm:
    def execute(self):
        print("compile")
        print("run")


class Mycharm:
    def execute(self):
        print("Intellisense")
        print("suggestions")
        print("compile")
        print("run")

class Laptop:
    def code(self, ide):
        ide.execute()

ide = Mycharm()

lap1 = Laptop()
lap1.code(ide)