#
# Load the Data
#

fname = 'test-input.txt' # Test data
fname = 'input.txt'      # Production data

import aocutils as aoc

data = [(ingr.split(' '), allerg.split(', ')) for ingr, allerg in [line.rstrip(')').split(' (contains ') for line in aoc.load_1D(fname)]]


#
# Part 1
#

ingredients = {ingredient for food in data for ingredient in food[0]}
allergens   = {allergen   for food in data for allergen   in food[1]}
allerg_ingr = set.union(*[set.intersection(*[set(food[0]) for food in data if allergen in food[1]]) for allergen in allergens])
print('Part 1:', sum([len([ingr for food in data if ingr in food[0]]) for ingr in ingredients - allerg_ingr]))


#
# Part 2
#

allerg_ingr_part2 = {allergen: set.intersection(*[set(food[0]) for food in data if allergen in food[1]]) for allergen in allergens}
ingr_allerg       = {}
while True:
    new_found   = {list(ingr)[0]: allerg for allerg, ingr in allerg_ingr_part2.items() if len(ingr) == 1}
    ingr_allerg = {**ingr_allerg, **new_found}
    for ingr in new_found:
        allerg_ingr_part2 = {allerg: ingrs - {ingr} for allerg, ingrs in allerg_ingr_part2.items() if ingr not in ingrs or len(ingrs) > 1}
    if len(allerg_ingr_part2) == 0:
        break

allerg_ingr_final = dict(zip(ingr_allerg.values(), ingr_allerg.keys()))
print('Part 2:', ','.join([allerg_ingr_final[allerg] for allerg in sorted(allerg_ingr_final.keys())]))
