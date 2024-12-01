
firstList = []
secondList = []
totalSim = 0
with open("./adventOfCode2024/AdventOfCode2024/DayOne/input2.txt", "r") as file1:
    for eachLine in file1.readlines():
        nums = eachLine.split()
        firstList.append(int(nums[0]))
        secondList.append(int(nums[1]))
    for eachNum in firstList:
        result = eachNum * secondList.count(eachNum)
        totalSim += result
    print(totalSim)
    file1.close()