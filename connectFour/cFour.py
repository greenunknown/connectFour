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
        if column > 6 or column < 0:
            return 0
        if self.amounts[column] == 6:
            return 0
        if player == 'black':
            self.grid[5 - self.amounts[column]][column] = 'B'
        elif player == 'red':
            self.grid[5 - self.amounts[column]][column] = 'R'
        else:
            print('error: invalid player code')
            exit(-1)
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
    '''
    checks diags of piece around origin i, j.
    counts the pieces in each of the diag directions
    and adds them. counting does not include origin piece,
    so + 1 will be added when checking.
    sw + ne + 1
    se + nw + 1
    '''
    def checkDiag(self, i, j, player):
        ne = 0
        nw = 0
        se = 0
        sw = 0
        x = i
        y = j
        #check in order: se -> nw -> sw -> ne
        for count in range(1,4):
            #check se
            if i + count < 6 and j + count < 7:
                if self.grid[i + count][j + count] == player:
                    se += 1
            #check nw
            if i - count >= 0 and j - count >= 0:
                if self.grid[i - count][j - count] == player:
                    nw += 1
            #check sw
            if i + count < 6 and j - count >= 0:
                if self.grid[i + count][j - count] == player:
                    sw += 1
            #check ne
            if i - count >= 0 and j + count < 7:
                if self.grid[i - count][j + count] == player:
                    ne += 1
        if se + nw + 1 >= 4 or sw + ne + 1 >= 4:
            return True
        return False
