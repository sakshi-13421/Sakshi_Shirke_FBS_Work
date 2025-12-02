def SOS(no):
    if(no == 0):
        return 0
    else:
        return no + SOS(no - 1)

no=int(input("Enter a Number : "))
res = SOS(no)
print(res)