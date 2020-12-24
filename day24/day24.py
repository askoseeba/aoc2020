#
# Load the data
#

fname = 'test-input.txt' # Test data
#fname = 'test0-input.txt' # Test data
fname = 'input.txt'      # Production data

import aocutils as aoc

data = aoc.load_1D(fname)


#
# Part 1
#

tiles = set()
for line in data:
    i = 0
    tile = 0 + 0j
    while i < len(line):
        if line[i] in 'ew':
            tile += 2 * aoc.directions_2D_imag_dict[line[i].upper()]
            i += 1
        else:
            tile += aoc.directions_2D_imag_dict[line[i : i + 2].upper()]
            i += 2
    if tile in tiles:
        tiles.remove(tile)
    else:
        tiles.add(tile)

print('Part 1:', len(tiles))


#
# Part 2
#

import copy

def count_black(loc, tiles):
    directions = {-2j, 2j, -1 - 1j, -1 + 1j, 1 - 1j, 1 + 1j}
    count = 0
    for d in directions:
        if loc + d in tiles:
            count += 1
    return count

yesterday_tiles = copy.deepcopy(tiles)

for day in range(1, 101):
    NS = [int(tile.real) for tile in yesterday_tiles]
    WE = [int(tile.imag) for tile in yesterday_tiles]
    minns, maxns, minwe, maxwe = min(NS), max(NS), min(WE), max(WE)
    new_tiles = set()
    for we in range(minwe - 2, maxwe + 3):
        for ns in range(minns - 1, maxns + 2):
            if ns % 2 == 0 and we % 2 == 1 or ns % 2 == 1 and we % 2 == 0:
                continue
            loc = ns + we * 1j
            cb = count_black(loc, yesterday_tiles)
            if loc in yesterday_tiles and cb in {1, 2} or loc not in yesterday_tiles and cb == 2:
                new_tiles.add(loc)
    yesterday_tiles = copy.deepcopy(new_tiles)

print('Part 2:', len(new_tiles))
