ticket = float(input("Enter ticket amount per person: "))

# Accept ages of 5 people
age1 = int(input("Enter age of person 1: "))
age2 = int(input("Enter age of person 2: "))
age3 = int(input("Enter age of person 3: "))
age4 = int(input("Enter age of person 4: "))
age5 = int(input("Enter age of person 5: "))

# Person 1 fare
if age1 < 12:
    fare1 = ticket * 0.70
elif age1 > 59:
    fare1 = ticket * 0.50
else:
    fare1 = ticket

# Person 2 fare
if age2 < 12:
    fare2 = ticket * 0.70
elif age2 > 59:
    fare2 = ticket * 0.50
else:
    fare2 = ticket

# Person 3 fare
if age3 < 12:
    fare3 = ticket * 0.70
elif age3 > 59:
    fare3 = ticket * 0.50
else:
    fare3 = ticket

# Person 4 fare
if age4 < 12:
    fare4 = ticket * 0.70
elif age4 > 59:
    fare4 = ticket * 0.50
else:
    fare4 = ticket

# Person 5 fare
if age5 < 12:
    fare5 = ticket * 0.70
elif age5 > 59:
    fare5 = ticket * 0.50
else:
    fare5 = ticket

# Total amount
total = fare1 + fare2 + fare3 + fare4 + fare5
print("Total amount to travel for all five persons:", total)