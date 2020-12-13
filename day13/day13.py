#
# Load the data
#

fname = 'test-input.txt'  # Test data (part 2 timestamp:    1068788)
#fname = 'test2-input.txt' # Test data (part 2 timestamp:       3417)
#fname = 'test3-input.txt' # Test data (part 2 timestamp:     754018)
#fname = 'test4-input.txt' # Test data (part 2 timestamp:     779210)
#fname = 'test5-input.txt' # Test data (part 2 timestamp:    1261476)
#fname = 'test6-input.txt' # Test data (part 2 timestamp: 1202161486)
fname = 'input.txt'       # Production data

import aocutils as aoc

data = aoc.load_1D(fname)
start_from, busids = int(data[0]), data[1].split(',')


#
# Part 1
#

busids_in_service  = [int(id) for id in busids if id != 'x']
next_departures    = [id - start_from % id for id in busids_in_service]
earliest_departure = min(next_departures)
earliest_busid     = busids_in_service[next_departures.index(earliest_departure)]
print('In service:        ', busids_in_service)
print('Next departures:   ', next_departures)
print('Earliest departure:', earliest_departure)
print('Earliest bus ID:   ', earliest_busid)
print('Part 1:            ', earliest_busid * earliest_departure)
print()


#
# Part 2
#

# The implementations of the chinese_reminder and mul_inv functions are copied from here:
# https://fangya.medium.com/chinese-remainder-theorem-with-python-a483de81fbb8
# The idea for using it from AoC 2020 day 13 implementation here:
# https://hastebin.com/userumorow.apache (author: Steve Dremelzen)
# Note, the original source (from the medium post), has a bug in it that caused the
# final answer to be wrong (by marginal amount) -- the solution from hastebin fixes that
# by not allowing floating point number: p=prod/n_i ==fix==> p=prod//n_i
from functools import reduce
def chinese_remainder(n, a):
    sum=0
    prod=reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n,a):
        p=prod//n_i
        sum += a_i* mul_inv(p, n_i)*p
    return sum % prod
def mul_inv(a, b):
    b0= b
    x0, x1= 0,1
    if b== 1: return 1
    while a>1 :
        q=a// b
        a, b= b, a%b
        x0, x1=x1 -q *x0, x0
    if x1<0 : x1+= b0
    return x1


busids_in_service  = [(int(id), busids.index(id)) for id in busids if id != 'x']
# The idea for the need of such array comes from AoC 2020 day 13 implementation here:
# https://hastebin.com/userumorow.apache (author: Steve Dremelzen)
busids_less_offset = [id - idx % id for id, idx in busids_in_service]
print('In service (with offsets):', [busids_in_service])
print('Buss ID-s less offset:    ', busids_less_offset)
print('Part 2:                   ', int(chinese_remainder([id for id, idx in busids_in_service], busids_less_offset)))

# The usage of chinese_reminder gave me correct answer for all the test cases, however, it gave a wrong answer for
# the production data initially. Weird thing is that the wrong answer was the right answer + 56 -- such a small
# error for a 15-digit number -- it took me time befora I became aware of the reason (see the comment above
# regarding the fix).
#
# While I didn't know how to fix the chinese_remainder implementation, I found another cool way to solve the
# puzzle -- I found that other idea from here:
# https://www.reddit.com/r/adventofcode/comments/kc4njx/2020_day_13_solutions/
#
# It is using a call to wolframalpha.com solver. Copy the print-out of the wolframalpha URL to your browser
# address bar, wait a bit for the solution to appear, and read the answer from the "Integer solution:"
# section. the answer is in the form "n = x * m + y" -- the "y" is you answer.

print('Part 2 (WolframAlpha):    ',
      'https://www.wolframalpha.com/input/?i=0+%3D+' + '+%3D+'.join(['((n+%%2B+%d)+mod+%d)' % (idx, id) for id, idx in busids_in_service]))
