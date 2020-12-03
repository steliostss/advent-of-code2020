# implementation for the day02 quiz of "advent of code" 

def read_input(infile):
    input = []
    with open(infile) as f:
        for line in f:
            input.append(line.strip('\n'))
    return input

def begin_slope(ground, step_right=3, step_down=1):
    counter = 0
    dest = 0
    row = 0
    while row < len(ground):
        line = ground[row]
        if (line[dest%len(line)] == '#'):
            counter += 1
        # print("[", row, "]", "[", dest%len(line)-1, "]", " counter = ", counter, sep="")
        dest += step_right
        row += step_down

    return counter

input = read_input("input.txt")
hits = begin_slope(input)
print("Part 1:", hits)

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
trees = []
for i in range(0, len(slopes)):
    r, d = slopes[i]
    trees.append(begin_slope(input, r, d))

mul = 1
for i in trees:
    mul *= i

print("Part 2:", mul)
