#Advent of Code 2024 Day 11

from tools import files
from tools import parsing
import time

cache = {}

def test():

    input = [

        #"0 1 10 99 999"
        "125 17"

    ]

    return input

def parse(input):

    stones = parsing.strings_to_ints(input)

    return stones[0]

def blink(stone, blinks):

    if (blinks == 0):
        return 1

    if (stone, blinks) in cache:
        return cache[(stone, blinks)]
    
    if (stone == 0):
        amount = blink(1, blinks-1)

    elif(len(str(stone))) % 2 == 0:
        string = str(stone)
        cut = len(string) // 2
        one = int(string[:cut])
        two = int(string[cut:])  

        amount = blink(one, blinks-1) + blink(two, blinks-1)

    else:
        amount = blink(stone*2024, blinks-1)

    cache[(stone, blinks)] = amount

    return amount

def part1(input):

    stones = parse(input)
    amount = 0

    for stone in stones:
        amount += blink(stone, 25)

    print("Part 1: My stone collection is", amount)

def part2(input):

    stones = parse(input)
    amount = 0

    for stone in stones:
        amount += blink(stone, 75)

    print("Part 2: My stone collection is", amount)

filename = "../input/11.txt"
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