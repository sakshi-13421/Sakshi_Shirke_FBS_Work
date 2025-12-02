no = int(input("enter a no :"))
sum=0
for i in range(1,no):
    if(no%i==0):
        sum=sum+i
if(sum==no):
    print(f"{no} is a perfect number.")
else:
    print(f"{no} is a not perfect number.")