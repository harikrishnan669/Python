#Write a Python program to find out the eldest and youngest of three individuals, with their ages being input through the keyboard (without using max and min functions)
person1=int(input("Enter the age of the first person"))
person2=int(input("Enter the age of the second person"))
person3=int(input("Enter the age of the third person"))

eldest=person1
youngest=person1

if person2>eldest:
    eldest=person2
if person3>eldest:
    eldest=person3

if person2>youngest:
    eldest=person2
if person3>youngest:
    eldest=person3

print("The eldest age is",eldest)
print("The youngest age is",youngest)