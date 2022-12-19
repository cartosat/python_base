import matplotlib.pyplot as plt
import seaborn as sns

x = ['sun', 'mon', 'fri', 'sat', 'tue', 'wed', 'thu']
y = [5, 6.7, 4, 6, 2, 4.9, 1.8]
ax = sns.stripplot(x, y);
ax.set(xlabel='Days', ylabel='Amount_spend')
plt.title('My first graph');

plt.show()