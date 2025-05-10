people={'Hari':'20','Kichu':'18','Ram':'16'}

name=input('Enter your name: ')

if name in people:
    print(f"{name} age is {people[name]}")
else:
    print(f"{name} age is not available")

