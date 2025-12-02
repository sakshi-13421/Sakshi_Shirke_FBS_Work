def check_element(lst, num):
    count = 0
    for i in lst:
        if i == num:
            count += 1

    if count > 0:
        print(num, "is present in the list.")
        print("It occurs", count, "time(s).")
    else:
        print(num, "is not present in the list.")
        
numbers = [2, 5, 7, 5, 9, 5, 1]
n = int(input("Enter a number to search: "))
check_element(numbers, n)
