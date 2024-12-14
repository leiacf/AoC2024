#Advent of Code 2024 Day 14

from tools import files
import time

def test():

    input = [

        "p=0,4 v=3,-3",
        "p=6,3 v=-1,-3",
        "p=10,3 v=-1,2",
        "p=2,0 v=2,-1",
        "p=0,0 v=1,3",
        "p=3,0 v=-2,-2",
        "p=7,6 v=-1,-3",
        "p=3,0 v=-1,-2",
        "p=9,3 v=2,3",
        "p=7,3 v=-1,2",
        "p=2,4 v=2,-3",
        "p=9,5 v=-3,-3"

    ]

    return input

def parse(input):

    robots = []

    for line in input:
        line = line.replace("p=", "")
        line = line.replace(" v=", ",")
        line = line.strip()
        robot = [int(x) for x in line.split(",")]

        robots.append(robot)

    return robots

def move(ver, hor, robot, times):

    x = robot[0]
    y = robot[1]

    dx = robot[2]
    dy = robot[3]

    for _ in range(times):

        x = x+dx
        y = y+dy

        if x < 0:
            x = x + hor
        elif x >= hor:
            x = x % hor

        if y < 0:
            y = y + ver
        elif y >= ver:
            y = y % ver

    robot[0] = x
    robot[1] = y

    return robot

def tuples(robots):

    points = []
    
    for robot in robots:
        points.append((robot[0], robot[1]))

    return points

def calculate(ver, hor, robots):

    points = tuples(robots)

    vmiddle = ver // 2+1
    hmiddle = hor // 2+1
    q1, q2, q3, q4 = 0, 0, 0, 0

    #Q1
    for x in range(hmiddle-1):
        for y in range(vmiddle-1):
            if (x, y) in points:
                q1 += points.count((x, y))

    #Q2
    for x in range(hmiddle, hor):
        for y in range(vmiddle-1):
            if (x, y) in points:
                q2 += points.count((x, y))

    #Q3
    for x in range(hmiddle-1):
        for y in range(vmiddle, ver):
            if (x, y) in points:
                q3 += points.count((x, y))

    #Q4
    for x in range(hmiddle, hor):
        for y in range(vmiddle, ver):
            if (x, y) in points:
                q4 += points.count((x, y))

    return q1*q2*q3*q4

def test(ver, hor, robots):

    points = tuples(robots)
    grid = []

    for y in range(ver):
        line = []
        for x in range(hor):
            if (x, y) in points:
                line.append("#")
            else:
                line.append(" ")

        row = "".join(line)
        grid.append(row)

    for line in grid:
        print(line)

def part1(input):

    ver = 103
    hor = 101
    times = 100
    robots = parse(input)

    for index, robot in enumerate(robots):
        move(ver, hor, robot, times)
        robots[index] = robot

    safe = calculate(ver, hor, robots)

    print("Part 1: The safety factor is", safe)

def part2(input):

    ver = 103
    hor = 101
    times = 10000
    robots = parse(input)

    print()

    for x in range(1, times):

        for index, robot in enumerate(robots):
            move(ver, hor, robot, 1)
            robots[index] = robot

        amount = list(set(tuples(robots)))

        if len(amount) == 500:
            test(ver, hor, robots)
            print("Part 2: Tree found at", x)

filename = "../input/14.txt"
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