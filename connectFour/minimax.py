
class ConnectFour:
    def __init__(self):
        self.grid = [['O' for i in range(7)] for j in range(6)]
        self.score = {'Red': 0, 'Black': 0, 'Winner': ''}
        self.amounts = [0, 0, 0, 0, 0, 0, 0]  # Amount of chips in each column
        self.players = ['B', 'R']

    def display(self):
        for i in range(6):
            for j in range(7):
                print(self.grid[i][j], end=' ')
            print()
        return

    def place(self, player, column):
        """
        Put a player's chip on the board
        :param player: Player's color
        :param column: Column to add that player's chip to
        :return:
        """
        placed = False
        while not placed:
            if 6 <= column >= 0 and self.amounts[column] < 6:
                placed = True
                self.grid[self.amounts[column]][column] = player

    def full(self):
        """
        Determine if the grid is full (reached end game) or not.
        :return: True if the board is full, otherwise return False
        """
        for i in range(6):
            for j in range(7):
                if self.grid[i][j] == 'O':
                    return False
        return True

    def checkRC(self, i, j, player):
        """
        Checks rows and columns of piece around origin i, j.
        Counts the pieces in vertical and horizontal directions
        and adds them. Counting does not include origin piece,
        so + 1 will be added when checking.
        e + w + 1
        n + s + 1
        :param i: Row of origin
        :param j: Column of origin
        :param player: Player's color we are checking
        :return: The bigger of the two counts (horizontal or vertical)
        """
        n = 0
        s = 0
        e = 0
        w = 0

        # Check in the following order: s -> n -> w -> e
        for count in range(1, 4):
            if i + count < 6:
                if self.grid[i + count][j] == player:
                    s += 1
            if i - count >= 0:
                if self.grid[i - count][j] == player:
                    n += 1
            if j + count < 7:
                if self.grid[i][j + count] == player:
                    w += 1
            if j - count >= 0:
                if self.grid[i][j - count] == player:
                    e += 1
        r = e + w + 1
        c = n + s + 1
        if r > c:
            return r
        return c

    def checkDiag(self, i, j, player):
        """
        Checks diagonals of piece around origin i, j.
        Counts the pieces in each of the diagonal directions
        and adds them. Counting does not include origin piece,
        so + 1 will be added when checking.
        sw + ne + 1
        se + nw + 1
        :param i: Row of origin
        :param j: Column of origin
        :param player: Player's color we are checking
        :return: The bigger of the two counts (bottom left to top right or top left to bottom right)
        """
        ne = 0
        nw = 0
        se = 0
        sw = 0

        # check in order: se -> nw -> sw -> ne
        for count in range(1, 4):
            # check se
            if i + count < 6 and j + count < 7:
                if self.grid[i + count][j + count] == player:
                    se += 1

            # check nw
            if i - count >= 0 and j - count >= 0:
                if self.grid[i - count][j - count] == player:
                    nw += 1

            # check sw
            if i + count < 6 and j - count >= 0:
                if self.grid[i + count][j - count] == player:
                    sw += 1

            # check ne
            if i - count >= 0 and j + count < 7:
                if self.grid[i - count][j + count] == player:
                    ne += 1

        diag1 = se + nw + 1
        diag2 = sw + ne + 1
        if diag1 > diag2:
            return diag1
        return diag2

    def win(self):
        """

        :return:
        """
        for i in range(6):
            for j in range(7):
                if self.grid[i][j] == self.players[0]:
                    w = self.checkRC(i, j, self.players[0])
                    if w >= 4:
                        return self.players[0]
                    w = self.checkDiag(i, j, self.players[0])
                    if w >= 4:
                        return self.players[0]
                elif self.grid[i][j] == self.players[1]:
                    w = self.checkRC(i, j, self.players[1])
                    if w >= 4:
                        return self.players[1]
                    w = self.checkDiag(i, j, self.players[1])
                    if w >= 4:
                        return self.players[1]
                else:
                    continue

        if self.full():
            return 'T'
        else:
            return '...'

    def evaluate(self):
        winner = self.win()

        if winner == self.players[0]:
            return 22
        elif winner == self.players[1]:
            return -22
        elif winner == 'T':
            return 0



def minimax(board, depth, isMax):
    pass


def findBestMove(board):
    pass
