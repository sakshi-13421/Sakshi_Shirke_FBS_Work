total_amount = 0

age1= int(input("Enter age of person1 : "))
ticket1 = int(input("Enter ticket amount of person1 : "))
if(age1 < 12):
    ticket1  = ticket1 * 0.30
elif(age1 > 59):
    ticket1  = ticket1 * 0.50
total_amount += ticket1

age2= int(input("Enter age of person2 : "))
ticket2 = int(input("Enter ticket amount of person2 : "))
if(age2 < 12):
    ticket2  = ticket2 * 0.30
elif(age2 > 59):
    ticket2  = ticket2 * 0.50
total_amount += ticket2

age3= int(input("Enter age of person3 : "))
ticket3 = int(input("Enter ticket amount of person3 : "))
if(age3 < 12):
    ticket3  = ticket3 * 0.30
elif(age3 > 59):
    ticket3  = ticket3 * 0.50
total_amount += ticket3

age4= int(input("Enter age of person4 : "))
ticket4 = int(input("Enter ticket amount of person4 : "))
if(age4 < 12):
    ticket4  = ticket4 * 0.30
elif(age4 > 59):
    ticket4  = ticket4 * 0.50
total_amount += ticket4

age5= int(input("Enter age of person5 : "))
ticket5 = int(input("Enter ticket amount of person5 : "))
if(age5 < 12):
    ticket5  = ticket5 * 0.30
elif(age5 > 59):
    ticket5  = ticket5 * 0.50
total_amount += ticket5

print(f"Total amount for all 5 people = Rs.", total_amount)