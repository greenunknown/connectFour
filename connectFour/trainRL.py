import rl
import cFour
import numpy
from collections import defaultdict


def saverewards(rewards1, rewards2):
    with open('rewards1.txt', 'w') as f:
        for r in rewards1:
            f.write(str(int(r)) + '\n')
    with open('rewards2.txt', 'w') as f:
        for r in rewards2:
            f.write(str(int(r)) + '\n')


def saveTable(q):
    with open('qtable.txt', 'w') as f:
        for item in q.items():
            f.write(item[0] + '\n')
            for i in item[1]:
                f.write(str(i) + ' ')
            f.write('\n')

def main():
    print('training')
    c4 = cFour.cFour()
    rlplayer = rl.rl('black', c4)
    q, g1r, g2r = rlplayer.qLearningInit()
    saverewards(g1r, g2r)
    saveTable(q)
    #winner = rlplayer.testHuman()
    #print('Winner is: ' + winner)

main()