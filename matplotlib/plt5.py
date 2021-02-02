import matplotlib.pyplot as plt
import numpy as np

#x = np.arange(0,10)
#plt.scatter(x,x**2)
#plt.show()


from random import sample
data = sample(range(1, 1000), 100)
print(len(data))
plt.hist(data)
plt.show()