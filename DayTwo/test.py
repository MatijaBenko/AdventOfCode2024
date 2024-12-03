safeCounter = 0

def check_conditions(array):
    differences = [array[i+1] - array[i] for i in range(len(array) - 1)]

    # Check if all differences are positive (decreasing trend)
    all_increasing = all(diff > 0 and (diff >= 0 and diff <=3) for diff in differences)

    # Check if all differences are negative (increasing trend)
    all_decreasing = all(diff < 0 and (diff >= -3 and diff <=0) for diff in differences)

    if (all_decreasing or all_increasing):
        return 1
    else:
        return 0

    
with open("AdventOfCode2024\DayTwo\input.txt", "r") as file1:
    lines = file1.readlines()
    array_2d = [list(map(int, line.split())) for line in lines]

    for eachRow in array_2d:
        safeCounter += check_conditions(eachRow)
    file1.close()

    print(safeCounter)

