#
# Load the data
#

fname = 'test-input.txt' # Test data
fname = 'input.txt'      # Production data

import aocutils as aoc

data_2D = aoc.load_2D(fname, padding_symbol = '.', padding_width = 2)
data_3D = [[['.' for col in line] for line in data_2D],
           [['.' for col in line] for line in data_2D],
           data_2D,
           [['.' for col in line] for line in data_2D],
           [['.' for col in line] for line in data_2D]]
data_4D = [[[['.' for col in line] for line in layer] for layer in data_3D],
           [[['.' for col in line] for line in layer] for layer in data_3D],
           data_3D,
           [[['.' for col in line] for line in layer] for layer in data_3D],
           [[['.' for col in line] for line in layer] for layer in data_3D]]


#
# Part 1
#

import copy

def new_state_3D(x, y, z, data):
    num_active = len(aoc.neighbours_3D(x, y, z, data, '#'))
    if data[z][y][x] == '#':
        return '#' if num_active in {2, 3} else '.'
    return '#' if num_active == 3 else '.'

def state_cycle_3D(data):
    cdata = copy.deepcopy(data)
    for z in range(1, len(data) - 1):
        for y in range(1, len(data[0]) - 1):
            for x in range(1, len(data[0][0]) - 1):
                cdata[z][y][x] = new_state_3D(x, y, z, data)
    for z in range(len(data)):
        for y in range(len(data[0])):
            cdata[z][y].insert(0, '.')
            cdata[z][y].append(   '.')
        cdata[z].insert(0, ['.' for col in cdata[0][0]])
        cdata[z].append(   ['.' for col in cdata[0][0]])
    cdata.insert(0, [['.' for col in line] for line in cdata[0]])
    cdata.append(   [['.' for col in line] for line in cdata[0]])
    return cdata

cdata = copy.deepcopy(data_3D)
for cycle in range(6):
    cdata = state_cycle_3D(cdata)

print('Part 1:', len(['#' for layer in cdata for line in layer for sym in line if sym == '#']))


#
# Part 2
#

def new_state_4D(x, y, z, w, data):
    num_active = len(aoc.neighbours_4D(x, y, z, w, data, '#'))
    if data[w][z][y][x] == '#':
        return '#' if num_active in {2, 3} else '.'
    return '#' if num_active == 3 else '.'

def state_cycle_4D(data):
    cdata = copy.deepcopy(data)
    for w in range(1, len(data) - 1):
        for z in range(1, len(data[0]) - 1):
            for y in range(1, len(data[0][0]) - 1):
                for x in range(1, len(data[0][0][0]) - 1):
                    #print('Enne new state:', x, y, z, w)
                    cdata[w][z][y][x] = new_state_4D(x, y, z, w, data)
    for w in range(len(data)):
        for z in range(len(data[0])):
            for y in range(len(data[0][0])):
                cdata[w][z][y].insert(0, '.')
                cdata[w][z][y].append(   '.')
            cdata[w][z].insert(0, ['.' for col in cdata[0][0][0]])
            cdata[w][z].append(   ['.' for col in cdata[0][0][0]])
        cdata[w].insert(0, [['.' for sym in line] for line in cdata[0][0]])
        cdata[w].append(   [['.' for sym in line] for line in cdata[0][0]])
    cdata.insert(0, [[['.' for col in line] for line in layer] for layer in cdata[0]])
    cdata.append(   [[['.' for col in line] for line in layer] for layer in cdata[0]])
    return cdata

cdata = copy.deepcopy(data_4D)
for cycle in range(6):
    cdata = state_cycle_4D(cdata)

print('Part 2:', len(['#' for cube in cdata for layer in cube for line in layer for sym in line if sym == '#']))
