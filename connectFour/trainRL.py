import rl
import cFour

def main():
    c4 = cFour.cFour()
    rlplayer = rl.rl('black', c4)
    rlplayer.qLearningInit()
    winner = rlplayer.testHuman()
    print('Winner is: ' + winner)

main()