no = int(input("Enter number"))

d1 = no % 10
no = no // 10

d2 = no % 10
no = no // 10

d3 = no % 10
no = no // 10

print(f'd1:{d1}, d2:{d2}, d3:{d3}')

print(f"sum of digit is {d1 + d2 + d3}")