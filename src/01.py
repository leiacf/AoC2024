#Advent of Code 2024 Day 01

from tools import files
import time

def test():

    input = [

        "3   4",
        "4   3",
        "2   5",
        "1   3",
        "3   9",
        "3   3"

    ]

    return input

def parse(input):

    l1 = []
    l2 = []

    for line in input:

        num1, num2 = line.split()
        l1.append(int(num1))
        l2.append(int(num2))

    l1.sort()
    l2.sort()

    return l1, l2

def calculate(l1, l2):

    total = 0

    for x in range(0, len(l1)):
        total += abs(l1[x] - l2[x])
    
    return total

def similarity(l1, l2):

    total = 0

    for number in l1:

        times = 0        

        for other in l2:

            if number == other:
                times +=1

        total += (number*times)

    return total

def part1(input):

    l1, l2 = parse(input)

    total = calculate(l1, l2)

    print("Part 1: The total distance is", total)


def part2(input):

    l1, l2 = parse(input)

    total = similarity(l1, l2)

    print("Part 2: The similarity score is", total)

filename = "../input/01.txt"
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