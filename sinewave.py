from matplotlib import pyplot as plt
import numpy as np
x=np.arange(0,np.pi*2,0.05)
y=np.sin(x)
plt.plot(x,y)
plt.xlabel('Angle')
plt.ylabel('Sine')
plt.title('Sine wave')
plt.show()