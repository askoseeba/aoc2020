#fname = 'test-input.txt' # Test data
fname = 'input.txt'      # Production data

import numpy as np

#
# Part 1
#

with open(fname) as f:
    print('Part 1: %d' % np.sum([len(set(line.replace('\n', ''))) for line in f.read()[:-1].split('\n\n')]))


#
# Part 2
#

with open(fname) as f:
    print('Part 2: %d' % np.sum([len(set.intersection(*[set(line) for line in group.split('\n')])) for group in f.read()[:-1].split('\n\n')]))
