no=int(input("Enter a no="))

no1 = no % 10
no2 = (no // 10) % 10
no3 = (no // 100)

reverse_no=(no1 * 100) + (no2 * 10)  + no3

print(f"Reverse no is {reverse_no}")