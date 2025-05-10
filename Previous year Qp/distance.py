from math import sqrt

x1=int(input("Enter the value for x1:"))
x2=int(input("Enter the value for x2:"))
y1=int(input("Enter the value for y1:"))
y2=int(input("Enter the value for y2:"))

x=(x2-x1)**2
y=(y2-y1)**2

distance=sqrt(x+y)
print("The distance is",distance)