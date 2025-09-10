def Fibonaci(no):
    a = -1
    b = 1
    for i in range(no):
        c = a + b
        print(c, end = " ")
        a, b = b, c

no = int(input("Enter a no : "))
Fibonaci(no)
