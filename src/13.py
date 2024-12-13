#Advent of Code 2024 Day 13

from tools import files
import time
import re

def test():

    input = [

        "Button A: X+94, Y+34",
        "Button B: X+22, Y+67",
        "Prize: X=8400, Y=5400",
        "",
        "Button A: X+26, Y+66",
        "Button B: X+67, Y+21",
        "Prize: X=12748, Y=12176",
        "",
        "Button A: X+17, Y+86",
        "Button B: X+84, Y+37",
        "Prize: X=7870, Y=6450",
        "",
        "Button A: X+69, Y+23",
        "Button B: X+27, Y+71",
        "Prize: X=18641, Y=10279",
        ""

    ]

    return input

def parse(input):

    prizes = []

    for i in range(0,len(input),4):

        A       = input[i]
        B       = input[i+1]
        prize   = input[i+2]

        m       = re.search(r"X\+\d+, Y\+\d+", A)
        A       = m.group(0)
        m       = re.search(r"X\+\d+, Y\+\d+", B)
        B       = m.group(0)
        m       = re.search(r"X\=\d+, Y\=\d+", prize)
        prize   = m.group(0)

        A       = A.split(", ")
        B       = B.split(", ")
        prize   = prize.split(", ")

        aX = int(A[0].replace("X+", ""))
        aY = int(A[1].replace("Y+", ""))

        bX = int(B[0].replace("X+", ""))
        bY = int(B[1].replace("Y+", ""))

        pX = int(prize[0].replace("X=", ""))
        pY = int(prize[1].replace("Y=", ""))

        prizes.append([[aX, aY], [bX, bY], [pX, pY]])

    return prizes

def linear(prize):

    ax = prize[0][0]
    ay = prize[0][1]

    bx = prize[1][0]
    by = prize[1][1]

    px = prize[2][0]
    py = prize[2][1]

    A = (px * by - py * bx) // (ax * by - bx * ay)
    B = (ax * py - px * ay) // (ax * by - bx * ay)

    if (A*ax + B*bx == px) and (A*ay + B*by == py):

        if (A <= 100 and B <= 100):
            return A*3 + B

    else:
        return 0
    
def linearoffset(prize, offset):

    ax = prize[0][0]
    ay = prize[0][1]

    bx = prize[1][0]
    by = prize[1][1]

    px = prize[2][0] + offset
    py = prize[2][1] + offset

    A = (px * by - py * bx) // (ax * by - bx * ay)
    B = (ax * py - px * ay) // (ax * by - bx * ay)

    if (A*ax + B*bx == px) and (A*ay + B*by == py):
        return A*3 + B

    else:
        return 0

def part1(input):

    prizes = parse(input)
    total = 0

    for prize in prizes:
        total += linear(prize)

    print("Part 1: The total number of tokens are", total)

def part2(input):

    prizes = parse(input)
    total = 0

    for prize in prizes:
        total += linearoffset(prize, 10000000000000)

    print("Part 2: The total number of tokens are", total)

filename = "../input/13.txt"
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