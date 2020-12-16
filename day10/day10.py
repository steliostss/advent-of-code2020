# implementation for the day10 quiz of "advent of code"

def part1(input):
    diff1 = 0
    diff3 = 1
    if input[0] == 3:
        diff3+=1
    elif input[0] == 1:
        diff1+=1

    for i in range(0, len(input)-1):
        if i+1 > len(input): break
        dJ = input[i+1] - input[i]
        if(dJ == 1):
            diff1 += 1
        elif (dJ == 3):
            diff3 += 1
    return diff1, diff3

def part2(input, id, max_id, pretext):
    # print(pretext, end='')
    # for i in input:
    #     print(i, end=' ')
    # print()
    if (len(input) == 2):
        return 1 # escape sequence
    else:
        cnt = 0
        limit = 0
        for i in {1,2,3}:
            if id+i < max_id and input[0+i]-input[0] <= 3:
                limit +=1
        i = 1
        while (i<=limit):
            if (input[i+1] - input[i]) <= 3 :
                cnt += part2(input[i:], id+i, max_id, pretext+'\t')
            else:
                break
            i += 1
        return cnt
    
input = sorted([int(line.strip('\n')) for line in open('input.txt')])
# print(input)

d1, d3 = part1(input)
# print(d1, d3)
print("Part 1:", d1*d3)

input.append(max(input)+3)
input.insert(0,0)

print("\nDON'T ATTEMPT TO RUN PART2 CAUSE BAD THINGS ARE GONNA HAPPEN")
print("BAD MEMORY HANDLING BOI HERE")
print("RUN AT YOUR OWN RISK")
# cnt = part2(input, 0, len(input)-1, '')
# print("Part 2:", cnt)
