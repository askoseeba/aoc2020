import pandas as pd


#
# Load the Data
#

#fname = 'test-input.txt'       # Test data
#fname = 'test-input-part2.txt' # Test data, part 2
fname = 'input.txt'            # Production data

with open(fname) as f:
    data = f.read().replace(' bags', '').replace(' bag', '').replace('.', '')[:-1].split('\n')
    
rules = []
for rule in data:
    container, contained = rule.split(' contain ')
    for bag in contained.split(', '):
        if bag == 'no other':
            continue
        rules.append({
            'container': container,
            'bag_count': int(bag[0]),
            'bag_type':  bag[2:]
        })
rules = pd.DataFrame(rules)


#
# Part 1
#

containers = {'shiny gold'}

while True:
    new_containers = containers.union(rules[rules['bag_type'].isin(containers)]['container'])
    if new_containers == containers:
        break
    containers = new_containers
        
print('Part 1: %d' % (len(containers) - 1))


#
# Part 2
#

def count_bags(bag, rules):
    count = 1
    for idx, rule in rules[rules['container'] == bag['bag_type']].iterrows():
        count += count_bags(rule, rules)
    return count * bag['bag_count']

print('Part 2: %d' % (count_bags({'bag_type': 'shiny gold', 'bag_count': 1}, rules) - 1))
