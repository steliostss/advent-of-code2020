
from pprint import pprint
import re

def read_passport(x):
    fields_list = x.replace('\n', ' ').split(' ')
    fields = dict()
    for field in fields_list:
        key, val = field.split(':', 2)
        fields[key] = val
    return fields

def validate_passport(x: dict):
    required_fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"] #,"cid"]
    
    # Validate keys
    if any(field not in x for field in required_fields):
        return False

    # Validate values
    if int(x['byr']) < 1920 or int(x['byr']) > 2002:
        # print(x, "Invalid byr")
        return False
    
    if int(x['iyr']) < 2010 or int(x['iyr']) > 2020:
        # print(x, "Invalid iyr")
        return False

    if int(x['eyr']) < 2020 or int(x['eyr']) > 2030:
        # print(x, "Invalid eyr")
        return False

    if re.match(r"\d+cm", x['hgt']):
        if int(x['hgt'][:-2]) < 150 or int(x['hgt'][:-2]) > 193:
            # print(x, "Invalid hgt")
            return False
    elif re.match(r"\d+in", x['hgt']):
        if int(x['hgt'][:-2]) < 59 or int(x['hgt'][:-2]) > 76:
            # print(x, "Invalid hgt")
            return False
    else:
        return False
    
    if not re.match(r"#(\d|[a-f]){6}", x['hcl']):
        # print(x, "Invalid hcl")
        return False
    
    if all([x['ecl'] != y for y in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]]):
        # print(x, "Invalid ecl")
        return False
    
    if not re.match(r"\d{9}", x['pid']):
        # print(x, "Invalid pid")
        return False
    
    return True

with open("input.txt", 'r') as batch_file:
    # print(batch_file)
    passport_strings = batch_file.read()[:-1].split("\n\n")
    pprint(passport_strings[-1])
    passports = [read_passport(x) for x in passport_strings]
    pprint(passports[-1])
    validation = [(x, validate_passport(x)) for x in passports]
    valids = sum([validate_passport(x) for x in passports])
    # pprint([x for (x, y) in validation if y])
    print(f"No. of valid passwords: {valids}")