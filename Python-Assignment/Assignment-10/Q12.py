def create_number_square_cube_lists(lst):
    squares = []  
    cubes = []    

    for i in range(len(lst)):
        squares = squares + [lst[i] * lst[i]]        
        cubes = cubes + [lst[i] * lst[i] * lst[i]] 

    return lst, squares, cubes

numbers = [1, 2, 3, 4, 5]
numbers_list, squares_list, cubes_list = create_number_square_cube_lists(numbers)

print("Numbers List:", numbers_list)
print("Squares List:", squares_list)
print("Cubes List:", cubes_list)
