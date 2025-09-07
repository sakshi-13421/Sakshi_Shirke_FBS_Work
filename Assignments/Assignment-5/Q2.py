n = int(input("Enter number of students: "))

total_percentage = 0

for i in range(1, n+1):
    marks = 0
    print(f"\nEnter marks of 5 subjects for student {i}:")
    for j in range(5):
        marks += int(input(f"Subject {j+1}: "))
    
    percent = marks / 5
    print(f"Percentage of student {i} = {percent}")
    total_percentage += percent

avg = total_percentage / n
print("\nAverage percentage of all students =", avg)
