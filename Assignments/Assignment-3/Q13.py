charges=float(input("Enter electricity unit charges : "))

if(charges <= 50):
    total_bill = charges * 0.50
elif(charges <= 150):
    total_bill = 50 * 0.50 + (charges - 50) * 0.75
elif(charges <= 250):
    total_bill = 50 * 0.50 + 100 * 0.75 + (charges - 150) * 1.20
else:
    total_bill = 50 * 0.50 + 100 * 0.75 + 100 * 1.20 + (charges - 250) * 1.50

surcharge= total_bill * 0.20
total= total_bill + surcharge
print(f"Total electricity bill: {total}")
