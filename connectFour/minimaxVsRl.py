import cFour
import minimax
import rl
from time import sleep

def minivsmini():
    winners = []
    for games in range(10):
        game = minimax.MinimaxConnectFour()
        print('Game ' + str(games))
        game.display()
        while not game.full():
            print('black\'s turn')
            bestMove = game.findBestMove(game.players[0], game.players[1])
            xy = game.place(game.players[0], bestMove)
            game.display()
            print('\n')
            if game.win(xy[0], xy[1]) == game.players[0]:
                winners.append('black')
                break
            print('red\'s turn')
            bestMove = game.findBestMove(game.players[1], game.players[0])
            xy = game.place(game.players[1], bestMove)
            game.display()
            print('\n')
            if game.win(xy[0], xy[1]) == game.players[1]:
                winners.append('red')
                break
            if game.full():
                print('draw')
                winners.append('draw')
                break
    return winners

def rlvsrl(bot):
    winners = []
    c4 = bot.board
    for game in range(10):
        c4 = cFour.cFour()
        state = c4.state()
        print('Game ' + str(game))
        c4.display()
        while True:
            print('black\'s turn')
            nextState, reward, action, done = bot.stateReward(bot.q, state, 'black', c4, 0.2, 0.9, 0.1)
            state = nextState
            c4.display()
            if done != 'not full':
                if done == 'full':
                    print('draw')
                    winners.append('draw')
                    break
                print('black wins')
                winners.append('black')
                break
            print('red\'s turn')
            nextState, reward, action, done = bot.stateReward(bot.q, state, 'red', c4, 0.2, 0.9, 0.1)
            state = nextState
            c4.display()
            if done != 'not full':
                if done == 'full':
                    print('draw')
                    winners.append('draw')
                    break
                print('red wins')
                winners.append('red')
                break
    return winners

def humanvsrl(rlbot):
    winners = []
    return

def humanvsmini():
    winners = []
    return

def save(fileName, data):
    winners = []
    return

def main():
    data = minivsmini()
    print(data)
    sleep(5)
    save('minivsmini.txt', data)
    rlbot = rl.loadQTable('qtable.txt', 'black')
    data = rlvsrl(rlbot)
    print(data)
    sleep(5)
    save('rlvsrl.txt', data)
    data = humanvsrl(rlbot)
    print(data)
    sleep(5)
    save('humanvsrl.txt', data)
    data = humanvsmini()
    print(data)
    sleep(5)
    save('humanvsmini.txt', data)

main()