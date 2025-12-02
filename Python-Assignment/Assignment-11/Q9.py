def create_numbers_squares_cubes(numbers):
    squares = []  
    cubes = []   

    for i in range(len(numbers)):
        squares = squares + [numbers[i] * numbers[i]]        
        cubes = cubes + [numbers[i] * numbers[i] * numbers[i]]  

    return numbers, squares, cubes


numbers = [1, 2, 3, 4, 5]
nums, squares, cubes = create_numbers_squares_cubes(numbers)

print("Numbers List:", nums)
print("Squares List:", squares)
print("Cubes List:", cubes)
