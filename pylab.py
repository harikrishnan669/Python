import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, np.pi * 2, 0.05)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.plot(x, -np.sin(x))
plt.plot(x,-np.cos(x))
plt.xlabel('X axis')
plt.ylabel('Y axix')
plt.title('Simple plot')
plt.show()
