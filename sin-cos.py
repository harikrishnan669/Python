import matplotlib.pyplot as plt
from numpy import linspace,sin,pi,cos
x=linspace(0,4*pi,40)
y=sin(x)
z=cos(x)

plt.stem(x,y,linefmt='g',markerfmt='rd')
plt.plot(x,y)

plt.plot(x,z)
plt.stem(x,z,linefmt='c',markerfmt='rd')

figure,axis=plt.subplots(2,1)

axis[0].plot(x,y)
axis[0].set_title("Sine function")

axis[1].plot(x,z)
axis[1].set_title("Cosine function")
plt.show
