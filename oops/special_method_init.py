class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is :-", self.cpu, self.ram)

acer = Computer('i5', '16GB')

acer.config()
