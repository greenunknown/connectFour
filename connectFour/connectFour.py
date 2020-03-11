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
        i = int(input("Select column to place piece: "))
        player = ''
        if turn%2 == 1:
            player = 'black'
        else:
            player = 'red'
        c.put(player, i)
        winner = c.win()
        if winner == 'Black' or winner == 'Red':
            c.display()
            return
        turn += 1

    

main()
