def print_snakes_ladder():
    n = 10  
    num = 100  

    for i in range(n):
        row = []
        for j in range(n):
            row.append(num)
            num -= 1

        if i % 2 == 0:
            row.reverse()
        
        for x in row:
            print(f"{x:3}", end=" ")
        print()  

print_snakes_ladder()
