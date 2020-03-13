import player
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


class rl(player):
    def __init__(self, color, board):
        super().__init__(color, board)
        self.actionSpace = 7#action space is 7 (can place is piece in any of 7 columns
        self.actionTaken = False

    def place(self, column):
        return super().put(self.color, column)

    def qLearningP1(q, episode, state, eta, gamma, epsilon):
        if epsilon <= 0.0:
            action = np.argmax(q[state])
        else:
            action = epsilonGreedy(q, epsilon, state)
        return


    def qLearningP2(q, episode, state, eta, gamma, epsilon):
        return

    def qLearning(episodes = 10000, eta = 0.2, gamma = 0.9, epsilon = 0.1):
        q = defaultdict(lambda: np.zeros(self.actionSpace))
        player2 = None
        if self.color == 'black':
            player2 = rl('red', None)
        else:
            player2 = rl('black', None)
        episodeRewards = np.zeros(episodes)
        for e in range(episodes):
            #reset board
            c4 = cFour.cFour()
            self.board = c4
            player2.board = c4
            #get initial state
            state = cFour.state()
            for t in itertools.count():
                print('Training - episode: ' + str(e + 2) + ' step: ' + str(t + 1))
                if epsilon <= 0.0:#greedy choice
                    action = np.argmax(q[state])
                else:#use policy
                    action = epsilonGreedy(q, epsilon, state)
                #take action
                nextState = State
                while nextState == State:
                    nextState, reward, done = c4.step(self.color, action)
                    episodeRewards[e] += reward

                nextAction = np.argmax(q[nextState])






