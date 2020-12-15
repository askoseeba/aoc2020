#data = [0,3,6]         # Test 1 -> 2020th spoken: 436  | 30000000th spoken: 175594
#data = [1,3,2]         # Test 2 -> 2020th spoken: 1    | 30000000th spoken: 2578
#data = [2,1,3]         # Test 3 -> 2020th spoken: 10   | 30000000th spoken: 3544142
#data = [1,2,3]         # Test 4 -> 2020th spoken: 27   | 30000000th spoken: 261214
#data = [2,3,1]         # Test 5 -> 2020th spoken: 78   | 30000000th spoken: 6895259
#data = [3,2,1]         # Test 6 -> 2020th spoken: 438  | 30000000th spoken: 18
#data = [3,1,2]         # Test 7 -> 2020th spoken: 1836 | 30000000th spoken: 362

data = [6,13,1,15,2,0] # Production

def speak(turn, num, memory):
    if num not in memory:
        memory[num] = [turn]
    else:
        memory[num].append(turn)
        if len(memory[num]) == 3:
            memory[num].pop(0)
    return memory

def solve(turns, data):
    last_spoken = data[-1]
    memory      = {num: [data.index(num) + 1] for num in data}
    for turn in range (len(memory) + 1, turns + 1):
        think_num = 0 if len(memory[last_spoken]) == 1 else memory[last_spoken][-1] - memory[last_spoken][-2]
        memory = speak(turn, think_num, memory)
        last_spoken = think_num
    return last_spoken

print('Part 1:', solve(2020, data))
print('Part 2:', solve(30000000, data))
