#
# Load the Data
#

#fname = 'test-input.txt'       # Test data
#fname = 'test-input-part2.txt' # Test data, part 2
fname = 'input.txt'            # Production data

with open(fname) as f:
    data = [{'cmd': line[:3], 'param': int(line[4:])} for line in f.read()[:-1].split('\n')]


#
# Part 1
#

accumulator = 0
address     = 0
been_there  = set()

def command_acc(address, param):
    global accumulator
    
    accumulator += param
    return address + 1

def command_jmp(address, param):
    return address + param

def command_nop(address, param):
    return address + 1

command = {
    'acc': command_acc,
    'jmp': command_jmp,
    'nop': command_nop
}

while True:
    if address in been_there:
        break
    been_there.add(address)
    address = command[data[address]['cmd']](address, data[address]['param'])
    
been_there, address, accumulator
print('Part 1: %d' % accumulator)


#
# Part 2
#

def run(data):
    global accumulator
    
    accumulator = 0
    address     = 0
    been_there  = set()
    while True:
        if address in been_there:
            break
        been_there.add(address)
        if address == len(data):
            break
        address = command[data[address]['cmd']](address, data[address]['param'])
    
    return {'address': address, 'accumulator': accumulator}

import copy
import pandas as pd

df          = pd.DataFrame(data)
failed_runs = 0
for idx, line in df[df['cmd'].isin({'nop', 'jmp'})].iterrows():
    data_patched = copy.deepcopy(data)
    if data_patched[idx]['cmd'] == 'jmp':
        data_patched[idx]['cmd'] = 'nop'
    elif data_patched[idx]['cmd'] == 'nop':
        data_patched[idx]['cmd'] = 'jmp'
    result = run(data_patched)
    if result['address'] == len(data_patched):
        break
    failed_runs += 1

print('Part 2: %d (failed runs: %d)' % (result['accumulator'], failed_runs))
