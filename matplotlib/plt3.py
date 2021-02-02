import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x**2

#changing figure size
#fig = plt.figure(figsize=(3,2))

#axes = fig.add_axes([0.15,0.15,1,1])

#axes.plot(x,y)
#plt.tight_layout()
#plt.show()

#fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(8,2))

#axes[0].plot(x,y)
#axes[1].plot(y,x)

#plt.show()

#saving a figure

#fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(8,2))

#axes[0].plot(x,y)
#axes[1].plot(y,x)

#fig.savefig('mypc.png',dpi=200 )
#plt.show()


#Using legends i.e label text in the plotting

fig = plt.figure()

axes = fig.add_axes([0.2,0.2,0.6,0.6])

axes.plot(x,x**2,label="X**2")
axes.plot(x,x**3,label="X**3")
axes.legend(loc=0)

plt.show()
