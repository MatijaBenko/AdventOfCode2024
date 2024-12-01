
firstList = []
secondList = []
totalDis = 0
with open("./adventOfCode2024/AdventOfCode2024/DayOne/input.txt", "r") as file1:
    for eachLine in file1.readlines():
        nums = eachLine.split()
        firstList.append(int(nums[0]))
        secondList.append(int(nums[1]))
    firstList.sort()
    secondList.sort()
    for firstNum, secondNum in zip(firstList,secondList):
        result = abs(firstNum - secondNum)
        totalDis += result
    print(totalDis)
    file1.close()