import numpy as np

# Test case
#data = [1721, 979, 366, 299, 675, 1456]

# Production data
data = np.genfromtxt('input.txt')

found = False
for i in range(len(data) - 2):
    for j in range(i + 1, len(data) - 1):
        for k in range(j + 1, len(data)):
            if data[i] + data[j] + data[k] == 2020:
                found = True
                break
        if found:
            break
    if found:
        break
        
print(data[i], data[j], data[k], data[i] * data[j] * data[k])
