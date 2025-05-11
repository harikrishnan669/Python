number = int(input("Enter a 5 didgit number"))
o=number
s=0
while number>0:
  d=number%10
  s=s*10+d
  number=number//10
print("The reversed number is", s)
if(s==o):
  print("Palindrome")
else:
  print("Not palindrome")
