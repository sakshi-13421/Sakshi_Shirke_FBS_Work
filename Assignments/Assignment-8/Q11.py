def count_digits(num):
    count = 0
    while(num != 0):
        num=num//10
        count += 1
    return count

def armstrong_sum(num, count):
    sum = 0
    while(num != 0):
        rem = num % 10
        sum = sum + (rem ** count)
        num = num // 10
    return sum

def is_armstrong(num):
    count = count_digits(num)
    sum = armstrong_sum(num, count)

    if(sum == num):
        print(num, "is an Armstrong number.")
    else:
      print(num, "is not an Armstrong number.")

num = int(input("Enter a number: "))    

is_armstrong(num)