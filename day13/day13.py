import fileinput

# ------- Part1 -------

timetable = [line.strip('\n').replace('x,', '').split(',') for line in open("input.txt", 'r')]
timestamp = int(timetable[0][0])
buses = [ int(j) for j in timetable[1]]

divs = []
diffs = []
for i,j in enumerate(buses):
    divs.append(timestamp // j)
    offset = 1
    temp = (divs[i]+offset)*buses[i]
    while temp < timestamp:
        offset += 1
        temp = (divs[i]+offset)*buses[i]
    diffs.append(temp - timestamp)

index, minim = min(enumerate(diffs), key=lambda x:x[1])
print("Part 1:", minim*buses[index])

# print(buses)

# ------- Part2 -------

# timetable_noisy = [line.strip('\n').replace('x','-1').split(',') for line in open("test.txt", 'r')]
# clean = [int(i) for i in timetable_noisy[1]]
# print(clean)

# found = False
# seconds = clean[0]
# while not found:
#     found = True
#     for i,bus in enumerate(clean):
#         if bus > 0: found = (bus % seconds) == 0 and found
#         seconds += 1
# print(seconds)

input = fileinput.input("input.txt")

arrival = int(next(input))
buses = [None if bus == "x" else int(bus) for bus in next(input).split(",")]

remainders = [-(arrival % (-bus)) if bus else float("inf") for bus in buses]
print(remainders)
print(
    "Part 1:",
    min(enumerate(buses), key=lambda x: remainders[x[0]])[1] * min(remainders),
)
