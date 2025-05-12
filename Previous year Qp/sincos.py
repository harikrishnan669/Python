import numpy as np
from matplotlib import pyplot as plt
from math import pi

x=np.linspace(0,2*np.pi,100)
y_sin=np.sin(x)
y_cos=np.cos(x)

plt.plot(x,y_sin,label='Sin(x)',color='Blue',linestyle='-')
plt.plot(x,y_cos,label='Cos(x)',color='Green',linestyle='--')

plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Sine and Cosine')

plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
           ['0', 'π/2', 'π', '3π/2', '2π'])

plt.yticks(np.arange(-1,-1.1,0.5))
plt.legend(loc='upper right')
plt.grid(True)
plt.show()