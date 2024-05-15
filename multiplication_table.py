# Multiplication Table program

table=int(input("Enter the value for the multiplication table to be found: "))
limit=int(input("Enter the limit up to which the table need to be calculated:"))
for i in range(1,limit+1) :
    multiply=table*i
    print("The tables are\n" + str(table) + "x" + str(i) + "=" + str(multiply))
