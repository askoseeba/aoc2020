directions_2D = [
    {'x': -1, 'y':  0}, # North
    {'x': -1, 'y':  1}, # North-East
    {'x':  0, 'y':  1}, # East
    {'x':  1, 'y':  1}, # South-East
    {'x':  1, 'y':  0}, # South
    {'x':  1, 'y': -1}, # South-West
    {'x':  0, 'y': -1}, # West
    {'x': -1, 'y': -1}  # North-West
]

directions_2D_NESW = [
    {'x': -1, 'y':  0}, # North
    {'x':  0, 'y':  1}, # East
    {'x':  1, 'y':  0}, # South
    {'x':  0, 'y': -1}, # West
]

directions_2D_imag = [
    -1 + 0j, # North
    -1 + 1j, # North-East
     0 + 1j, # East
     1 + 1j, # South-East
     1 + 0j, # South
     1 - 1j, # South-West
     0 - 1j, # West
    -1 - 1j  # North-West
]

directions_2D_imag_NESW = [
    -1 + 0j, # North
     0 + 1j, # East
     1 + 0j, # South
     0 - 1j, # West
]

directions_2D_imag_NESW_dict = {
    'N': -1 + 0j, # North
    'E':  0 + 1j, # East
    'S':  1 + 0j, # South
    'W':  0 - 1j, # West
}

def load_1D(fname, l_strip = True, r_strip = True, to_int = False, sep = '\n'):
    with open(fname) as f:
        data = f.read()
    if l_strip:
        data = data.lstrip()
    if r_strip:
        data = data.rstrip()
    data = data.split(sep)
    if to_int:
        return [int(line) for line in data]
    return data
    
def load_2D(fname, l_strip = True, r_strip = True, padding_symbol = None, padding_width = 1):
    data = [list(line) for line in load_1D(fname, l_strip, r_strip)]
    if padding_symbol:
        for i in range(padding_width):
            data = [[padding_symbol] + row + [padding_symbol] for row in data]
            data.insert(0, [padding_symbol for i in range(len(data[0]))])
            data.append(   [padding_symbol for i in range(len(data[0]))])
    return data

def load_2D_imag(fname, l_strip = True, r_strip = True, padding_symbol = None):
    data = load_2D(fname, l_strip, r_strip, padding_symbol)
    return {x + y * 1j: data[y][x] for y in range(len(data)) for x in range(len(data[y]))}

def neighbours_2D(x, y, data, is_sym = None):
    if is_sym:
        return [data[y + direction['y']][x + direction['x']]
                for direction in directions_2D if data[y + direction['y']][x + direction['x']] == is_sym]
    return [data[y + direction['y']][x + direction['x']] for direction in directions_2D]

def neighbours_3D(x, y, z, data, is_sym):
    active_neighbours = []
    for z_i in [z - 1, z, z + 1]:
        active_neighbours += neighbours_2D(x, y, data[z_i], is_sym)
        if z_i != z and data[z_i][y][x] == is_sym:
            active_neighbours.append(is_sym)
    return active_neighbours

def neighbours_4D(x, y, z, w, data, is_sym):
    active_neighbours = []
    for w_i in [w - 1, w, w + 1]:
        active_neighbours += neighbours_3D(x, y, z, data[w_i], is_sym)
        if w_i != w and data[w_i][z][y][x] == is_sym:
            active_neighbours.append(is_sym)
    return active_neighbours

def neighbours_2D_imag(loc, data, is_sym = None, is_not_sym = None, is_NESW = False):
    assert(not is_sym or not is_not_sym)
    directions = directions_2D_imag_NESW if is_NESW else directions_2D_imag
    if is_sym:
        return [loc + direction for direction in directions if data[loc + direction] == is_sym]
    elif is_not_sym:
        return [loc + direction for direction in directions if data[loc + direction] != is_not_sym]
    return [loc + direction for direction in directions]

def print_2D(data):
    for row in data:
        print(''.join(row))
    return

def print_2D_imag(data, with_marker = None, marker_loc = None):
    if with_marker:
        import copy
        d = copy.deepcopy(data)
        d[marker_loc] = with_marker
    else:
        d = data
    x_size, y_size = size_2D_imag(d)
    for y in range(y_size):
        for x in range(x_size):
            print(d[x + y * 1j], end = '')
        print()
    return

def size_2D(data):
    return (len(data[0]), len(data))

def size_2D_imag(data):
    x = max([int(imag.real) for imag in data.keys()]) + 1
    return (x, int(len(data) / x))

def slice_2D_imag(x_start, x_stop, y_start, y_stop, data):
    return {loc - (x_start + y_start * 1j): sym for loc, sym in data.items() if x_start <= loc.real and loc.real < x_stop and y_start <= loc.imag and loc.imag < y_stop}
