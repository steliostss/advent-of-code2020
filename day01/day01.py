# implementation for the day01 quiz of "advent of code"
\
from itertools import combinations

def part1(input):
    front = 1
    back = 0
    while (front < len(input) and back < len(input)):
        sum = sorted[back] + sorted[front]
        if (sum == 2020):
            return (sorted[back]*sorted[front])
        elif (sum > 2020):
            back += 1
        else: # sum < 2020
            front +=1



def fsum(val):
      return sum(val) == 2020

def part2(input):
    res = list(filter(fsum,list(combinations(input, 3))))
    res = res[0]
    result = res[0]*res[1]*res[2]
    return result

input = []
with open("input.txt") as f:
    for line in f:
        input.append(int(line.strip('\n')))
    sorted = sorted(input)
    result1 = part1(sorted)
    print("part1:", result1)
    result2 = part2(sorted)
    print("part2:", result2)

