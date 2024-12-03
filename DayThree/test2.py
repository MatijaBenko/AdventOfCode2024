import re

fileContents = open("AdventOfCode2024\DayThree\input.txt")
arr = fileContents.read()

results = re.findall(
    r"do\(\)|don't\(\)|mul\([0123456789]{1,3},[01234567890]{1,3}\)", arr
)

print(results)

do_or_not = True
total = 0
for result in results:
    print(repr(result))
    if result.startswith("do("):
        do_or_not = True
    elif result.startswith("don"):
        do_or_not = False
    else:
        left, right = result[4:-1].split(",")
        if do_or_not:
            total += int(left) * int(right)

print(total)