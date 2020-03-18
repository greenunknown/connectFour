import random
from datetime import datetime
import numpy as np
import cFour
import itertools
from collections import defaultdict

random.seed(datetime.now())


def epsilonGreedy(q, epsilon, state):
    threshold = 1 - epsilon
    i = random.random()
    if i < threshold:
        return np.argmax(q[state])
    return random.randint(0, 6)


def copyQ(q, actionSpace):
    newq = defaultdict(lambda: np.zeros(actionSpace))
    for item in q.items():
        newq[item[0]] = np.copy(item[1])
    return newq

def loadQTable(fileName, color):
    with open(fileName) as f_obj:
        lines = f_obj.readlines()
    index = 0
    qtable = defaultdict(lambda: np.zeros(7))
    while index < len(lines):
        state = lines[index][:len(lines[index]) - 1]
        values = lines[index + 1][:len(lines[index + 1]) - 1]
        '''
        parse values to get numbers
        '''
        fvalues = []
        value = ''
        for c in values:
            if c == ' ':
                fvalues.append(float(value))
                value = ''
                continue
            value += c

        for i in range(len(qtable[state])):
            qtable[state][i] += fvalues[i]
        print(qtable[state])
        print(fvalues)
        index += 2
    return rl(color, cFour.cFour(), qtable)

def dataCalc(fileName):
    return
class rl():
    def __init__(self, color, board, q=None):
        self.color = color
        self.board = board
        self.actionSpace = 7  # action space is 7 (can place is piece in any of 7 columns
        self.q = q
        self.episodeRewards = None

    def stateReward(self, q, state, player, c4, eta, gamma, epsilon):
        nextState = state
        r = 0
        while nextState == state:
            if epsilon <= 0.0:
                action = np.argmax(q[state])
            else:
                action = epsilonGreedy(q, epsilon, state)
            nextState, reward, done = c4.step(player, action)
            r = reward
            if action == np.argmax(q[state]) and nextState == state:
                action = epsilonGreedy(q, 0.1, state)
                nextState, reward, done = c4.step(player, action)
        return nextState, r, action, done

    def qLearningInit(self, episodes=100000, eta=0.5, gamma=0.9, epsilon=0.1):
        q = defaultdict(lambda: np.zeros(self.actionSpace))
        #q2 = defaultdict(lambda: np.zeros(self.actionSpace))
        player2 = None
        if self.color == 'black':
            player2 = 'red'
        else:
            player2 = 'black'
        g1rewards = np.zeros(episodes)
        g2rewards = np.zeros(episodes)
        #p2Rewards = np.zeros(episodes)
        g1 = self.board
        g2 = cFour.cFour()
        #self.board = c4
        #player2.board = c4
        #get initial state
        g1state = g1.state()
        g2state = g2.state()
        g1done = 'not full'
        g1rDone = 'not full'
        g2done = 'not full'
        g2rDone = 'not full'
        for t in itertools.count():
            if g1done == 'not full' and g1rDone == 'not full':
                g1tempnextState, g1reward, g1action, g1done = self.stateReward(q, g1state, self.color, g1, eta, gamma, epsilon)
                g1nextState, g1r, g1rDone = g1.step(player2, random.randint(0,6))
                while g1nextState == g1tempnextState:#prevent same state assignment
                    g1nextState, g1r, g1rDone = g1.step(player2, random.randint(0,6))
                if g1done == self.color:
                    g1reward += 50
                if g1done == 'full' or g2rDone == 'full':
                    g1reward += 10
                if g1rDone == player2:
                    g1reward -= 50
                g1rewards[0] += g1reward
                g1nextAction = np.argmax(q[g1nextState])
                value = eta * (g1reward + (gamma * q[g1nextState][g1nextAction]) - q[g1state][g1action])
                q[g1state][g1action] += value
                g1state = g1nextState
                continue
            if g2done == 'not full' and g1rDone == 'not full':
                g2nextState, g2r, g2rDone = g2.step('black', random.randint(0,6))
                while g2nextState == g2state:  # prevent same state assignment
                    g2nextState, g2r, g2rDone = g2.step('black', random.randint(0,6))
                g2nextState, g2reward, g2action, g2done = self.stateReward(q, g2state, 'red', g2, eta, gamma, epsilon)
                if g2done == 'red':
                    g2reward += 50
                if g2done == 'full' or g2rDone == 'full':
                    g2reward += 10
                if g2rDone == 'black':
                    g2reward -= 50
                g2rewards[0] += g2reward
                g2nextAction = np.argmax(q[g2nextState])
                value = eta * (g2reward + (gamma * q[g2nextState][g2nextAction]) - q[g2state][g2action])
                q[g2state][g2action] += value
                g2state = g2nextState
                continue
            self.q = q
            break
        return self.qLearning(player2, episodes - 1, g1rewards, g2rewards, eta, gamma, epsilon)

    def qLearning(self, player2, episodes, g1episodeRewards, g2episodeRewards, eta, gamma, epsilon):
        p1q = copyQ(self.q, self.actionSpace)
        p2q = defaultdict(lambda: np.zeros(self.actionSpace))
        for e in range(1, episodes):
            g1 = cFour.cFour()
            g2 = cFour.cFour()
            self.board = g1
            g1state = g1.state()
            g2state = g2.state()
            g1done = 'not full'
            g1p2done = 'not full'
            g2done = 'not full'
            g2p2done = 'not full'
            for t in itertools.count():
                #print('Training - episode: ' + str(e + 1) + ' step: ' + str(t + 1))
                if g1done == 'not full' and g1p2done == 'not full':
                    g1nextState, g1reward, g1action, g1done = self.stateReward(p1q, g1state, self.color, g1, eta, gamma, epsilon)
                    if g1done == 'not full':
                        g1nextState, g1p2reward, g1p2action, g1p2done = self.stateReward(p2q, g1nextState, player2, g1, eta, gamma, epsilon)
                    if g1done == self.color:
                        g1reward += 50
                    if g1done == 'full' or g1p2done == 'full':
                        g1reward += 10
                    if g1p2done == player2:
                        g1reward -= 50
                    g1episodeRewards[e] += g1reward
                    g1nextAction = np.argmax(p1q[g1nextState])
                    value = eta * (g1reward + (gamma * p1q[g1nextState][g1nextAction]) - p1q[g1state][g1action])
                    p1q[g1state][g1action] += value
                    g1state = g1nextState
                    continue
                if g2done == 'not full' and g2p2done == 'not full':
                    g2nextState, g2p2reward, g2p2action, g2p2done = self.stateReward(p2q, g2state, 'black', g2, eta, gamma, epsilon)
                    if g2done == 'not full':
                        g2nextState, g2reward, g2action, g2done = self.stateReward(p1q, g2nextState, 'red', g2, eta, gamma, epsilon)
                    if g2done == 'red':
                        g2reward += 50
                    if g2done == 'full' or g2p2done == 'full':
                        g2reward += 10
                    if g1p2done == player2:
                        g2reward -= 50
                    g2episodeRewards[e] += g2reward
                    g2nextAction = np.argmax(p1q[g2nextState])
                    value = eta * (g2reward + (gamma * p1q[g2nextState][g2nextAction]) - p1q[g2state][g2action])
                    p1q[g2state][g2action] += value
                    g2state = g2nextState
                    continue
                self.q = p1q
                p2q = copyQ(p1q, self.actionSpace)
                break
            # decrease epsilon
            if (e + 1) % 50 == 0:
                if epsilon > 0:
                    epsilon -= .001
        return self.q, g1episodeRewards, g2episodeRewards

    def testHuman(self, eta=0.2, gamma=0.9, epsilon=0.1):
        q = self.q
        self.board = cFour.cFour()
        c4 = self.board
        state = c4.state()
        for t in itertools.count():
            c4.display()
            whosturn = 'black'
            print(whosturn + '\'s turn')
            nextState, reward, action, done = self.stateReward(q, state, self.color, c4, eta, gamma, epsilon)
            if done != 'not full':
                c4.display()
                winner = done
                break
            c4.display()
            whosturn = 'red'
            print(whosturn + '\' turn')
            p2a = int(input('Enter the column you wish to place a piece in (1-7): '))
            while p2a < 1 or p2a > 7:
                print('Invalid input, try again')
                p2a = int(input('Enter the column you wish to place a piece in (1-7): '))
            nextState, p2r, p2d = c4.step(whosturn, p2a - 1)
            if p2d != 'not full':
                c4.display()
                winner = p2d
                break
            state = nextState
        return winner




            

'''
    def qLearning(episodes, eta, gamma, epsilon):
        #q = defaultdict(lambda: np.zeros(self.actionSpace))
        #q2 = defaultdict(lambda: np.zeros(self.actionSpace))
        player2 = None
        if self.color == 'black':
            player2 = rl('red', None)
        else:
            player2 = rl('black', None)
        rewards = np.zeros(episodes)
        #p2Rewards = np.zeros(episodes)
        for e in range(episodes):
            #reset board
            c4 = cFour.cFour()
            self.board = c4
            player2.board = c4
            #get initial state
            state = cFour.state()
            for t in itertools.count():
                print('Training - episode: ' + str(e + 1) + ' step: ' + str(t + 1))
                #p1state, p1reward, p1action, done = stateReward(q1, state, self.color, eta, gamma, epsilon)
                #p2state, p2reward, p2action, done= stateReward(q2, p1state, player2.color, eta, gamma, epsilon)
                #p1Rewards[e] += p1reward
                #p2Rewards[e] += p2reward
                #p1nextAction = np.argmax(q[p2state])
                #value = eta * (p1reward + (gamme * q[p2state][p1nextAction]) - q[state][p1action])
                #q[state][p1action] += value
                #if done != 'none':
                    #break
                #state = p2state
                nextState, reward, action, done = stateReward(q, state, self.color, eta, gamma, epsilon)
                rewards[e] += reward
                nextState, r, rDone = c4.step(player2, random.randint(0,6))
                nextAction = np.argmax(q[nextState])
                value = eta * (reward + (gamma * q[nextState][nextAction]) - q[state][action])
                q[state][action] += value
                if done != 'none':
                    return done, 
                nextAction = np.argmax(q[nextState])
'''






