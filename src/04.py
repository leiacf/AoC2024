#Advent of Code 2024 Day 04

from tools import files
import time

def test():

    input = [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX"
    ]

    return input

def rotate(input):

    rotated = []

    for j in range(len(input[0])):
        line = ""
        for i in range(len(input)):
            line = line+input[i][j]
            
        rotated.append(line[::-1])

    return rotated

def down(input):

    diagonally = []

    size = len(input)

    #middle
    line = ""
    for i in range(size):
        line += input[i][i]

    diagonally.append(line)
       
    for hor in range(1, size):
        line = ""

        for i in range(0, size-hor):
            line += input[i][hor+i]

        diagonally.append(line)

    for ver in range(1, size):
        line = ""

        for i in range(0, size-ver):
            line += input[ver+i][i]

        diagonally.append(line)

    return diagonally

def parse(input):

    total = 0

    #Horizontal
    for line in input:
        total += line.count("XMAS")
        line = line[::-1]
        total += line.count("XMAS")

    #Vertical
    vertical = rotate(input)
    for line in vertical:
        total += line.count("XMAS")
        line = line[::-1]
        total += line.count("XMAS")

    #Diagonally
    diagonally = down(input)
    for line in diagonally:
        total += line.count("XMAS")
        line = line[::-1]
        total += line.count("XMAS")

    #Diagonally again
    rotated = rotate(input)
    done = down(rotated)
    for line in done:
        total += line.count("XMAS")
        line = line[::-1]
        total += line.count("XMAS")

    return total

def xmas(a, input):

    ver = a[0]
    hor = a[1]

    if (ver == 0 or ver == len(input)-1 or hor == 0 or hor == len(input)-1):
        return False

    nw = input[ver-1][hor-1]
    ne = input[ver-1][hor+1]
    sw = input[ver+1][hor-1]
    se = input[ver+1][hor+1]

    if nw == "M":
        if se == "S":
            if ne == "M":
                if sw == "S":
                    return True
                else:
                    return False
            elif ne == "S":
                if sw == "M":
                    return True
                else:
                    return False
        else:
            return False
    elif nw == "S":
        if se == "M":
            if ne == "M":
                if sw == "S":
                    return True
                else:
                    return False
            elif ne == "S":
                if sw == "M":
                    return True
                else:
                    return False
        else:
            return False


    return False

def mas(input):

    A = []
    total = 0

    for ver in range(len(input)):
        for hor in range(len(input)):

            if input[ver][hor] == "A":
                A.append([ver,hor])

    for a in A:
        if xmas(a, input):
            total += 1

    return total

def part1(input):

    total = parse(input)
    print("Part 1: The number of times XMAS appears is", total)

def part2(input):

    total = mas(input)

    print("Part 2: The amount of MAS is", total)

filename = "../input/04.txt"
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