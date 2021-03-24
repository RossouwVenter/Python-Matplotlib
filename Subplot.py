import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3]
y = [1,2,3]

fig = plt.figure()
fig.subtitle('Plot title')

#  can add more. the last one is where on the grid.
#  x by y and where the plot is.
plt.subplot(2,2,4)
plt.plot(x,y,color = 'orange')

plt.subplot(2,2,1)
plt.plot(x,y, color ='red')

plt.show()