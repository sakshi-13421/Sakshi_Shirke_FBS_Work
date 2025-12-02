no =int(input("Enter a no = "))

print(f"Prime number upto {no} is")

for i in range(2,no):
    for j in range(2 , i):
      if(i % j == 0):
         break
    else:
       print(i, end=" ")