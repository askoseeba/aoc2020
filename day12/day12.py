#
# Load the Data
#

#fname = 'test-input.txt' # Test data
fname = 'input.txt'      # Production data

import aocutils as aoc

data = [(line[0], int(line[1:])) for line in aoc.load_1D(fname)]

#
# Part 1
#

def abs_direction(facing_direction, direction, degrees):
    assert(direction in {'L', 'R'})
    turns = degrees / 90
    return {'N': {'L': 'W' if turns == 1 else abs_direction('W', 'L', degrees - 90),
                  'R': 'E' if turns == 1 else abs_direction('E', 'R', degrees - 90)},
            'E': {'L': 'N' if turns == 1 else abs_direction('N', 'L', degrees - 90),
                  'R': 'S' if turns == 1 else abs_direction('S', 'R', degrees - 90)},
            'S': {'L': 'E' if turns == 1 else abs_direction('E', 'L', degrees - 90),
                  'R': 'W' if turns == 1 else abs_direction('W', 'R', degrees - 90)},
            'W': {'L': 'S' if turns == 1 else abs_direction('S', 'L', degrees - 90),
                  'R': 'N' if turns == 1 else abs_direction('N', 'R', degrees - 90)}
    }[facing_direction][direction]

def new_coords(x, y, direction, length):
    assert(direction in {'N', 'E', 'S', 'W'})
    return {
        'N': (lambda x, y, length: (x         , y + length)),
        'E': (lambda x, y, length: (x + length, y         )),
        'S': (lambda x, y, length: (x         , y - length)),
        'W': (lambda x, y, length: (x - length, y         ))
    }[direction](x, y, length)

facing = 'E'
x      = 0
y      = 0
for step in data:
    if step[0] in {'L', 'R'}:
        facing = abs_direction(facing, *step)
    if step[0] in {'N', 'E', 'S', 'W'}:
        x, y = new_coords(x, y, *step)
    if step[0] == 'F':
        x, y = new_coords(x, y, facing, step[1])

print('Part 1: %d' % (abs(x) + abs(y)))


#
# Part 2
#

def rotate_wp(wx, wy, direction, degrees):
    assert(direction in {'L', 'R'})
    turns = degrees / 90
    if turns > 1:
        wx, wy = rotate_wp(wx, wy, direction, degrees - 90)
    if direction == 'L':
        return -wy, wx
    #else direction == 'R':
    return wy, -wx

sx, sy, wx, wy = 0, 0, 10, 1
for step in data:
    if step[0] in {'N', 'E', 'S', 'W'}:
        wx, wy = new_coords(wx, wy, *step)
    if step[0] in {'L', 'R'}:
        wx, wy = rotate_wp(wx, wy, *step)
    if step[0] == 'F':
        sx += step[1] * wx
        sy += step[1] * wy

print('Part 2: %d' % (abs(sx) + abs(sy)))
