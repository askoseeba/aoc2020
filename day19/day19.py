#
# Load the data
#

# Test data:
fname = 'test-input.txt'
fname = 'test2-input.txt'

# Production data:
fname = 'input.txt'

import aocutils as aoc

rulesdata, messages = (section.split('\n') for section in aoc.load_1D(fname, sep = '\n\n'))
rules = {}
for rule in rulesdata:
    id, subrules = rule.split(': ')
    rules[id] = subrules[1] if subrules[1].isalpha() else [option.split(' ') for option in subrules.split(' | ')]


#
# Part 1
#

def check_option(rules, option, message, orule_idx = 0):
    #print('Check options:', option, message, orule_idx)
    rule_results = check_rule(rules, option[orule_idx], message)
    if orule_idx == len(option) - 1:
        return rule_results
    results = []
    for rr in rule_results:
        oresults = check_option(rules, option, rr, orule_idx + 1)
        if oresults:
            results += oresults
    return results

def check_rule(rules, rule, message):
    if rule == '29' and message == '':
        print('Check rule:', rule, message, rules[rule])
    if message == '':
        return []
    if type(rules[rule]) != list:
        if rules[rule] == message[0]:
            return [message[1:]]
        else:
            return []
    results = []
    for option in rules[rule]:
        option_results = check_option(rules, option, message)
        if '' in option_results:
            return ['']
        results += option_results
    return results

print('Part 1:', len([result for result in [check_rule(rules, '0', message) for message in messages] if '' in result]))


#
# Part 2
#

import copy

rules2 = copy.deepcopy(rules)
rules2['8']  = [['42']      , ['42', '8']       ]
rules2['11'] = [['42', '31'], ['42', '11', '31']]
print('Part 1:', len([result for result in [check_rule(rules2, '0', message) for message in messages] if '' in result]))
