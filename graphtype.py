import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([1,4,9,16,25])
plt.subplot(2,2,1)
plt.plot(x,y)
plt.xlabel("x values")
plt.ylabel("square values")
plt.title("My graph")
plt.subplot(2,2,2)
plt.stem(x,y)
z=np.array([1,8,27,64,125])
plt.subplot(2,2,3)
plt.plot(x,z)
plt.ylabel("cube values")
plt.subplot(2,2,4)
plt.stem(x,z)