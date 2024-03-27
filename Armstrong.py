print("Enter a number:")
sum=0
num=int(input())
temp=int(num)
count=0
while(temp!=0):
    temp = temp//10
    count=count+1
temp=int(num)
while(temp!=0):
    digit=(temp%10)
    sum=sum+digit**count
    temp=temp//10
if(sum==num):
    print("The number is Armstrong.")
else:
    print("The number is not Armstrong.")
