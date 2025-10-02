import random

print('Welcome to my TicTacToe game!')
print('------------------------------')

possibleNumbers = [1,2,3,4,5,6,7,8,9]
gameBoard = [[1,2,3],
             [4,5,6],
             [7,8,9]
]

horizontal = 3
vertical = 3

def printGameBoard():
    for x in range(horizontal):
        print('\n+---+---+---+')
        print('|', end='')
        for y in range(vertical):
            print('', gameBoard[x][y], end=' |')
    print('\n+---+---+---+')
printGameBoard()