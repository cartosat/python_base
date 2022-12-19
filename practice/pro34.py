

class computer:

    def __init__(self,RAM,CPU):
        self.RAM=RAM
        self.CPU=CPU


    def config(self):
        print("Config is:-",self.RAM,"GB",self.CPU)


comp1=computer(8,'RYZEN')
comp2=computer(16,'AMD')


comp1.config()
comp2.config()