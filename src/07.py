#Advent of Code 2024 Day 07

from tools import files
import time

def test():

    input = [

        "190: 10 19",
        "3267: 81 40 27",
        "83: 17 5",
        "156: 15 6",
        "7290: 6 8 6 15",
        "161011: 16 10 13",
        "192: 17 8 14",
        "21037: 9 7 18 13",
        "292: 11 6 16 20"

    ]

    return input

def parse(input):

    numbers = []

    for line in input:
        result, digits = line.split(": ")
        values = [int(x) for x in digits.split(" ")]
        
        values.insert(0, int(result))

        numbers.append(values)

    return numbers

def recursive(entry, results, result):

    plus = result + entry[0]
    multiply = result * entry[0]

    if len(entry) == 1:

        results.append(plus)
        results.append(multiply)

    else:

        recursive(entry[1:], results, plus)
        recursive(entry[1:], results, multiply)

def calculate(numbers):

    total = 0

    for entry in numbers:

        results = []
        result = entry[0]
        recursive(entry[2:], results, entry[1])

        for res in results:
            if res == result:
                total += result
                break

    return total

def rec(entry, results, result):

    plus = result + entry[0]
    multiply = result * entry[0]
    concat = int(str(result) + str(entry[0]))

    if len(entry) == 1:

        results.append(plus)
        results.append(multiply)
        results.append(concat)

    else:

        rec(entry[1:], results, plus)
        rec(entry[1:], results, multiply)
        rec(entry[1:], results, concat)

def cal(numbers):

    total = 0

    for entry in numbers:

        results = []
        result = entry[0]
        rec(entry[2:], results, entry[1])

        for res in results:
            if res == result:
                total += result
                break

    return total

def part1(input):

    numbers = parse(input)

    total = calculate(numbers)

    print("Part 1: The total sum of the doable equations is", total)

def part2(input):

    numbers = parse(input)

    total = cal(numbers)

    print("Part 2: The total sum of the doable equations is", total)

filename = "../input/07.txt"
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