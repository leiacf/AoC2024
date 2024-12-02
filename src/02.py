#Advent of Code 2024 Day 02

from tools import files
import time
import copy

def test():

    input = [

        "7 6 4 2 1",
        "1 2 7 8 9",
        "9 7 6 2 1",
        "1 3 2 4 5",
        "8 6 4 4 1",
        "1 3 6 7 9"

    ]

    return input

def parse(input):

    reports = []

    for line in input:
        levels = line.split()

        intlevels = []

        for level in levels:
            level = int(level)
            intlevels.append(level)

        reports.append(intlevels)

    return reports

def increasing(levels):

    for x in range(1, len(levels)):
        if levels[x-1] >= levels[x]:
            return False
        
    return True

def decreasing(levels):

    for x in range(1, len(levels)):
        if levels[x-1] <= levels[x]:
            return False
        
    return True

def numbers(levels):

    for x in range(1, len(levels)):

        if abs(levels[x-1] - levels[x]) == 1 or abs(levels[x-1] - levels[x]) == 2 or abs(levels[x-1] - levels[x]) == 3:
           continue
        else:
            return False
        
    return True

def check(reports):

    safe = 0

    for levels in reports:

        if increasing(levels):
            if numbers(levels):
                safe += 1

        elif decreasing(levels):
            if numbers(levels):
                safe += 1

    return safe

def damp_increasing(levels):

    safe = 0

    if increasing(levels):
        if numbers(levels):
            safe +=1
        
        else:
            for x in range(0, len(levels)):

                temp = copy.deepcopy(levels)
                del temp[x]

                if numbers(temp):
                    safe += 1
                    break

    else:
        for x in range(0, len(levels)):
        
            temp = copy.deepcopy(levels)
            del temp[x]

            if increasing(temp):
                if numbers(temp):
                    safe +=1
                    break

    return safe

def damp_decreasing(levels):
    
    safe = 0

    if decreasing(levels):
        if numbers(levels):
            safe +=1
        
        else:
            for x in range(0, len(levels)):

                temp = copy.deepcopy(levels)
                del temp[x]
                
                if numbers(temp):
                    safe += 1
                    break

    else:
        for x in range(0, len(levels)):
        
            temp = copy.deepcopy(levels)
            del temp[x]

            if decreasing(temp):
                if numbers(temp):
                    safe +=1
                    break

    return safe

def check_damp(reports):

    safe = 0

    for levels in reports:

        safe += damp_increasing(levels)
        safe += damp_decreasing(levels)

    return safe

def part1(input):

    reports = parse(input)

    safe = check(reports)

    print("Part 1: The amount of safe resports are", safe)

def part2(input):

    reports = parse(input)

    safe = check_damp(reports)

    print("Part 2: The amount of safe reports are", safe)

filename = "../input/02.txt"
input = files.input_as_list(filename)
#input = test()

print()

start1 = time.perf_counter()
part1(input)
end1 = time.perf_counter()

start2 = time.perf_counter()
part2(input)
end2 = time.perf_counter()

print()
print("Spent {:>7.2f} seconds on Part 1".format(end1-start1))
print("Spent {:>7.2f} seconds on Part 2".format(end2-start2))