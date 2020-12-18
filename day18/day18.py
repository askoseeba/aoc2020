#
# Load the data
#

fname = 'test-input.txt' # Test data
fname = 'input.txt'      # Production data

import aocutils as aoc

data = aoc.load_1D(fname)


#
# Part 1
#

def compute(expr):
    left    = expr[0] if type(expr[0]) != tuple else compute(expr[0])
    right   = expr[2] if type(expr[2]) != tuple else compute(expr[2])
    reduced = left + right if expr[1] == '+' else left * right
    return compute((reduced, *expr[3:])) if len(expr) > 3 else reduced

expression_trees = [eval(''.join([("'%s'" % sym) if sym in {'+', '*'} else sym for sym in expr.replace(' ', ',')])) for expr in data]
print('Part 1:', sum([compute(expr) for expr in expression_trees]))


#
# Part 2
#

class WeirdInt:
    def __init__(self, num):
        self.num = num
    def __add__(self, other):
        return WeirdInt(self.num * other.num)
    def __mul__(self, other):
        return WeirdInt(self.num + other.num)

data_op_swapped = [expr.replace('*', '.').replace('+', '*').replace('.', '+') for expr in data]
print('Part 2:', sum([eval(''.join([('WeirdInt(%s)' % sym) if sym.isdigit() else sym for sym in expr])).num for expr in data_op_swapped]))
