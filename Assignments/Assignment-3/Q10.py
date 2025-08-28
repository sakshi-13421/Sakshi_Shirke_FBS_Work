gender=(input("Enter gender (M/F) : "))
age=int(input("Enter a age : "))

if(gender == 'M'):
    if(age >= 23):
        print(f'Eligible for Marriage')
    else:
        print(f'Not Eligible for Marriage')
else:
    if(age > 17):
        print(f'Eligible for Marriage')
    else:
        print(f'Not Eligible for Marriage')