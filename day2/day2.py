import numpy as np

# Test data:
data = np.fromregex('test-input.txt', r'(\d*)-(\d*) ([a-z]): ([a-z]*)',
                    [('min', np.int64), ('max', np.int64), ('letter', 'S20'), ('password', 'S20')]
                   )

# Production data:
data = np.fromregex('input.txt', r'(\d*)-(\d*) ([a-z]): ([a-z]*)',
                    [('min', np.int64), ('max', np.int64), ('letter', 'S20'), ('password', 'S20')]
                   )

counts = np.char.count(data['password'], data['letter'])
part1 = np.sum((data['min'] <= counts) & (counts <= data['max']))

print('Part 1: %d' % part1)

import pandas as pd

df = pd.DataFrame(data)
df['letter']   = df['letter'].str.decode('utf8')
df['password'] = df['password'].str.decode('utf8')
part2 = df.apply(lambda row:
                 (row['letter'] == row['password'][row['min'] - 1]) !=
                 (row['letter'] == row['password'][row['max'] - 1]),
                 axis = 1).sum()

print('Part 2: %d' % part2)
