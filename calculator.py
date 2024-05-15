print("CALCULATOR")
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
print(" 1-Addition\n 2-Subtraction\n 3-Multiplication\n 4-Divsion\n")
choice=int(input("Enter the choice value to perform the operation"))
if choice==1:
    sum=int(num1)+int(num2)
    print("The sum of two numbers is" + str(sum))
elif choice==2:
        sub=int(num1)-int(num2)
        print("The difference of two numbers is" + str(sub))
elif choice==3:
    multiply=int(num1)*int(num2)
    print("The product of two numbers is" + str(multiply))
elif choice==4:
    divide=int(num1)/int(num2)
    print("The quotient of two numbers is" + str(divide))
else:
    print("Invalid number")
