import pandas as pd


#
# Load the Data
#

#fname = 'test-input.txt' # Test data
fname = 'input.txt'      # Production data

data = pd.read_csv(fname, header = None)


#
# Part 1
#

data['seat_row'] = data[0].str.slice(0, 7).str.replace('B', '1').str.replace('F', '0').apply(lambda s: int(s, 2))
data['seat_col'] = data[0].str.slice(7)   .str.replace('R', '1').str.replace('L', '0').apply(lambda s: int(s, 2))
print('Part 1: %d' % (data['seat_row'] * 8 + data['seat_col']).max())


#
# Part 2
#

ids = (data['seat_row'] * 8 + data['seat_col']).sort_values()
print('Part 2: %d' % (ids[ids - ids.shift() > 1].iloc[0] - 1))
