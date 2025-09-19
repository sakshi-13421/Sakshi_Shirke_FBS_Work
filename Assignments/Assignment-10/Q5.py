li = [10, 25, 7, 42, 18, 25, 42, 25]

num = int(input("Enter a number to check: "))

if num in li:
    count = li.count(num)
    print(f"{num} is present in the list {count} time(s).")
else:
    print(f"{num} is not present in the list.")
