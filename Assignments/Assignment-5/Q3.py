n = int(input("Enter number of passengers: "))
cost = float(input("Enter ticket cost: "))

total = 0

for i in range(n):
    age = int(input("Enter age of passenger: "))

    if (age < 12):
        price = cost * 0.7   
    elif (age > 59):
        price = cost * 0.5   
    else:
        price = cost       

    total += price

print("Total ticket cost =", total)
