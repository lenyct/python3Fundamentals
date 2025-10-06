total = 0
expenses = []

#1
# for i in range(7):
#     expenses.append(float(input("Enter expense: $")))

# total = sum(expenses)
# print("Total expenses: $", total, sep='')



#2 
for i in range(int(input("How many expenses do you have? \n"))):
    expenses.append(float(input("Enter expense: $")))
total = sum(expenses)
print("Total expenses: $", total, sep='')