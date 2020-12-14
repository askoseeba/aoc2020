#
# Load the data
#

fname = 'test-input.txt'  # Test data
fname = 'test2-input.txt' # Test data, part 2

fname = 'input.txt'      # Production data

import aocutils as aoc

data = [line.split(' = ') for line in aoc.load_1D(fname)]


#
# Part 1
#

def cmd_mask(mask_str):
    return [(len(mask_str) - i, int(mask_str[i])) for i in range(len(mask_str)) if mask_str[i] != 'X']

#                   123456789012345678901234567890123456
neg_bit_mask = int('111111111111111111111111111111111111', 2)
def cmd_setmem(addr_str, value_str, mask, mem):
    global neg_bit_mask
    addr      = int(addr_str.split('[')[1][:-1])
    mem[addr] = int(value_str)
    for bit in mask:
        bitval = 1 << bit[0] - 1
        if bit[1]: # Positive bit
            mem[addr] |= bitval
        else:      # Negative bit
            mem[addr] &= (neg_bit_mask ^ bitval)
    return mem

def run(data):
    mask = []
    mem = {}
    for cmd in data:
        if cmd[0] == 'mask':
            mask = cmd_mask(cmd[1])
        else:
            mem = cmd_setmem(cmd[0], cmd[1], mask, mem)
    return mem

print('Part 1:', sum(run(data)))


#
# Part 1
#

def cmd_mask(mask_str):
    return [(len(mask_str) - i, mask_str[i]) for i in range(len(mask_str)) if mask_str[i] != '0']

def xbitvals(i):
    xpos = 1 << i - 1
    xneg = neg_bit_mask ^ xpos
    return xneg, xpos

def cmd_setmem(addr_str, value_str, mask, mem):
    global neg_bit_mask
    addr = int(addr_str.split('[')[1][:-1])
    for bit in [(i, bit) for i, bit in mask if bit == '1']:
        addr = addr | (1 << bit[0] - 1)
    xbits = [xbitvals(i) for i, bit in mask if bit == 'X']
    meta_bits = ''.join(['1' for i in range(len(xbits))]) # Introducing the concept of meta-bit to indicate the value selected for an x-bit when running the combinations
    for i in range(int(meta_bits, 2) + 1): # Running the combinations across possible X-bit values
        new_addr = addr
        for j in range(len(xbits)):
            state = bool(i & (1 << j))
            xbit  = xbits[j][bool(i & (1 << j))]
            if state: # Positive bit
                new_addr |= xbit
            else:     # Negative bit
                new_addr &= ~(neg_bit_mask ^ xbit)
        mem[new_addr] = int(value_str)
    return mem
    
mem = run(data)

print('Part 1:', sum(run(data).values()))
