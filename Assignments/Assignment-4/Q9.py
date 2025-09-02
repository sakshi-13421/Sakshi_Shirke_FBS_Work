start=int(input("Enter a starting range : "))
end=int(input("Enter a ending range : "))
divisor=int(input("Enter a divisor no : "))

for i in range(start, end + 1):
    if(i % divisor == 0):
        print(i, end = " ")
