class cFour():
    """
    A connect four board and methods to manipulate and
    get information about the board.
    """
    def __init__(self):
        self.grid = [['O' for i in range(7)] for j in range(6)]
        self.score = {'Red': 0, 'Black': 0, 'Winner': ''}
        self.amounts = [0, 0, 0, 0, 0, 0, 0]

    def put(self, player, column):
        """
        Put a player's chip on the board
        :param player: Player's color
        :param column: Column to add that player's chip to
        :return:
        """
        if column > 6 or column < 0:
            return -5, 0  # TODO FIX THE RETURN works for negative numbers
                            # because of the way python lists work but not larger numbers
                            # ORIGINAL # 5 - self.amounts[column]
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
                print(self.grid[i][j], end=' ')
            print()
        return

    def full(self):
        """
        Determine if the grid is full (reached end game) or not.
        :return: 'full' if the board is full, otherwise return 'not full'
        """
        for i in range(6):
            for j in range(7):
                if self.grid[i][j] != 'B' or self.grid[i][j] != 'R':
                    return 'not full'
        return 'full'

    def win(self):
        """

        :return:
        """
        for i in range(6):
            for j in range(7):
                if self.grid[i][j] == 'B':
                    w = self.checkRC(i, j, 'B')
                    if w >= 4:
                        return 'black', w
                    w = self.checkDiag(i, j, 'B')
                    if w >= 4:
                        return 'black', w
                elif self.grid[i][j] == 'R':
                    w = self.checkRC(i, j, 'R')
                    if w >= 4:
                        return 'red', w
                    w = self.checkDiag(i, j, 'R')
                    if w >= 4:
                        return 'red', w
                else:
                    continue
        return self.full(), w

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

    def state(self):
        """

        :return: Return the state
        """
        state = ''
        for i in range(6):
            for j in range(7):
                state += self.grid[i][j]
        return state

    def step(self, player, action):
        """
        Used in the RL algorithm to simulate moves.
        :param player:
        :param action:
        :return:
        """
        reward, row = self.put(player, action)
        done, r2 = self.win()
        reward += r2
        return self.state(), reward, done
