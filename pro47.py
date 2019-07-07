from threading import *
from time import *

class hello(Thread):
    def run(self):
        for i in range(5):
            print("Helllllo")
            sleep(1)

class hi(Thread):
     def run(self):
         for i in range(5):
            print("hiiii")
            sleep(1)

a1=hello()
a2=hi()

a1.start()
sleep(0.4)
a2.start()

a1.join()
a2.join()

print("Byee")

