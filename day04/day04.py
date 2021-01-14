# implementation for the day04 quiz of "advent of code"

import re
import sys

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

def make_empty_dict():
    dictionary = {
        "byr" : "",
        "iyr" : "",
        "eyr" : "",
        "hgt" : "",
        "hcl" : "",
        "ecl" : "",
        "pid" : "",
        "cid" : ""
    }
    return dictionary

def mkdict(entries):
    final = []
    for entry in entries:
        entry_dict = make_empty_dict()
        for i in entry:
            temp_list = i.split(':')
            entry_dict[temp_list[0]] = temp_list[1]
        final.append(entry_dict)
    return final

def check_entry(entry):
    checks = ["byr","iyr","eyr","hgt","hcl","ecl","pid"] # cid is missing, as it should
    for i in checks:        # for all the fields we want to check
        if entry[i] == "":  # if field is empty
            return False    # passport is invalid
    return True

def check_entries(passports):
    counter = 0
    for entry in passports:     # for each passport
        if check_entry(entry):  # if all checks completed successfully then
            counter += 1        # increse the counter
    return counter

field_req = {
    'byr': re.compile(r'^(19[2-9][0-9]|200[0-2])$'),
    'iyr': re.compile(r'^(201[0-9]|2020)$'),
    'eyr': re.compile(r'^(202[0-9]|2030)$'),
    'hgt': re.compile(r'^(1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in$'),
    'hcl': re.compile(r'^#[0-9a-f]{6}$'),
    'ecl': re.compile(r'^amb|blu|brn|gry|grn|hzl|oth$'),
    'pid': re.compile(r'^[0-9]{9}$')
}

def validate_entries(passports):
    counter = 0
    for entry in passports:
        flag2 = True
        flag1 = check_entry(entry)
        for i in field_req:
            flag2 = field_req[i].match(entry[i])
            if not flag2:
                break
        if (flag1 and flag2):
            counter += 1
    return counter

def part1(t):
    return check_entries(t)

def part2(t):
    return validate_entries(t)

# byr:(19[2-9][0-9]|200[0-2])
# iyr:(201[0-9]|2020)
# eyr:(202[0-9]|2030)
# hgt:((1([5-8][0-9])|9[0-3])cm|([59]|6[0-9]|7[0-6])in)
# hcl:(#[0-9a-f]{6})
# ecl:(amb|blu|brn|gry|grn|hzl|oth)
# pid:[0-9]{9}
# cid:.+


input = read_input("input.txt")
input = flatten(input)
fixed = mkdict(input)

counter = part1(fixed)
print("Part 1:", counter)

counter = part2(fixed)
print("Part 2:", counter)

# one line solution taken from reddit
print(len(re.findall(''.join(r'(\n\n|^)(?=(\S+\s)*byr: (19[2-9]\d|200[0-2])\b )(?=(\S+\s)*iyr: (201\d|2020)\b )(?=(\S+\s)*eyr: (202\d|2030)\b )(?=(\S+\s)*hgt: ((1[5-8]\d|19[0-3])cm|(59|6\d|7[0-6])in)\b )(?=(\S+\s)*hcl: #[0-9a-f]{6}\b )(?=(\S+\s)*ecl: (amb|blu|brn|gry|grn|hzl|oth)\b )(?=(\S+\s)*pid: \d{9}\b )'.split()[::1+(sys.argv[1]<'2')]), sys.stdin.read())))
