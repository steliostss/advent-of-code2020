# implementation for the day06 quiz of "advent of code" 

from string import ascii_lowercase

def read_input(infile):
    input = []
    buffer = []
    with open(infile) as f:
        for line in f:
            if line == '\n': # found the separator
                if (buffer): # if buffer has been set
                    input.append(buffer)
                buffer = []
                continue
            else: # valid line so far
                buffer.append(line.strip('\n').split(' '))
        input.append(buffer)
    return input

def flatten(t):
    flat_list = []
    buff_list = []
    for sublist in t:
        for item in sublist:
            for entry in item:
                buff_list.append(entry)
        flat_list.append(buff_list)
        buff_list = []
    return flat_list

def bincount(input):
    bin = []
    for i in input:
        sum = ''
        for answer in i:
            sum += answer
        bin.append(sum)
    sum = 0
    for i in bin:
        temp_bin = []
        for letter in range(0,len(i)):
            if i[letter] not in temp_bin:
                temp_bin.append(i[letter])
        # print(temp_bin)
        sum += len(temp_bin)
    return (sum)

def check(entry):
    answers = {}
    for question in entry[0]:
        answers[question] = 0

    for person in entry:
        for question in person:
            if question in answers.keys():
                answers[question] += 1
    sum = 0
    for i in answers:
        if answers[i] == len(entry):
            sum += 1
    return sum

def check_each_person(input):
    counter = 0
    for entry in input:
        counter += check(entry)
    return counter

early_input = read_input('input.txt')
flat_input = flatten(early_input)

res = bincount(flat_input)
print("Part 1:", res)

res = check_each_person(flat_input)
print("Part 2:", res)
