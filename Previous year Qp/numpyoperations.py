import numpy as np
from numpy.ma.core import transpose

A=np.random.randint(0,21,size=(3,3))
B=np.random.randint(0,21,size=(3,3))

matrix_addition=A+B

matrix_multiplication=A.dot(B)

matrix_transpose=transpose(matrix_multiplication)

print("The matrix A is",A)
print("The matrix B is",B)
print("The matrix matrix_addition is",matrix_addition)
print("The matrix multiplication is",matrix_multiplication)
print("The transpose of matrix multiplication is",matrix_transpose)