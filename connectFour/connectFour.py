import sys
import cFour

def main():
    if len(sys.argv) > 3:
        print('usage: python3 connectFour.py [String] [String] || python3 connectFour.py')
        return
    if len(sys.argv) > 1 and len(sys.argv) < 3:
        print('usage: python3 connectFour.py [String] [String] || python3 connectFour.py')
        return
    c = cFour.cFour()
    turn = 1
    while True:
        c.display()
        player = ''
        if turn%2 == 1:
            player = 'black'
        else:
            player = 'red'
        print(player + '\'s turn')
        i = int(input("Select column to place piece (0-6): "))
        flag, r = c.put(player, i)
        if flag == -5:
            print('Invalid column, try again.')
            continue
        winner, r = c.win()
        if winner == 'Black' or winner == 'Red':
            c.display()
            print(winner + ' wins!')
            return
        turn += 1

    

main()
