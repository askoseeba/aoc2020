#fname = 'test-input.txt'  # Test data
fname = 'test2-input.txt' # Test data, part 2
fname = 'input.txt'       # Test data

import aocutils as aoc
import math

data = aoc.load_1D(fname, sep = '\n\n')
fields             = {field[:field.index(':')]: set.union(*[(lambda start, stop: set(range(start, stop + 1)))(*[int(num) for num in rng.split('-')])
                                                            for rng in field[field.index(':') + 2:].split(' or ')])
                      for field in data[0].split('\n')}
my_ticket, tickets = [[[int(num) for num in line.split(',')] for line in section.split('\n')[1:]] for section in data[1:]]
my_ticket          = my_ticket[0]


#
# Part 1
#

all_fields_values = set().union(*fields.values())
print('Part 1:', sum(v for ticket in tickets for v in ticket if v not in all_fields_values))


#
# Part 2
#

valid_tickets     = [ticket for ticket in tickets if not any(v not in set().union(*fields.values()) for v in ticket)]
col_field_matches = {i: {fname for fname, fvalues in fields.items() if {ticket[i] for ticket in valid_tickets}.issubset(fvalues)} for i in range(len(fields))}

final_columns = {}
while True:
    single_match_cols = {col: next(iter(fnames)) for col, fnames in col_field_matches.items() if len(fnames) == 1}
    assert(single_match_cols)
    final_columns     = {**final_columns, **single_match_cols}
    for smc in single_match_cols:
        for col, fnames in col_field_matches.items():
            if single_match_cols[smc] in fnames:
                col_field_matches[col].remove(single_match_cols[smc])
        col_field_matches = {k: v for k, v in col_field_matches.items() if v}
    if not col_field_matches:
        break

print('Part 2:', math.prod([my_ticket[i] for i, fname in final_columns.items() if fname[:9] == 'departure']))
