#Advent of Code 2024 Day 02

from tools import files
from tools import parsing
import time

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

    reports = parsing.strings_to_ints(input)

    return reports

def is_safe(levels):

    pairs = list(zip(levels, levels[1:]))

    increasing = all(a < b for a, b in pairs)
    decreasing = all(a > b for a, b in pairs)

    if not (increasing or decreasing):
        return False
    
    if any(abs(a-b) > 3 for a, b in pairs):
        return False
    
    return True

def is_safe_damp(levels):

        if is_safe(levels):
             return True

        for x in range(len(levels)):
            damp = levels[:x] + levels[x+1:]
            if is_safe(damp):
                return True
                
        return False
    
def check(reports):

    safe = 0

    for levels in reports:

        if is_safe(levels):
            safe += 1

    return safe

def check_damp(reports):

    safe = 0

    for levels in reports:

        if is_safe_damp(levels):
            safe += 1

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