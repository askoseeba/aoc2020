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

any([not any([w1 + w2 == data[i] for w1, w2 in itertools.combinations(data[i - preamble_len:i], 2)]) for i in range(preamble_len, len(data))])

print('Part 1: %d' % data[i])


#
# Part 2, more compact, almost as fast (about 25% slower)
#

cs_len = 2
while True:
    if any([sum(data[cs_start : cs_start + cs_len]) == data[i] for cs_start in range(len(data) - cs_len + 1)]):
        break
    cs_len += 1
cs = data[cs_start : cs_start + cs_len]

print('Part 2: %d' % (min(cs) + max(cs)))