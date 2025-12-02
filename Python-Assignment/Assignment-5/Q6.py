beg = int(input("Enter a beginning range : "))
end = int(input("Enter a ending range : "))

print(f"Enter Prime Number {beg} to {end} is : ")

for no in range(beg, end + 1):
    if(no > 1):
        for i in range(2, no):
            if(no % i) == 0:
                break
        else:
            print(no)
