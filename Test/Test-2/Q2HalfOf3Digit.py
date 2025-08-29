no=float(input("Enter a no : "))

first = no // 100
second =(no // 10) % 10
third= no % 10

if(first == 2 * second and first == third / 2):
    print("You have done it")
else:
    print("Please try next time")