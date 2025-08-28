basic = int(input("Enter basic salary="))

da = 0.10 * basic
ta = 0.12 * basic
hra = 0.15 * basic

Total_Salary = basic + da + ta + hra

print(f"DA is = {da}")
print(f"TA is = {ta}")
print(f"HRA is = {hra}")
print(f"Total Salary of Employee is = {Total_Salary}")
