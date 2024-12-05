#Advent of Code 2024 Day 05

from tools import files
import time

def test():

    input = [

        "47|53",
        "97|13",
        "97|61",
        "97|47",
        "75|29",
        "61|13",
        "75|53",
        "29|13",
        "97|29",
        "53|29",
        "61|53",
        "97|53",
        "61|29",
        "47|13",
        "75|47",
        "97|75",
        "47|61",
        "75|61",
        "47|29",
        "75|13",
        "53|13",
        "",
        "75,47,61,53,29",
        "97,61,53,29,13",
        "75,29,13",
        "75,97,47,61,53",
        "61,13,29",
        "97,13,75,29,47"

    ]

    return input

def parse(input):

    rules = []
    updates = []

    for line in input:

        if "|" in line:

            rule = line.split("|")
            X = int(rule[0])
            Y = int(rule[1])
            rules.append([X,Y])

        elif "," in line:
            order = line.split(",")
            numbers = []
            for number in order:
                numbers.append(int(number))

            updates.append(numbers)

    return rules, updates

def valid(rules, update):

    for number in update:
        for rule in rules:

            if rule[0] == number:
                if rule[1] in update:
                    if update.index(number) > update.index(rule[1]):
                        return False
                
            if rule[1] == number:
                if rule[0] in update:
                    if update.index(number) < update.index(rule[0]):
                        return False
                
    return True

def fix(rules, update):


    while not valid(rules, update):

        for number in update:
            for rule in rules:

                if rule[0] == number:
                    if rule[1] in update:
                        if update.index(number) > update.index(rule[1]):
                            update.pop(update.index(number))
                            update.insert(update.index(rule[1])-1, number)

                if rule[1] == number:
                    if rule[0] in update:
                            if update.index(number) < update.index(rule[0]):
                                update.pop(update.index(number))
                                update.insert(update.index(rule[0])+1, number)

    return update


def calculate_valid(rules, updates):

    total = 0

    for update in updates:

        if valid(rules, update):
            total += update[len(update)//2]

    return total

def calculate_invalid(rules, updates):

    total = 0

    for update in updates:

        if not valid(rules, update):
            
            fixed = fix(rules, update)

            total += fixed[len(update)//2]

    return total

def part1(input):

    rules, updates = parse(input)

    total = calculate_valid(rules, updates)

    print("Part 1: The total value is", total)

def part2(input):

    rules, updates = parse(input)

    total = calculate_invalid(rules, updates)

    print("Part 2: The total value is", total)

filename = "../input/05.txt"
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