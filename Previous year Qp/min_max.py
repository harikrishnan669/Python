def min_max(numbers):
    smallest=min(numbers)
    largest=max(numbers)
    return smallest,largest

nums=[1,2,3,4,5,6,7,8,9,10]
min_nums,max_nums=min_max(nums)
print("Largest number",max_nums)
print("Smallest number",min_nums)