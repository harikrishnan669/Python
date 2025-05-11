import os

current_dir = os.getcwd()

items = os.listdir(current_dir)

print("Items in the current working directory:")
for item in items:
    print(item)
