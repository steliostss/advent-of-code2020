from copy import deepcopy
from sys import argv

def huge_tuple(): # huge aka not a normal number
	em = []
	oc = []
	for _ in range(0,9):
		em.append( ( (),() ) )
		oc.append( ( (),() ) )
	return em,oc

def update_neighbors(w8):
	temp = deepcopy(w8)
	for i,row in enumerate(temp.neighbors_list):
		for j,col in enumerate(row):
			em, oc = col
			if (temp.seats[i][j] == 0 and len(oc) == 0):
				w8.seats[i][j] = 1
			elif (temp.seats[i][j] == 1 and len(oc) >= 4):
				w8.seats[i][j] = 0
	return 

def count_oc(w8):
	cnt = 0
	for i,row in enumerate(w8.seats):
		for j,_ in enumerate(row):
			if str(w8.seats[i][j]) == '1':
				cnt += 1
	return cnt

def list_directions(dir):
	directions = [[0],[0]] # [i,j]
	for i in dir:
		if i == 'L': # left
			directions[1].append(-1) # column
		if i == 'R': # right
			directions[1].append( 1) # column
		if i == 'U': # up
			directions[0].append(-1) # row
		if i == 'D': # down
			directions[0].append( 1) # row
	
	return directions

class waiting_area(object):

	def __init__(self, infile):
		self.input = [line.strip('\n') for line in open(infile)]
		self.seats = []
		self.neighbors_list = []
		with open(infile) as f:
			for i,line in enumerate(f):
				line.strip('\n')
				self.seats.append([])
				for j,item in enumerate(line):
					# elif item == '#':
					# 	self.seats[i][j] = 1
					if item == 'L':
						self.seats[i].append(0)
					elif item == '.':
						self.seats[i].append('.')

	def print_waiting_area(self):
		# for i in self.input:
		# 	print(i)
		# print()
		for i in self.seats:
			for j in i:
				print(j, sep="", end="")
			print()

	def print_neighbors(self):
		print()
		for line in w8.neighbors_list:
			for col in line:
				print(len(col[0]), end='')
			print()

	# ---------------------------------------------------

	def check(self, i,j, irange, jrange):
		empty = []
		occupied = []
		for r in irange:
			for c in jrange:
				if r!=i or c!=j:
					if self.seats[r][c] == 0:
						empty.append((r,c))
					elif self.seats[r][c] == 1:
						occupied.append((r,c))
		return empty, occupied

	def available_neighbors(self,i,j):
		ilength = len(self.seats)-1
		jlength = len(self.seats[0])-1
		if self.seats[i][j] == '.':
			em, oc = huge_tuple()
			return em, oc
		if i == 0: # first row
			if j == 0: # first column
				em, oc = self.check(i,j, [i,i+1], [j,j+1])
			elif j == jlength: # last column
				em, oc = self.check(i,j, [i,i+1], [j-1,j])
			else: # just first row
				em, oc = self.check(i,j, [i,i+1], [j-1,j,j+1])
		elif i == ilength: # last row
			if j == 0: # first column
				em, oc = self.check(i,j, [i-1,i], [j,j+1])
			elif j == jlength: # last column
				em, oc = self.check(i,j, [i-1,i], [j-1,j])
			else: # just last row
				em, oc = self.check(i,j, [i-1,i], [j-1,j,j+1])
		else: # random row
			if j == 0: # first column
				em, oc = self.check(i,j, [i-1,i,i+1], [j,j+1])
			elif j == jlength: # last column
				em, oc = self.check(i,j, [i-1,i,i+1], [j-1,j])
			else:
				em, oc = self.check(i,j, [i-1,i,i+1], [j-1,j,j+1])
		return em, oc

	def check_neighbors(self):
		neighbors_list = []
		for i,row in enumerate(w8.seats):
			neighbors_list.append([])
			for j,_ in enumerate(row):
				# print(i,j)
				em, oc = w8.available_neighbors(i,j)
				neighbors_list[i].append((em,oc))
		self.neighbors_list = neighbors_list

	# ---------------------------------------------------

	def check_dirs(self, i, j, irange, jrange):
		empty = []
		occupied = []
		ilength = len(self.seats)-1
		jlength = len(self.seats[0])-1
		for r in irange:
			for c in jrange:
				() # TODO
		return

	def available_directions(self,i,j):
		ilength = len(self.seats)-1
		jlength = len(self.seats[0])-1
		directions = {
			'R': 0,
			'L': 0,
			'U': 0,
			'D': 0
		} # TODO
		if self.seats[i][j] == '.':
			# em, oc = huge_tuple()
			return []
		if i == 0:
			if j == 0:
				dirs = list_directions('RD')
			elif j == jlength:
				dirs = list_directions('LD')
			else:
				dirs = list_directions('LRD')
		elif i == ilength:
			if j == 0:
				dirs = list_directions('RU')
			elif j == jlength:
				dirs = list_directions('LU')
			else:
				dirs = list_directions('LRU')
		else:
			if j == 0:
				dirs = list_directions('UDR')
			elif j == jlength:
				dirs = list_directions('UDL')
			else:
				dirs = list_directions('LRUD')
		return dirs

	def check_directions(self):
		# TODO
		neighbors_list = []
		for i,row in enumerate(w8.seats):
			neighbors_list.append([])
			for j,_ in enumerate(row):
				# print(i,j)
				em, oc = w8.neighbors(i,j)
				neighbors_list[i].append((em,oc))
		self.neighbors_list = neighbors_list
		return


if __name__ == '__main__':

	part1 = argv[1]
	part2 = argv[2]
	w8 = waiting_area("input.txt")
	same = False
	while not same:
		compare = deepcopy(w8.seats)
		# w8.print_waiting_area()
		# w8.print_neighbors()
		w8.check_neighbors()
		update_neighbors(w8)
		# print("-----------------")
		same = (compare == w8.seats)
	print("Part 1:", count_oc(w8))

with open('input11.txt') as file:
    data = file.readlines()
    data = [ list(line.strip()) for line in data ]
    original = data.copy()

def get_num_occupied():
    count = 0
    for row in data:
        for seat in row:
            if seat == '#':
                count +=1
    return count

def get_adjacent_count(row,col):
    count = 0
    currentRow = data[row]

    #check left
    if col-1 >= 0:
        if currentRow[col-1] == '#': count +=1

    # check right
    if col+1 <= len(currentRow)-1:
        if currentRow[col+1] == '#': count += 1

    # above
    if row-1 >= 0:
        aboveRow = data[row-1]
        if aboveRow[col] == '#':
            count+=1
        
        if col-1 >= 0:
            if aboveRow[col-1] == '#':
                count+=1
        
        if col+1 <= len(aboveRow)-1:
            if aboveRow[col+1] == '#':
                count+=1

    # below
    if row+1 <= len(data)-1:
        belowRow = data[row+1]
        if belowRow[col] == '#':
            count+=1
        
        if col-1 >= 0:
            if belowRow[col-1] == '#':
                count+=1
        
        if col+1 <= len(belowRow)-1:
            if belowRow[col+1] == '#':
                count+=1
    
    return count

def get_adjaccent_count_p2(row, col):
    count = 0

    # i is for row, j for col
    iU, iD, jR, jL = row-1, row+1, col+1, col-1
    N, S, E, W, NE, SE, NW, SW = False, False, False, False, False, False, False, False

    while not (N and S and W and E and NE and SE and NW and SW):
        # North
        if not N and iU >= 0:
            if data[iU][col] == '#':
                count+=1
                N=True
            elif data[iU][col] == 'L':
                N=True
        else:
            N=True
            
        # South
        if not S and iD <= len(data)-1:
            if data[iD][col] == '#':
                count+=1
                S=True
            elif data[iD][col] == 'L':
                S=True
        else:
            S=True

        # East
        if not E and jR <= len(data[row])-1:
            if data[row][jR] == '#':
                count+=1
                E=True
            elif data[row][jR] == 'L':
                E=True
        else:
            E=True

        # West
        if not W and jL >= 0:
            if data[row][jL] == '#':
                count+=1
                W=True
            elif data[row][jL] == 'L':
                W=True
        else:
            W=True

        # North West
        if not NW and iU >= 0 and jL >= 0:
            if data[iU][jL] == '#':
                count+=1
                NW=True
            elif data[iU][jL] == 'L':
                NW=True
        else:
            NW=True

        # South West
        if not SW and iD <= len(data)-1 and jL >= 0:
            if data[iD][jL] == '#':
                count+=1
                SW=True
            elif data[iD][jL] == 'L':
                SW=True
        else:
            SW=True

        # North East
        if not NE and iU >= 0 and jR <= len(data[row])-1:
            if data[iU][jR] == '#':
                count+=1
                NE=True
            elif data[iU][jR] == 'L':
                NE=True
        else:
            NE=True

        # South East
        if not SE and iD <= len(data)-1 and jR <= len(data[row])-1:
            if data[iD][jR] == '#':
                count+=1
                SE=True
            elif data[iD][jR] == 'L':
                SE=True
        else:
            SE=True

        iU -= 1
        iD += 1
        jR += 1
        jL -= 1

    return count
        

def run_rules(tolerance):
    newSeating = []

    for row in range(len(data)):
        currentRow = data[row]
        newRow = []

        for col in range(len(currentRow)):
            if currentRow[col] == '.':
                newRow.append('.')
                continue

            adjacentCount = 0
            if tolerance == 4:
                adjacentCount = get_adjacent_count(row,col)
            elif tolerance == 5:
                adjacentCount = get_adjaccent_count_p2(row,col)

            if currentRow[col] == 'L' and adjacentCount == 0:
                newRow.append('#')
            
            elif currentRow[col] == '#' and adjacentCount >= tolerance:
                newRow.append('L')

            else:
                newRow.append(currentRow[col])
        newSeating.append(newRow)

    for i in range(len(data)):
        data[i] = newSeating[i]

def get_final_count(tolerance):
    prev = data.copy()
    run_rules(tolerance)

    while data != prev:
        prev = data.copy()
        run_rules(tolerance)
    
    return get_num_occupied()

print(get_final_count(4))

# part 2
data = original.copy()
print(get_final_count(5))