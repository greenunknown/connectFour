class cFour():
    def __init__(self):
        self.grid = []
        for i in range(6):
            row = []
            for j in range(7):
                row.append('O')
            self.grid.append(row)
        self.score = {'Red': 0, 'Black': 0, 'Winner': ''}
        self.amounts = [0,0,0,0,0,0,0]

    def put(self, player, column):
        if self.amounts[column] == 6:
            return 0
        if player == 'black':
            self.grid[5 - self.amounts[column]][column] = 'B'
        elif player == 'red':
            self.grid[5 - self.amounts[column]][column] = 'R'
        else:
            print('error: invalid player code')
            return -1
        self.amounts[column] += 1
        return 1

    def display(self):
        for i in range(6):
            for j in range(7):
                print(self.grid[i][j], end = ' ')
            print()
        return

    def win(self):
        for i in range(6):
            for j in range(7):
                if self.grid[i][j] == 'B':
                    w = self.checkRC(i, j, 'B')
                    if w == True:
                        return 'Black'
                    w = self.checkDiag(i, j, 'B')
                    if w == True:
                        return 'Black'
                elif self.grid[i][j] == 'R':
                    w = self.checkRC(i, j, 'R')
                    if w == True:
                        return 'Red'
                    w = self.checkDiag(i, j, 'R')
                    if w == True:
                        return 'Red'
                else:
                    continue
        return None

    def checkRC(self, i, j, player):
        inRow = 0
        for column in range(7):
            if self.grid[i][column] == player:
                inRow += 1
            else:
                inRow = 0
            if inRow >= 4:
                return True
        inColumn = 0
        for row in range(6):
            if self.grid[row][j] == player:
                inColumn += 1
            else:
                inColumn = 0
            if inColumn >= 4:
                return True
        return False

    def checkDiag(self, i, j, player):
        return False
