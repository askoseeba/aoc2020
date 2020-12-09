#
# Load the data
#

#fname, preamble_len = 'test-input.txt', 5 # Test data
fname, preamble_len = 'input.txt', 25     # Production data

with open(fname) as f:
    data = [int(line) for line in f.read()[:-1].split('\n')]


#
# Part 1
#

for i in range(preamble_len, len(data)):
    window = data[i - preamble_len:i]
    found = False
    for j in range(preamble_len - 1):
        for k in range(j + 1, preamble_len):
            if window[j] + window[k] == data[i]:
                found = True
                break
        if found:
            break
    if not found:
        break

print('Part 1: %d' % data[i])


#
# Part 2
#

invalid_number = data[i]
cs_len         = 2
found          = False

while True:
    for cs_start in range(len(data) - cs_len + 1):
        if sum(data[cs_start : cs_start + cs_len]) == invalid_number:
            found = True
            break
    if found:
        break
    cs_len += 1
cs = data[cs_start : cs_start + cs_len]
print('Part 2: %d' % (min(cs) + max(cs)))
