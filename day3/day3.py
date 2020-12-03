import numpy as np

# Test data:
with open('test-input.txt') as f:
    data = np.array([list(line) for line in f.read().split('\n')[:-1]])

# Production data:
with open('input.txt') as f:
    data = np.array([list(line) for line in f.read().split('\n')[:-1]])
    
#
# Part 1
#

needed_hor = (data.shape[0] - 1) * 3 + 1
trees      = np.concatenate([data for i in range(int(needed_hor / data.shape[1]) + 1)], axis = 1)
hor_idx    = [3 * i for i in range(data.shape[0])]
vert_idx   = list(range(data.shape[0]))

print('Part 1: %d' % np.sum(trees[vert_idx, hor_idx] == '#'))

#
# Part 2
#

slopes = [
    {'hor': 1, 'vert': 1},
    {'hor': 3, 'vert': 1},
    {'hor': 5, 'vert': 1},
    {'hor': 7, 'vert': 1},
    {'hor': 1, 'vert': 2}
]

slope_trees = []
for slope in slopes:
    needed_hor = int((data.shape[0] - 1) * slope['hor'] / slope['vert']) + 1
    trees      = np.concatenate([data for i in range(int(needed_hor / data.shape[1]) + 1)], axis = 1)
    hor_idx    = [slope['hor']  * i for i in range(int(data.shape[0] / slope['vert']))]
    vert_idx   = [slope['vert'] * i for i in range(int(data.shape[0] / slope['vert']))]
    slope_trees.append(np.sum(trees[vert_idx, hor_idx] == '#'))

print('Part 3: %d' % np.prod(slope_trees, dtype = np.int64))
