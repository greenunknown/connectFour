import cFour
import rl
import numpy
from collections import defaultdict

def main():
    player = rl.loadQTable('qtable.txt', 'black')
    winner = player.testHuman()
    print('The winner is ' + winner)

main()