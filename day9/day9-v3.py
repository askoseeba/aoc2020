#
# Load the data
#

#fname, preamble_len = 'test-input.txt', 5 # Test data
fname, preamble_len = 'input.txt', 25     # Production data

with open(fname) as f:
    data = [int(line) for line in f.read()[:-1].split('\n')]


#
# Part 1 as oneliner, reduced speed loss (3 times slower than v1, (v2 is about 10x slower)
#

import itertools

num = next(data[i] for i in range(preamble_len, len(data)) if data[i] not in {w1 + w2 for w1, w2 in itertools.combinations(data[i - preamble_len:i], 2)})

print('Part 1: %d ' % num)

#
# Part 2 as oneliner, no speed loss compared to v1
#

print('Part 2: %d' % next(filter(lambda l: len(l) == 1, ([min(data[cs_start : cs_start + cs_len]) + max(data[cs_start : cs_start + cs_len]) for cs_start in range(len(data) - 2) if sum(data[cs_start : cs_start + cs_len]) == num] for cs_len in range(2, len(data)))))[0])
