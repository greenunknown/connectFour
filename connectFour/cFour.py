import player
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
            return -5, 5 - self.amounts[column]
        if self.amounts[column] == 6:
            return -5, 5 - self.amounts[column]
        if player == 'black':
            self.grid[5 - self.amounts[column]][column] = 'B'
        elif player == 'red':
            self.grid[5 - self.amounts[column]][column] = 'R'
        else:
            print('error: invalid player code')
            exit(-1)
        self.amounts[column] += 1
        return 0, 5 - self.amounts[column] + 1

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
                    if w >= 4:
                        return 'Black', w
                    w = self.checkDiag(i, j, 'B')
                    if w >= 4:
                        return 'Black', w
                elif self.grid[i][j] == 'R':
                    w = self.checkRC(i, j, 'R')
                    if w >= 4:
                        return 'Red', w
                    w = self.checkDiag(i, j, 'R')
                    if w >= 4:
                        return 'Red', w
                else:
                    continue
        return 'none', w

    def checkRC(self, i, j, player):
        n = 0
        s = 0
        e = 0
        w = 0
        for count in range(1,4):
            cont = True
            if i + count < 6:
                if self.grid[i + count][j] == player:
                    if cont == True:
                        s += 1
                else:
                    cont = False
            cont = True
            if i - count >= 0:
                if self.grid[i - count][j] == player:
                    if cont == True:
                        n += 1
                else:
                    cont = False
            cont = True
            if j + count < 7:
                if self.grid[i][j + count] == player:
                    if cont == True:
                        w += 1
                else:
                    cont = False
            cont = True
            if j - count >= 0:
                if self.grid[i][j - count] == player:
                    if cont == True:
                        e += 1
                else:
                    cont = False
        r = e + w + 1
        c = n + s + 1
        if r > c:
            return r
        return c

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
            cont = True
            #check se
            if i + count < 6 and j + count < 7:
                if self.grid[i + count][j + count] == player:
                    if cont == True:
                        se += 1
                else:
                    cont = False
            cont = True
            #check nw
            if i - count >= 0 and j - count >= 0:
                if self.grid[i - count][j - count] == player:
                    if cont == True:
                        nw += 1
                else:
                    cont = False
            cont = True
            #check sw
            if i + count < 6 and j - count >= 0:
                if self.grid[i + count][j - count] == player:
                    if cont == True:
                        sw += 1
                else:
                    cont = False
            cont = True
            #check ne
            if i - count >= 0 and j + count < 7:
                if self.grid[i - count][j + count] == player:
                    if cont == True:
                        ne += 1
                else:
                    cont = False
        diag1 = se + nw + 1
        diag2 = sw + ne + 1
        if diag1 > diag2:
            return diag1
        return diag2

    def state(self):
        state = ''
        for i in range(6):
            for j in range(7):
                state += self.grid[i][j]
        return state

    def step(self, player, action):#for rl algorithm
        reward, row = self.put(player, action)
        done, r2 = self.win()
        reward += r2
        return self.state(), reward, done