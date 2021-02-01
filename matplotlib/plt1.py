import  matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x**2
print(x)
print(y)

#Functional method

#plt.plot(x,y)
#plt.xlabel('X label')
#plt.ylabel('Y label')
#plt.title('Title')
#plt.show()

#Creating subpolt on same canvas

#plt.subplot(1,2,1)
#plt.plot(x,y,'r')
#plt.subplot(1,2,2)
#plt.plot(y,x,'g')
#plt.show()

#Creating plots using object oriented methods

#fig = plt.figure()
#axes = fig.add_axes([0.1,0.1,0.8,0.8])
#axes.plot(x,y)

#plt.show()

#Creating 2 plots using OOP method

fig= plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])

axes1.plot(x,y)
axes1.set_title('LARGER PLOT')

axes2.plot(y,x)
axes2.set_title('SMALLER PLOT')

plt.show()