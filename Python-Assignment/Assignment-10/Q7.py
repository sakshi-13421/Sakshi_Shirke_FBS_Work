def cube_list(lst):
    cubes = [] 
    for i in range(len(lst)):
        cube = lst[i] * lst[i] * lst[i]  
        cubes = cubes + [cube]  
    return cubes


numbers = [1, 2, 3, 4, 5]
print("Original List:", numbers)
print("Cube List:", cube_list(numbers))
