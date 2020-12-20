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
