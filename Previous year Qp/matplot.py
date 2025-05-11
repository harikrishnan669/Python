from matplotlib import pyplot as plt
from math import pi
import numpy as np

x=np.arange(0,pi*2,0.05)
y=np.sin(x)
plt.plot(x,y)
plt.xlabel("Angle")
plt.ylabel("Sin(x)")
plt.title("Sine wave")
plt.show()

