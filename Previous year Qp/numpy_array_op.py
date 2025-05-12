import numpy as np

arr1=np.random.randint(0,20,size=(3,3))
arr2=np.random.randint(0,20,size=(3,3))

addition=arr1+arr2
print("The addition of two array is",addition)

mean_arr1=np.mean(arr1)
print("The mean of first array is",mean_arr1)

std_arr1=np.std(arr1)
print("The standard deviation of first array is",std_arr1)

multiply_scalarvalue=arr1*5
print("The scalar multiplication of first array is",multiply_scalarvalue)

dot_product=arr1.dot(arr2)
print("The dot product of two array id",dot_product)