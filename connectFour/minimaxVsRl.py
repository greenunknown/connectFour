import cFour
import minimax
import rl
from time import sleep
from os import system, name

def clear():
    if name == 'nt':#if windows
        _ = system('cls')
    else:#max and linux have same clear call
        _ = system('clear')

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

def humanvsrl(bot):
    winners = []
    c4 = bot.board
    print('For this test, the 10 games will be split in two; one set with the AI as player one and one witht eh AI as player two')
    print('First set: AI = player one')
    for game in range(5):
        c4 = cFour.cFour()
        state = c4.state()
        print('Game ' + str(game))
        c4.display()
        while True:
            print('AI turn')
            nextState, reward, action, done = bot.stateReward(bot.q, state, 'black', c4, 0.2, 0.9, 0.1)
            state = nextState
            c4.display()
            if done != 'not full':
                if done == 'full':
                    print('draw')
                    winners.append('draw')
                    break
                print('AI wins')
                winners.append('rl')
                break
            print('Your turn')
            i = 0
            while state == nextState:
                while i < 1 or i > 7:
                    i = int(input('Enter a column number (1-7) to place a piece: '))
                    if i < 1 or i > 7:
                        print('Out of bounds column! Try again')
                nextState, r, done = c4.step('red', i - 1)
                if nextState == state:
                    print('Sorry, that column is full, try again')
            state = nextState
            if done != 'not full':
                if done == 'full':
                    print('draw')
                    winners.append('draw')
                    break
                print('You win')
                winners.append('player')
                break
    print('Second set: AI = player two')
    bot.color = 'red'
    for game in range(5):
        c4 = cFour.cFour()
        state = c4.state()
        print('Game ' + str(game))
        c4.display()
        while True:
            print('Your turn')
            i = 0
            nextState = state
            while state == nextState:
                while i < 1 or i > 7:
                    i = int(input('Enter a column number (1-7) to place a piece: '))
                    if i < 1 or i > 7:
                        print('Out of bounds column! Try again')
                nextState, r, done = c4.step('black', i - 1)
                if nextState == state:
                    print('Sorry, that column is full, try again')
            state = nextState
            c4.display()
            if done != 'not full':
                if done == 'full':
                    print('draw')
                    winners.append('draw')
                    break
                print('You win')
                winners.append('player')
                break
            print('AI turn')
            nextState, reward, action, done = bot.stateReward(bot.q, state, 'red', c4, 0.2, 0.9, 0.1)
            state = nextState
            c4.display()
            if done != 'not full':
                if done == 'full':
                    print('draw')
                    winners.append('draw')
                    break
                print('AI wins')
                winners.append('rl')
                break
    return winners

def humanvsmini():
    winners = []
    print('For this test, the 10 games will be split in two; one set with the AI as player one and one with the AI as player two')
    print('First set: AI = player one')
    for games in range(5):
        game = minimax.MinimaxConnectFour()
        game.display()
        print('Game: ' + str(games))
        while not game.full():
            print('AI turn')
            bestMove = game.findBestMove(game.players[0], game.players[1])
            xy = game.place(game.players[0], bestMove)
            if xy[0] == -1:
                continue
            game.display()
            if game.win(xy[0], xy[1]) == game.players[0]:
                print('AI wins')
                winners.append('minimax')
                break
            print('Your turn')
            xy = [-1, -1]
            while xy[0] == -1:
                i = int(input('Enter a column number (1-7) to place a piece: '))
                xy = game.place(game.players[1], i - 1)
                if xy[0] == -1:
                    print('That column is full, try again')
            game.display()
            if game.win(xy[0],xy[1]) == game.players[1]:
                print('You win')
                winners.append('player')
                break
            if game.full():
                print('draw')
                winners.append('draw')
                break
    print('Second set: AI = player two')
    for games in range(5):
        game = minimax.MinimaxConnectFour()
        game.display()
        print('Game: ' + str(games))
        while not game.full():
            print('Your turn')
            i = int(input('Enter a column number (1-7) to place a piece: '))
            xy = game.place(game.players[0], i - 1)
            if xy[0] == -1:
                print('That column is full, try again')
                continue
            game.display()
            if game.win(xy[0], xy[1]) == game.players[0]:
                print('You win')
                winners.append('player')
                break
            xy = [-1, -1]
            print('AI turn')
            while xy[0] == -1:
                bestMove = game.findBestMove(game.players[1], game.players[0])
                xy = game.place(game.players[1], bestMove)
            game.display()
            if game.win(xy[0], xy[1]) == game.players[1]:
                print('AI wins')
                winenrs.append('minimax')
                break
            if game.full():
                print('draw')
                winners.append('draw')
                break
    return winners

def save(fileName, data):
    with open(fileName, 'w') as f:
        for d in data:
            f.write(d + '\n')
    return

def main():
    rlbot = rl.loadQTable('qtable.txt', 'black')
    while True:
        clear()
        print('--------MINIMAX--VS--RL--------')
        print('Test No.        Test Name')
        print('      0.        Exit Program')
        print('      1.        Minimax vs Minimax')
        print('      2.        Rl vs RL')
        print('      3.        Human vs Minimax')
        print('      4.        Human vs RL')
        #print('      5.        Minimax vs RL') maybe if time
        i = int(input('Enter the number for the test you wish to perform: '))
        data = []
        fileName = ''
        if i == 0:
            print('Good day!')
            return
        elif i == 1:
            fileName = 'minivsmini.txt'
            data = minivsmini()
        elif i == 2:
            fileName = 'rlvsrl.txt'
            data = rlvsrl(rlbot)
        elif i == 3:
            fileName = 'humanvsmini.txt'
            data = humanvsmini()
        elif i == 4:
            fileName = 'humanvsrl.txt'
            data = humanvsrl(rlbot)
        else:
            print('Invalid input, try again')
            continue
        save(fileName, data)
        s = input('Would you like to do another test? (y/n): ')
        if s == 'y' or s == 'Y':
            continue
        elif s == 'n' or s == 'N':
            print('Good day!')
            return
        else:
            print('Invalid input, exiting program')
            return

main()
exit(1)