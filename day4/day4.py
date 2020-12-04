import pandas as pd
import re

#
# Load the Data
#

#fname = 'test-input.txt'         # Test data (part 1)
#fname = 'test-invalid-input.txt' # Test data (part 2)
#fname = 'test-valid-input.txt'   # Test data (part 2)

fname = 'input.txt'              # Production data

with open(fname) as f:
    data = pd.DataFrame([dict([item.split(':') for item in re.split(r'[ \n]', line)]) for line in f.read()[:-1].split('\n\n')])

#
# Part 1
#

print('Part 1: %d' %(data.drop('cid', axis = 1).isna().sum(axis = 1) == 0).sum())

#
# Part 2
#

import numpy as np

data2 = data.loc[data.drop('cid', axis = 1).isna().sum(axis = 1) == 0, :].copy(deep = True)

data2[['hgt_value', 'hgt_unit']] = data2['hgt'].str.extract(r'(\d+)(.*)')
data2[['iyr', 'eyr', 'byr', 'hgt_value']] = data2[['iyr', 'eyr', 'byr', 'hgt_value']].astype(int, errors='ignore')

print('Part 2: %d' %
    data2[  (1920 <= data2['byr'])       & (data2['byr']       <= 2002)                                 &
            (2010 <= data2['iyr'])       & (data2['iyr']       <= 2020)                                 &
            (2020 <= data2['eyr'])       & (data2['eyr']       <= 2030)                                 &
          ((( 150 <= data2['hgt_value']) & (data2['hgt_value'] <= 193)  & (data2['hgt_unit'] == 'cm')) |
           ((  59 <= data2['hgt_value']) & (data2['hgt_value'] <=  76)  & (data2['hgt_unit'] == 'in'))) &
          data2['hcl'].str.match(r'#[0-9a-f]{6}')                                                       &
          data2['ecl'].isin({'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'})                          &
          data2['pid'].str.match(r'^\d{9}$')
         ].shape[0]
)
