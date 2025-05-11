# Familiarizing Numpy modules
import random
import numpy as np
from numpy.linalg import inv
from numpy import trace
from numpy.linalg import det

# Use a square matrix
a = np.array([[2, 4], [5, -6]])
print("Matrix a:")
print(a)

print("Transpose of a is:")
c = a.transpose()
print(c)

print("Inverse of a is:")
b = inv(a)
print(b)

# Calculate trace
t = trace(a)
print("Trace of a is:")
print(t)

d=det(a)
print("Determinant of a is:")
print(d)

x=np.random.randint(100,size=(5,5))
print(x)

y=np.random.choice([2,4,6,8,10])
print(y)

y=np.array([2,4,6,8,10])
np.random.shuffle(y)
np.random.permutation(y)
print(y)

matrix=np.random.randint(10,size=(3,3))
print("Marix is")
print(matrix)

A = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]
print("Marix is")
# Print the matrix
for row in A:
    print(row)