limit=int(input("Enter the limit value: "))
odd_count=0
even_count=0

for i in range(limit):
    if i%2==0:
        even_count=even_count+1
        print("Even numbers are",i)
    else:
        odd_count=odd_count+1
        print("Odd numbers are",i)

print(odd_count)
print(even_count)