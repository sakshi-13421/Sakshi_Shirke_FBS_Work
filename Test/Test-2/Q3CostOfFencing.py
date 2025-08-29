length = 50
breadth = 40
radius = 20
strands = 5
cost_per_m = 35

perimeter = (2 * length + breadth) + (3.14 * radius)
total_length = perimeter * strands
total_cost = total_length * cost_per_m

if(perimeter > 0):
    print(f"One round fencing length : ", perimeter)
    print(f"Total wire length for 5 rounds : ", total_length)
    print(f"Total fencing cost : Rs", (total_cost))
else:
    print(f"Invalid data")