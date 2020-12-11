#
# Load the Data
#

# Test data
#fname = 'test-input.txt'
#fname = 'test2-input.txt'
#fname = 'test3-input.txt'
#fname = 'test4-input.txt'

# Production data
fname = 'input.txt'

with open(fname) as f:
    data = [['.'] + list(line) + ['.'] for line in f.read()[:-1].split('\n')]

data.insert(0, ['.' for i in range(len(data[0]))])
data.append(   ['.' for i in range(len(data[0]))])
dataj = {x + y * 1j: data[y][x] for y in range(len(data)) for x in range(len(data[y]))}


#
# Debug Utilities
#

def debug_display_floor(floor, x_size, y_size):
    for y in range(y_size):
        for x in range(x_size):
            print(floor[x + y * 1j], end = '')
        print()


#
# Part 1
#

directions = {
    -1 + 0j, # Upper middle
    -1 + 1j, # Upper right
     0 + 1j, # Right middle
     1 + 1j, # Right bottom
     1 + 0j, # Bottom middle
     1 - 1j, # Bottom left
     0 - 1j, # Left middle
    -1 - 1j  # Left upper
}

def visible_occupied_part1(loc, step, floor):
    return floor[loc + step] == '#'

def new_state(loc, floor, visibility_method, tolerance):
    global directions
    
    if floor[loc] == '.':
        return '.'
    occupied = sum([visibility_method(loc, direction, floor) for direction in directions])
    if floor[loc] == 'L' and occupied == 0:
        return '#'
    if floor[loc] == '#' and occupied >= tolerance:
        return 'L'
    return floor[loc]

def run(visibility_method, tolerance):
    count = 0
    floor = dataj
    while True:
        count += 1
        new_floor = {loc: new_state(loc, floor, visibility_method, tolerance) for loc in floor}
        if new_floor == floor:
            break
        floor = new_floor
    return len(list(filter(lambda s: s == '#', floor.values())))
    
print('Part 1: %d' % run(visible_occupied_part1, 4))


#
# Part 2
#

def visible_occupied_part2(loc, step, floor):
    cur_loc = loc + step
    while True:
        if cur_loc not in floor:
            return False
        if floor[cur_loc] == '#':
            return True
        elif floor[cur_loc] == 'L':
            return False
        cur_loc = cur_loc + step

print('Part 1: %d' % run(visible_occupied_part2, 5))
