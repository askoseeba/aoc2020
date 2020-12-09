#
# Load the data
#

#fname, preamble_len = 'test-input.txt', 5 # Test data
fname, preamble_len = 'input.txt', 25     # Production data

with open(fname) as f:
    data = [int(line) for line in f.read()[:-1].split('\n')]


#
# Part 1 as oneliner, 10 times slower, though.
#

import itertools

num = [data[i] for i in range(preamble_len, len(data)) if data[i] not in {w1 + w2 for w1, w2 in itertools.combinations(data[i - preamble_len:i], 2)}][0]

print('Part 1: %d ' % num)

#
# Part 2, more compact, no speed impact
#

cs_len = 2
while True:
    cs = [data[cs_start : cs_start + cs_len] for cs_start in range(len(data) - cs_len + 1) if sum(data[cs_start : cs_start + cs_len]) == num]
    if len(cs) > 0:
        break
    cs_len += 1
    
print('Part 2: %d' % (min(cs[0]) + max(cs[0])))