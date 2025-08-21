m1=int(input("Enter marks of subject 1="))
m2=int(input("Enter marks of subject 2="))
m3=int(input("Enter marks of subject 3="))
m4=int(input("Enter marks of subject 4="))
m5=int(input("Enter marks of subject 5="))

Gain_marks = m1 + m2 + m3 + m4 + m5

Perc = (Gain_marks/500) * 100

print(f"Percentage of 5 subject is {Perc}%")
