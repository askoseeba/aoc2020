#
# Load the data:
#

# Test data:
fname = 'test-input.txt'
#fname = 'test2-input.txt'

# Production data
fname = 'input.txt'

import aocutils as aoc

data = [[int(card) for card in player.replace('Player 1:\n', '').replace('Player 2:\n', '').split('\n')] for player in aoc.load_1D(fname, sep = '\n\n')]


#
# Part 1
#

import copy

player1, player2 = copy.deepcopy(data)

while player1 and player2:
    p1, p2 = player1.pop(0), player2.pop(0)
    assert(p1 != p2)
    if p1 > p2:
        player1.append(p1)
        player1.append(p2)
    else:
        player2.append(p2)
        player2.append(p1)

winner = player1 if player1 else player2

print('Player 1 (small crab)              :', player1)
print('Player 2 (me)                      :', player2)
print('The winner                         :', 'small crab' if player1 else 'me')
print("The winning player's score (part 1):", sum([winner[i] * (len(winner) - i) for i in range(len(winner))]))


#
# Part 2
#

def play(player1, player2):
    previous_rounds_p1 = set()
    previous_rounds_p2 = set()
    while player1 and player2:
        p1, p2 = player1.pop(0), player2.pop(0)
        assert(p1 != p2)
        p1_wins, p2_wins = False, False
        if p1 <= len(player1) and p2 <= len(player2):
            player1_sub, player2_sub = copy.deepcopy(player1)[:p1], copy.deepcopy(player2)[:p2]
            global gamecount
            player1_sub, player2_sub = play(player1_sub, player2_sub)
            p1_wins, p2_wins = (True, False) if player1_sub else (False, True)
        else:
            p1_wins, p2_wins = p1 > p2, p2 > p1
        player1, player2 = (player1 + [p1, p2], player2) if p1_wins else (player1, player2 + [p2, p1])
        p1_state, p2_state = frozenset(enumerate(player1)), frozenset(enumerate(player2))
        if p1_state in previous_rounds_p1 or p2_state in previous_rounds_p2:
            return player1, player2
        previous_rounds_p1.add(p1_state)
        previous_rounds_p2.add(p2_state)
    return player1, player2

player1, player2 = play(*copy.deepcopy(data))
winner           = player1 if player1 and not player2 else player2

print('Player 1 (small crab)              :', player1)
print('Player 2 (me)                      :', player2)
print('The winner                         :', 'small crab' if player1 else 'me')
print("The winning player's score (part 2):", sum([winner[i] * (len(winner) - i) for i in range(len(winner))]))
