#
# Load the data
#

fname = 'test-input.txt' # Test data
fname = 'input.txt'      # Production data

import aocutils as aoc

card_pubkey, door_pubkey = aoc.load_1D(fname, to_int = True)


#
# Part 1
#

def find_loop_size(pubkey):
    mod_val     = 20201227
    subject_num = 7
    value       = 1
    loop_size   = 0
    while value != pubkey:
        value      = (value * subject_num) % mod_val
        loop_size += 1
    return loop_size

def find_encryption_key(loop_size, pubkey):
    mod_val     = 20201227
    subject_num = pubkey
    value       = 1
    for i in range(loop_size):
        value = (value * subject_num) % mod_val
    return value

card_loop_size, door_loop_size = find_loop_size(card_pubkey), find_loop_size(door_pubkey)

print('Part 1:', find_encryption_key(card_loop_size, door_pubkey))
#print('Part 1:', find_encryption_key(door_loop_size, card_pubkey))


#
# Part 2
#

# No part 2, other than you have to have all the 49 stars collected to earn the last one.
