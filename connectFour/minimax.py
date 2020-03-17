
# Written based on code from:
#  https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-3-tic-tac-toe-ai-finding-optimal-move/

class MinimaxConnectFour:
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
            if 0 <= column <= 6:
                if self.amounts[column] < 6:
                    placed = True
                    self.grid[self.amounts[column]][column] = player
                    self.amounts[column] += 1
                    return [self.amounts[column], column]

    def remove(self, player, column):
        self.grid[self.amounts[column]][column] = 'O'
        self.amounts[column] -= 1
        return [self.amounts[column], column]

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
        nadd = True
        sadd = True
        eadd = True
        wadd = True

        # Check in the following order: n -> s -> e -> w
        for count in range(1, 4):
            if i - count >= 0 and nadd:
                if self.grid[i - count][j] == player:
                    n += 1
                else:
                    nadd = False

            if i + count < 6 and sadd:
                if self.grid[i + count][j] == player:
                    s += 1
                else:
                    sadd = False

            if j - count >= 0 and eadd:
                if self.grid[i][j - count] == player:
                    e += 1
                else:
                    eadd = False

            if j + count < 7 and wadd:
                if self.grid[i][j + count] == player:
                    w += 1
                else:
                    wadd = False

        r = e + w + 1
        c = n + s + 1

        return max(r, c)

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

        neadd = True
        nwadd = True
        seadd = True
        swadd = True

        # check in order: ne -> nw -> se -> sw
        for count in range(1, 4):
            # check ne
            if i - count >= 0 and j + count < 7 and neadd:
                if self.grid[i - count][j + count] == player:
                    ne += 1
                else:
                    neadd = False

            # check nw
            if i - count >= 0 and j - count >= 0 and nwadd:
                if self.grid[i - count][j - count] == player:
                    nw += 1
                else:
                    nwadd = False

            # check se
            if i + count < 6 and j + count < 7 and seadd:
                if self.grid[i + count][j + count] == player:
                    se += 1
                else:
                    seadd = False

            # check sw
            if i + count < 6 and j - count >= 0 and swadd:
                if self.grid[i + count][j - count] == player:
                    sw += 1
                else:
                    swadd = False

        diag1 = se + nw + 1
        diag2 = sw + ne + 1
        return max(diag1, diag2)

    def win(self, row, col):
        """
        :param row: The row of the piece that was just placed.
        :param col: The column of the piece that was just placed.
        :return: The result of the lastest move if a player won, the game is a draw, or the game is ongoing
        """
        if self.grid[row][col] == self.players[0]:
            w = self.checkRC(row, col, self.players[0])
            if w >= 4:
                return self.players[0]
            w = self.checkDiag(row, col, self.players[0])
            if w >= 4:
                return self.players[0]
        elif self.grid[row][col] == self.players[1]:
            w = self.checkRC(row, col, self.players[1])
            if w >= 4:
                return self.players[1]
            w = self.checkDiag(row, col, self.players[1])
            if w >= 4:
                return self.players[1]

        if self.full():
            return 'T'
        else:
            return '...'

    def evaluate(self, row, col):
        winner = self.win(row, col)

        if winner == self.players[0]:
            return 22
        elif winner == self.players[1]:
            return -22
        elif winner == 'T':
            return 1
        else:
            return 0

    def minimax(self, depth, isMax, player, opponent, row, col):
        score = self.evaluate(row, col)

        if score == 22:
            return score

        if score == -22:
            return score

        if not self.full():
            return 0

        if isMax:
            best = -1000
            for i in range(7):
                if self.amounts[i] < 5:
                    self.place(player, i)
                    best = max(best, self.minimax(depth + 1, not isMax, player, opponent))
                    self.remove(player, i)
            return best
        else:
            best = 1000
            for i in range(7):
                if self.amounts[i] < 5:
                    self.place(player, i)
                    best = max(best, self.minimax(depth + 1, not isMax, player, opponent))
                    self.remove(player, i)
            return best

    def findBestMove(self, player, opponent):
        bestVal = -1000
        bestMove = -1
        for i in range(7):
            if self.amounts[i] < 5:
                self.place(player, i)
                moveVal = self.minimax(0, False, player, opponent)
                self.remove(player, i)

                if moveVal > bestVal:
                    bestMove = i
                    bestVal = moveVal

        print(f"The value of the best move is: {bestMove}\n\n")

        return bestMove


def main():
    game = MinimaxConnectFour()

    while not game.full():
        game.display()
        # Human
        # print("Enter where you want to place pieces: ")
        # player_input_x = input("row: ")
        # player_input_y = input("col: ")
        # board[int(player_input_x)][int(player_input_y)] = 'x'
        print("Player one")
        bestMove = game.findBestMove(game.players[0], game.players[1])
        print("Placing piece")
        game.place(game.players[0], bestMove)
        print(f"The optimal move for {game.players[0]} is:\n")
        print(f"Row: {bestMove}\n\n")

        bestMove = game.findBestMove(game.players[1], game.players[0])
        game.place(game.players[1], bestMove)
        print(f"The optimal move for {game.players[1]} is:\n")
        print(f"Row: {bestMove}\n\n")


main()
