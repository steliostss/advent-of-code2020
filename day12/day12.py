from math import sin, cos, radians
import numpy as np

instructions = [[l.strip()[0], int(l.strip()[1:])] for l in open('input.txt', 'r')]
distance = {'N':0, 'E':0, 'W':0, 'S': 0}
dirs = 'ESWN'
curr_dir = dirs[0]

def changeDirection(turn: str, angle: int):
    if turn == 'L':
        return -angle//90
    if turn == 'R':
        return angle//90

for instr in instructions:
    if instr[0] == 'L' or instr[0] == 'R':
        curr_dir = dirs[(dirs.find(curr_dir) + changeDirection(instr[0],instr[1]))%4]
    elif instr[0] == 'F':
        distance[curr_dir] += instr[1]
    else:
        distance[instr[0]] += instr[1]
	
print("Part1:", abs(distance['N'] - distance['S']) + abs(distance['E'] - distance['W']))

def navigate_ship_two(instructions):
    x, y = 0, 0
    w_x, w_y = 10, 1
    cardinal_map = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
    lateral_map = {'L': 1, 'R': -1}
    for instruction in instructions:
        action = instruction[0]
        value = int(instruction[1:])
        if action in cardinal_map:
            w_x_unit, w_y_unit = cardinal_map[action]
            w_x += w_x_unit * value
            w_y += w_y_unit * value
        elif action in lateral_map:
            angle = radians(value * lateral_map[action])
            rotation_mat = np.array([[cos(angle), -sin(angle)],
                                     [sin(angle), cos(angle)]])
            coord_mat = np.array([[w_x, w_y]]).reshape(2, 1)
            w_x, w_y = [coord[0] for coord in np.matmul(rotation_mat, coord_mat)]
        elif action == 'F':
            x += w_x * value
            y += w_y * value
    return int(abs(x) + abs(y))

x = [ line.strip('\n') for line in open("input.txt")]
x1 = navigate_ship_two(x)
print("Part2:", x1)