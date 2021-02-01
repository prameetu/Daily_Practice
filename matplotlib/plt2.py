import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x**2
print(x)

#fig,axes = plt.subplots()
#axes.plot(x,y)
#plt.show()

fig,axes = plt.subplots(nrows=1,ncols=2)
#i=1
#for ax in axes:
#    ax.plot(x,y)
#   ax.set_title(f'Axes {i}')
#    i += 1

#plt.show()

#INdexing through axes list

#axes[0].plot(x,y)
#axes[1].plot(y,x)


