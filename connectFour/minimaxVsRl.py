import cFour
import minimax
import rl
import sys


def main():
    if len(sys.argv) != 3:
        print('usage: python3 minimaxVsRl.py [player1] [player1]')
        exit(-1)
    c4 = cFour.cFour()
    if sys.argv[1] == 'human':
        player1 = human.human('black', c4)
    elif sys.argv[1] == 'rl':
        player1 = rl.rl('black', c4)
    elif sys.argv[1] == 'minimax':
        player1 = minimax.minimax('black', c4)
    else:
        print('invalid player1 argument')
        exit(-1)
    if sys.argv[2] == 'human':
        player1 = human.human('red', c4)
    elif sys.argv[2] == 'rl':
        player2 = rl.rl('red', c4)
    elif sys.argv[2] == 'minimax':
        player2 = minimax.minimax('red', c4)
    else:
        print('invalid player2 argument')
        exit(-1)
