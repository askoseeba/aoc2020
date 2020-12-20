fname = 'test-input.txt'            # Test data
fname = 'input.txt'                 # Production data

monster_fname = 'input-monster.txt' # Monster data

import aocutils as aoc
import numpy as np

tilesdata = [dict(zip(('id', 'data'), tiledata.lstrip('Tile: ').split(':'))) for tiledata in aoc.load_1D(fname, sep = '\n\n')]
tilesdata = [{'id': tile['id'], 'data': np.array([list(line) for line in tile['data'].lstrip('\n').split('\n')])} for tile in tilesdata]

monster = np.array(aoc.load_2D(monster_fname, l_strip = False, r_strip = False))


#
# Part 1
#

import copy

edge = {
    'N': (lambda tile: tile['data'][0]),
    'E': (lambda tile: tile['data'][:, 9]),
    'S': (lambda tile: tile['data'][9]),
    'W': (lambda tile: tile['data'][:, 0])
}
orient_edge = {
    'N': (lambda edge, direction: np.flip(edge) if direction in {'N', 'E'} else edge),
    'E': (lambda edge, direction: np.flip(edge) if direction in {'N', 'E'} else edge),
    'S': (lambda edge, direction: np.flip(edge) if direction in {'S', 'W'} else edge),
    'W': (lambda edge, direction: np.flip(edge) if direction in {'S', 'W'} else edge)
}
def orient_tile(dir_match, tiledata):
    if dir_match in {'NN', 'EE', 'SS', 'WW'}: # Rotate 180 degrees
        return np.rot90(m = tiledata, k = 2)
    if dir_match in {'NE', 'ES', 'SW', 'WN'}: # Rotate  90 degrees clockwise
        #print('Kaka ja ventikas?', dir_match)
        return np.rot90(m = tiledata, k = 1, axes = (1, 0))
    if dir_match in {'NS', 'EW', 'SN', 'WE'}: # Don't rotate
        return              tiledata
    if dir_match in {'NW', 'EN', 'SE', 'WS'}: # Rotate  90 degrees counter clockwise
        return np.rot90(m = tiledata, k = 1)

def check_edges(tile1, tile2):
    for dir1 in ['N', 'E', 'S', 'W']:
        for dir2 in ['N', 'E', 'S', 'W']:
            if sum(edge[dir1](tile1) == orient_edge[dir1](edge[dir2](tile2), dir2)) == 10:
                return dir1 + dir2
            tile2_f = {'id': tile2['id'], 'data': np.flipud(tile2['data'])}
            if sum(edge[dir1](tile1) == orient_edge[dir1](edge[dir2](tile2_f), dir2)) == 10:
                return dir1 + dir2 + 'f'
    return ()

td1                  = copy.deepcopy(tilesdata)
final_tiles          = {0j: td1[0]}
prev_new_final_tiles = {0j: td1[0]}
del td1[0]
count = 0
while td1:
    new_final_tiles = {}
    count += 1
    for loc, ftile in prev_new_final_tiles.items():
        for tile in td1:
            dir_match = check_edges(ftile, tile)
            if dir_match:
                if 'f' in dir_match:
                    tile['data'] = np.flipud(tile['data'])
                dir_match = dir_match[:2]
                tile['data'] = orient_tile(dir_match, tile['data'])
                new_coord = loc + aoc.directions_2D_imag_NESW_dict[dir_match[0]]
                if new_coord in final_tiles:
                    assert(not new_coord in final_tiles)
                if new_coord in new_final_tiles:
                    assert(tile['id'] == new_final_tiles[new_coord]['id'])
                new_final_tiles[new_coord] = tile
    final_tiles          = {**final_tiles, **new_final_tiles}
    prev_new_final_tiles = new_final_tiles
    new_td1 = [tile for tile in td1 if tile not in final_tiles.values()]
    td1 = new_td1

minx = min([int(loc.real) for loc in final_tiles.keys()])
maxx = max([int(loc.real) for loc in final_tiles.keys()])
miny = min([int(loc.imag) for loc in final_tiles.keys()])
maxy = max([int(loc.imag) for loc in final_tiles.keys()])

print('Part 1:', int(final_tiles[(minx + miny * 1j)]['id']) * int(final_tiles[(minx + maxy * 1j)]['id']) * int(final_tiles[(maxx + miny * 1j)]['id']) * int(final_tiles[(maxx + maxy * 1j)]['id']))


#
# Part 2
#

def check_monster(image, monster):
    matched_locations = np.empty([0, 2], dtype = int)
    for x in range(image.shape[0] - monster.shape[0]):
        for y in range(image.shape[1] - monster.shape[1]):
            window = image[x : x + monster.shape[0], y : y + monster.shape[1]]
            matches = np.argwhere((monster == '#') & (window == '#')) + [x, y]
            if len(matches) == 15: # Number of monster pieces: 15
                matched_locations = np.concatenate([matched_locations, matches])
    return matched_locations

def check_monster_and_rotate(image, monster):
    image_copy = copy.deepcopy(image)
    for i in range(4):
        matches = check_monster(image_copy, monster)
        if len(matches) != 0:
            print('Found the monsters. Number of monster pieces:', len(matches))
            return matches, image_copy
        if i != 3:
            print('No monster found. Rotating image.')
            image_copy = np.rot90(image_copy)
    return matches, image

print('Looking for this monster:')
aoc.print_2D(monster)

final_tiles_part2 = {loc: tile['data'][1:-1, 1:-1] for loc, tile in final_tiles.items()}

rows = []
for x in range(minx, maxx + 1):
    row = []
    for y in range(miny, maxy + 1):
        tile = final_tiles_part2[x + y*1j]
        row.append(tile)
    rows.append(np.concatenate(row, axis = 1))
image = np.concatenate(rows, axis = 0)

matches, final_image = check_monster_and_rotate(image, monster)
if len(matches) == 0:
    print('No monsters found. Flipping image, upside down.')
    flipped_image = np.flipud(image)
    matches, final_image = check_monster_and_rotate(flipped_image, monster)

image_illuminated = copy.deepcopy(final_image)
for match in matches:
    image_illuminated[match[0], match[1]] = 'O'
print('Part 2:', sum(sum(image_illuminated == '#')))
aoc.print_2D(image_illuminated)
