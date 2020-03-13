'''
Player class
Base class for humanPlayer, minimaxPlayer, rlPlayer classes
'''
import cFour

class player():
    def __init__(self, color, board):
        self.color = color
        self.board = board

    def put(self, column):
        return board.put(self.color, column)