safeCounter = 0

def check__increasing_conditions(array):
    #print("CHECKING AGAIN", array)
    differences = [array[i+1] - array[i] for i in range(len(array) - 1)]
    #print("DIFF", differences)
    # Check if all differences are positive (decreasing trend)
    all_increasing = all(diff > 0 and (diff > 0 and diff <=3) for diff in differences)

    if (all_increasing):
        return True
    else:
        return False
    
def check__decreasing_conditions(array):
    differences = [array[i+1] - array[i] for i in range(len(array) - 1)]
    # Check if all differences are negative (increasing trend)
    all_decreasing = all(diff < 0 and (diff >= -3 and diff < 0) for diff in differences)

    if (all_decreasing):
        return True
    else:
        return False

def check_conditions(array):
    differences = [array[i+1] - array[i] for i in range(len(array) - 1)]
    arrayCopy = array
    arrayCopy2 = array
    isIncreasing = True
    deleteOneLevel = False
    isDecreasing = True
    diffCopy = differences

    #print("ARRAY",array)
    #print(differences)

    # Check if all differences are positive (decreasing trend)
    for eachIndex in range(len(differences)):
        if(differences[eachIndex] > 0 and (differences[eachIndex] >= 1 and differences[eachIndex] <=3)):
            continue
        else:
            if not deleteOneLevel:
                del arrayCopy[eachIndex]
                #print("COPY", arrayCopy)
                isIncreasing = check__increasing_conditions(arrayCopy)
                break

    for eachIndex in range(len(diffCopy)):
            if(diffCopy[eachIndex] < 0 and (diffCopy[eachIndex] >= -3 and diffCopy[eachIndex] <= -1)):
                continue
            else:
                if not deleteOneLevel:
                    del arrayCopy2[eachIndex]
                    #print("COPY2", arrayCopy2)
                    isDecreasing = check__decreasing_conditions(arrayCopy2)
                    break    

    
    #print(isDecreasing, isIncreasing)
    

    if (isDecreasing or isIncreasing):
        print(array)
        return 1
    else:
        return 0

    
with open("AdventOfCode2024\DayTwo\input2.txt", "r") as file1:
    lines = file1.readlines()
    array_2d = [list(map(int, line.split())) for line in lines]

    for eachRow in array_2d:
        safeCounter += check_conditions(eachRow)
    file1.close()

    print(safeCounter)

