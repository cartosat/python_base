import matplotlib.pyplot as plt
import math
import numpy as np

x=np.arange(0,math.pi*2,0.05)
y=np.sin(x)
plt.xlabel("Angle")
plt.ylabel("Sine")
plt.title("Sine Graph")
plt.plot(x,y)
plt.show()