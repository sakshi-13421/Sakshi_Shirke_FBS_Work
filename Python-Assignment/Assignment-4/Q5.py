no = int(input("Enter a no : "))
a=-1
b=1
print("Fibonacii Series")
for i in range(no):
    c = a + b
    print(c, end = " ")
    a, b =  b, c