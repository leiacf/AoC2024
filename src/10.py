#Advent of Code 2024 Day 10

from tools import files
from tools import node
from tools import grid
import time

def test():

    input = [

        "10..9..",
        "2...8..",
        "3...7..",
        "4567654",
        "...8..3",
        "...9..2",
        ".....01"

    ]

    return input

def parse(input):

    mountain = {}
    size = len(input)

    for ver, line in enumerate(input):
        for hor, number in enumerate(line):
            if number != ".":
                number = int(number)
            position = node.Node(number, ver, hor)
            mountain[(ver, hor)] = position

    for _, position in mountain.items():
        
        nodes = []
        ver, hor = position.get_point()

        neighbours = grid.neighbours(ver, hor, size)

        for neighbour in neighbours:
            if neighbour in mountain:
                nodes.append(mountain[neighbour])

        position.set_neighbours(nodes)

    return mountain

def heads(mountain):

    heads = []

    for _, position in mountain.items():
        if position.get_value() == 0:
            heads.append(position)

    return heads

def flush(mountain):

    for _, position in mountain.items():
        position.set_visited(False)

def show(position):

    print()
    print(position)

    for neighbour in position.get_neighbours():
        print(neighbour.get_point())

    print()

def recursive_part1(current, path, paths):

        if current.get_visited() == True:
            paths.append(path)
            return

        path += str(current.get_value())

        if current.get_value() == 9:
            current.set_visited(True)
            paths.append(path)

        else:

            for neighbour in current.get_neighbours():

                if neighbour.get_value() != ".":

                    if neighbour.get_value() - current.get_value() == 1:
                        recursive_part1(neighbour, path, paths)

def recursive_part2(current, path, paths):

        path += str(current.get_value())

        if current.get_value() == 9:
            paths.append(path)

        else:

            for neighbour in current.get_neighbours():

                if neighbour.get_value() != ".":

                    if neighbour.get_value() - current.get_value() == 1:
                        recursive_part2(neighbour, path, paths)

def walk_part1(mountain, trailheads):

    paths = []

    for head in trailheads:
        recursive_part1(head, "0", paths)
        flush(mountain)

    return paths

def walk_part2(trailheads):

    paths = []

    for head in trailheads:
        recursive_part2(head, "0", paths)

    return paths

def calculate(paths):

    scores = 0

    for path in paths:
        if path[-1] == "9":
            scores += 1

    return scores

def part1(input):

    mountain = parse(input)
    trailheads = heads(mountain)
    paths = walk_part1(mountain, trailheads)
    scores = calculate(paths)

    print("Part 1: The sum of all trailheads is", scores)

def part2(input):

    mountain = parse(input)
    trailheads = heads(mountain)
    paths = walk_part2(trailheads)
    scores = calculate(paths)

    print("Part 2: The sum of all trailheads is", scores)

filename = "../input/10.txt"
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