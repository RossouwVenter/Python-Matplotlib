import matplotlib.pyplot as plt


x1=[1,2,3,4,5]
y1 = [1,2,4,8,16]
y2 = [1,1,2,3,5]

plt.plot(x1, y1, 'g-s',label='students') 
plt.plot(x1, y2, 'r^-',label='teachers') 
plt.subplots_adjust(right= 0.7,bottom= 0.3)
plt.legend(loc = 'upper right')
plt.xlabel('Horisontal title')
plt.ylabel('Vertical title')
plt.title('My title')
plt.show()