#
# Load the Data
#

# Test data
#fname = 'test-input.txt'
#fname = 'test2-input.txt'

# Production data:
fname = 'input.txt'

import pandas as pd

data = pd.read_csv(fname, header = None)
data = pd.concat([pd.Series([0]), data[0].sort_values(), pd.Series(data[0].max() + 3)]).reset_index()[0]


#
# Part 1 -- exec time: 2 milliseconds
#

print('Part 1: %d' % (data - data.shift()).value_counts().product())


#
# Part 2 -- exec time: 0 nanoseconds
#

counts = {}

def current_adapter(i, data, data_len):
    if i == data_len - 1:
        return 1
    if i in counts: # This turns the impossible brute force into 0 nanoseconds solution.
        return counts[i]
    count = 0
    for idx in range(i + 1, i + 4):
        if idx == data_len:
            break
        if idx < data_len and data[idx] <= data[i] + 3:
            count += current_adapter(idx, data, data_len)
    counts[i] = count # This turns the impossible brute force into 0 nanoseconds solution.
    return count

print('Part 2: %d' % current_adapter(0, list(data), data.shape[0]))
