import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.axis('equal')
lang=['C','C++','java','python','PHP']
student=[10,25,36,42,15]
ax.pie(student,labels=lang,autopct='%1.2f%%')
plt.show()