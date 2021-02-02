import matplotlib.pyplot as plt
import numpy as np

#Assigning color ,linewidth,transperency to the plot
x = np.linspace(0,5,11)
y = x**2

fig = plt.figure()
ax = fig.add_axes([0.2,0.2,0.6,0.6])

#ax.plot(x,y,color='purple',linewidth=20,alpha=0.5)

#plt.show()

#Linestyle

#ax.plot(x,y,color= 'green',linestyle='dashdot')
#plt.show()

#Markers

#ax.plot(x,x**2,color = 'purple',lw=2,ls='--',marker='o')

#ax.plot(x,x**3,color = 'red',lw=2,ls='--',marker='+')
#ax.plot(x,x**4,color = 'green',lw=2,ls='--',marker='s')


#changing marker color
#ax.plot(x,x**3,color='green',marker='o',markerfacecolor='red',lw=2)

ax.plot(x,x**2,color='purple',lw=2,ls='--')
ax.set_xlim([0,1])
ax.set_ylim([0,1])

plt.show()