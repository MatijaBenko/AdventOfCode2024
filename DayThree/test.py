import re

def calculate(allMatches):
    result = 0
    for eachMatch in allMatches:
        result += int(eachMatch[0]) * int(eachMatch[1])
    return result

try:
    with open(r"AdventOfCode2024\DayThree\input.txt", "r", encoding="utf-8") as file1:
        lines = file1.read()
        #print("File content before processing:")
        #print(lines)  # Debugging: Check file content

        matches = re.findall(r'mul\((\d+),\s*(\d+)\)', lines)
        #print("Regex matches found:", matches)  # Debugging: Check matches

        result = calculate(matches)
        print(result)
except FileNotFoundError:
    print("The file was not found. Check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")