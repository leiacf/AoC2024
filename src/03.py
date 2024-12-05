#Advent of Code 2024 Day 03

from tools import files
import time
import re

def test():

    input = [
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    ]

    return input

def parse(input, part2=False):

    total = 0
    matches = []
    do = True

    pattern = r"(mul)\((\d+),(\d+)\)"

    if part2:
        pattern = r"(mul)\((\d+),(\d+)\)|(do)\(\)|(don't)\(\)"

    for line in input:
        matches.extend(re.findall(pattern, line))

    for match in matches:

        if part2:
            if match[3] == "do":
                do = True
            elif match[4] == "don't":
                do = False

        if match[0] == "mul" and do:
            total += int(match[1]) * int(match[2])

    return total

def part1(input):

    total = parse(input, False)
    print("Part 1: The sum of all muls is", total)

def part2(input):

    total = parse(input, True)
    print("Part 2: The total number of muls is", total)

filename = "../input/03.txt"
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
print("Spent {:>7.3f} seconds on Part 1".format(end1-start1))
print("Spent {:>7.3f} seconds on Part 2".format(end2-start2))