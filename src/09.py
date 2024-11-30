#Advent of Code 2024 Day 09

from tools import files
import time

def test():

    input = [

    ]

    return input

def part1(input):

    print("Part 1: ")

def part2(input):

    print("Part 2: ")

filename = "../input/09.txt"
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