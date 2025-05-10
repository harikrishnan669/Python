numbers = [5, -3, 0, 9, -12, 4, -7, 8]

positive_numbers = []
negative_numbers = []

for num in numbers:
    if num >= 0:
        positive_numbers.append(num)
    else:
        negative_numbers.append(num)

print("Positive numbers:", positive_numbers)
print("Negative numbers:", negative_numbers)
