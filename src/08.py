#Advent of Code 2024 Day 08

from tools import files
from itertools import combinations
import time

def test():

    input = [

        "............",
        "........0...",
        ".....0......",
        ".......0....",
        "....0.......",
        "......A.....",
        "............",
        "............",
        "........A...",
        ".........A..",
        "............",
        "............"

    ]

    return input

def parse(input):

    locations = {}

    for row, line in enumerate(input):
        for col, letter in enumerate(line):
            if letter != ".":
                if letter in locations:
                    locations[letter].extend([(row, col)])
                else:
                    locations[letter] = [(row, col)]

    return locations

def bounds(location, input):

    if location[0] < 0 or location[0] >= len(input):
        return False
    
    if location[1] < 0 or location[1] >= len(input[0]):
        return False
    
    return True

def anti(locations, input):

    antinodes = []

    for _, location in locations.items():
        pairs = list(combinations(location, 2))

        for pair in pairs:

            y = (pair[0][0]-pair[1][0])
            x = (pair[0][1]-pair[1][1])

            one =   (pair[0][0] - y , pair[0][1] - x)
            two =   (pair[0][0] + y , pair[0][1] + x)
            three = (pair[1][0] - y , pair[1][1] - x)
            four =  (pair[1][0] + y , pair[1][1] + x)

            if bounds(one, input) and one not in pair and one not in antinodes:
                antinodes.append(one)
            if bounds(two, input) and two not in pair and two not in antinodes:
                antinodes.append(two)
            if bounds(three, input) and three not in pair and three not in antinodes:
                antinodes.append(three)
            if bounds(four, input) and four not in pair and four not in antinodes:
                antinodes.append(four)

    return antinodes

def antires(locations, input):

    antinodes = []

    for _, location in locations.items():

        pairs = list(combinations(location, 2))

        for pair in pairs:
            
            y = pair[0][0] - pair[1][0]
            x = pair[0][1] - pair[1][1]

            one =   (pair[0][0] - y , pair[0][1] - x)
            two =   (pair[0][0] + y , pair[0][1] + x)
            three = (pair[1][0] - y , pair[1][1] - x)
            four =  (pair[1][0] + y , pair[1][1] + x)

            while bounds(one, input):
                if one not in antinodes:
                    antinodes.append(one)
                one = (one[0] - y, one[1] - x)

            while bounds(two, input):
                if two not in antinodes:
                    antinodes.append(two)
                two = (two[0] + y, two[1] + x)

            while bounds(three, input):
                if three not in antinodes:
                    antinodes.append(three)
                three = (three[0] - y, three[1] - x)

            while bounds(four, input):
                if four not in antinodes:
                    antinodes.append(four)
                four = (four[0] + y, four[1] + x)

    return antinodes

def part1(input):

    locations = parse(input)
    antinodes = anti(locations, input)

    print("Part 1: The number of antinodes is", len(antinodes))

def part2(input):

    locations = parse(input)
    antinodes = antires(locations, input)

    print("Part 2: The numner of antinodes is", len(antinodes))

filename = "../input/08.txt"
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