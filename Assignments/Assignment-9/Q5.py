def SOF(no):
    if(no == 0):
        return 1
    else:
        return no * SOF(no - 1)

no=int(input("Enter a number : "))
res = SOF(no)
print(res)