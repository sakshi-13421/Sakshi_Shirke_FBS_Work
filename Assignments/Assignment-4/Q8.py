beg = int(input("Enter a beginning range : "))
end = int(input("Enter a ending range : "))
for no in range(beg, end, + 1):
    if(no % 7 == 0 and no % 5 == 0):
        print(no)
