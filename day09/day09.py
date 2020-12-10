# implementation for the day09 quiz of "advent of code" 
from itertools import combinations

def read_input(infile):
    input = []
    with open(infile) as f:
        for line in f:
            input.append(int(line.strip('\n')))
    return input

def findPairs(lst, K, N): 
    return [pair for pair in combinations(lst, N) if sum(pair) == K]

def findCombs(lst, K):
    front_i = 1
    back_i = 0
    sum = 0
    sum = lst[front_i] + lst[back_i]
    while front_i < len(lst)-1 and sum != K and back_i != front_i:
        if sum < K:
            front_i += 1
            sum += lst[front_i]
        else: # sum > K
            if (front_i-back_i) != 1:
                sum -= lst[back_i]
                back_i += 1
            else:
                sum -= lst[back_i]
                front_i += 1
                sum += lst[front_i]
                back_i += 1

    return back_i, front_i

input = read_input("input.txt")
preamble = 25
# input = read_input("test.txt")
# preamble = 5
for i in range(0+preamble, len(input)):
    part1 = findPairs(input[i-preamble:i], input[i], 2)
    if not part1:
        print("Part 1:", input[i])
        (x,y) = findCombs(input, input[i])

        part2 = min(input[x:y])+max(input[x:y])
        print("Part 2:", part2)
        break
