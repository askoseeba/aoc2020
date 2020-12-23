#
# The data
#

#input_data = '389125467' # Test data. Part 1: after 10 steps: 92658374; after 100 steps: 67384529
input_data = '469217538' # Production data

data = [int(cup) for cup in list(input_data)]


#
# Part 1
#

import copy

def select_destination(current, cups, removed_cups):
    destination = current - 1
    while True:
        if destination < min(cups):
            return max(cups)
        if destination in removed_cups:
            destination -= 1
            continue
        return destination

i0 = 0
cups     = copy.deepcopy(data)
num_cups = len(cups)

for move in range(1, 101):
    current      = cups[i0]
    i1, i2, i3   = (i0 + 1) % num_cups, (i0 + 2) % num_cups, (i0 + 3) % num_cups
    removed_cups = [cups[i1], cups[i2], cups[i3]]
    del cups[i1]
    del cups[i1 if i1 < len(cups) else 0]
    del cups[i1 if i1 < len(cups) else 0]
    destination  = select_destination(current, cups, removed_cups)
    dest_index = cups.index(destination)
    cups.insert(dest_index + 1, removed_cups[0])
    cups.insert(dest_index + 2, removed_cups[1])
    cups.insert(dest_index + 3, removed_cups[2])
    i0 = (cups.index(current) + 1) % num_cups

print('Part 1:', ''.join(['%d' % cups[(i + cups.index(1) + 1) % len(cups)] for i in range(len(cups) - 1)]))


#
# Part 2
#

data2 = data + list(range(10, 1000001))
cups = {cup: data2[(i + 1) % len(data2)] for i, cup in enumerate(data2)}

def select_destination(current, removed_cups, min_cup, max_cup):
    destination = current - 1
    while True:
        if destination < min_cup_adjusted(removed_cups, min_cup):
            return max_cup_adjusted(removed_cups, max_cup)
        if destination in removed_cups:
            destination -= 1
            continue
        return destination
def min_cup_adjusted(removed_cups, min_cup):
    mc = min_cup
    while mc in removed_cups:
        mc += 1
    return mc
def max_cup_adjusted(removed_cups, max_cup):
    mc = max_cup
    while mc in removed_cups:
        mc -= 1
    return mc

def cups_to_list(cups, cup, num_cups = None):
    ret = []
    ptr = cup
    for i in range(len(cups)):
        ret.append(cups[ptr])
        ptr = cups[ptr]
        if num_cups and i + 1 == num_cups:
            return ret
        #print(ret, ptr)
    return ret
        
min_cup  = min(data)
max_cup  = len(data)
current  = data2[0]
for move in range(1, 10000001):
    destination = select_destination(current, [cups[current], cups[cups[current]], cups[cups[cups[current]]]], min_cup, max_cup)
    moved_cups_start                   = cups[current]
    cups[current]                      = cups[cups[cups[cups[current]]]]
    cups[cups[cups[moved_cups_start]]] = cups[destination]
    cups[destination]                  = moved_cups_start
    current                            = cups[current]
    if move % 1000000 == 0:
        print('%d moves passed.' % move)

print('Part 2:', cups[1] * cups[cups[1]])
