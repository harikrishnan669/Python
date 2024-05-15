# Hotel bill calculation

print("ZEENATH HOTEL")
print("MENU\n 1-porotta\n 2-chicken curry\n 3-chicken biriyani\n")
item=int(input("Enter the item number needed:"))
if item==1:
    print("Item is porotta of Rs 10")
    count=int(input("Enter the number of porotta needed:"))
elif item==2:
    print("Item is chicken curry of Rs 120")
    count=int(input("Enter the numbe rof chcoken curry needed:"))
elif item==3:
    print("Item is Biriyani of Rs 120")
    count=int(input("Enter the number of biriyani needed:"))
else:
    print("Invalid number")
    
if item==1:
    amount=count*10
    print("The amount for porotta is:" +str(amount))
elif item==2:
    amount=count*120
    print("The amount for chicken curry is:" +str(amount))
elif item==3:
    amount=count*120
    print("The amount for biriyani is:" + str(amount))
else:
    print("Invalid number")
    
