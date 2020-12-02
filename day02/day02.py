# implementation for the day02 quiz of "advent of code" 

def read_input(infile):
    input = []
    with open(infile) as f:
        for line in f:
            # print(line.strip('\n').split(':')[0])
            entry = line.strip('\n').split(':')
            
            # handle properties
            prop = entry[0]
            id = prop.split(' ')[1]
            times = prop.split(' ')[0]
            times_from = int(times.split('-')[0])
            times_to = int(times.split('-')[1])
            # handle password
            password = entry[1].strip(' ')
            tup = (times_from, times_to,  id , password )
            input.append(tup)
    return input

# return 1 if password is valid
# else return 0
def check_password_pt1(entry):
    ( min, max, id, pswd ) = entry
    count = pswd.count(id)
    if count >= min and count <= max:
        return 1
    else:
        return 0

def check_password_pt2(entry):
    ( fr, to, id, pswd ) = entry
    if ( pswd[fr-1] == id and pswd[to-1] != id ):
        return 1
    if ( pswd[fr-1] != id and pswd[to-1] == id ):
        return 1
    else:
        return 0

input = read_input("input.txt")
counter = 0
for i in input:
    counter += check_password_pt1(i)
print("part1:", counter)

counter = 0
for i in input:
    counter += check_password_pt2(i)

print("part2:", counter)

