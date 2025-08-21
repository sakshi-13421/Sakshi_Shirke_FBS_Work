P=int(input("Enter a principle amount = "))
R=int(input("Enter a rate of interst = "))
T=int(input("Enter a time(year) = "))

CI = P * (1+R/100)**T - P

print(f"Compund Interest is {CI}")



