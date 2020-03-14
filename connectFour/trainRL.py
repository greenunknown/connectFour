import rl
import cFour
import numpy


def saverewards:
    with open('rewards.txt', 'w') as f:


def saveTable(q):
    with open('qtable.txt' 'w') as f:


def main():
    c4 = cFour.cFour()
    rlplayer = rl.rl('black', c4)
    q, g1r, g2r = rlplayer.qLearningInit()
    print('Winner is: ' + winner)

main()