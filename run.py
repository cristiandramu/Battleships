# ‘*’ indicates the ships hit
# ‘-‘ indicates the hits missed
from random import randint

Hidden_Pattern = [[' '] * 8 for x in range(8)]
Guess_Pattern = [[' '] * 8 for x in range(8)]

let_to_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}


def print_board(board):
    print('  A B C D E F G H')
    print(' ________________________')
    row_num = 1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num += 1


# Enter the row number between 1 to 8
def get_ship_location():
    row = input('Please enter a ship row 1-8 ')
    while row not in '1 2 3 4 5 6 7 8':
        print("Please enter a valid row ")
        row = input('Please enter a ship row 1-8 ')
# Enter the Ship column from A to H
    column = input('Please enter a ship column A-H ').upper()
    while column not in 'A B C D E F G H':
        print("Please enter a valid column ")
        column = input('Please enter a ship column A-H ')
    return int(row)-1, let_to_num[column]


# Function to create the battleships
def create_ships(board):
    for ship in range(5):
        ship_r, ship_cl = randint(0, 7), randint(0, 7)
        while board[ship_r][ship_cl] == "*":
            ship_r, ship_cl = randint(0, 7), randint(0, 7)
        board[ship_r][ship_cl] = '*'


def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == '*':
                count += 1
    return count


create_ships(Hidden_Pattern)

turns = 10
while turns > 0:
    print('Welcome to the battlefield soldier!')
    print_board(Guess_Pattern)
    row, column = get_ship_location()
    if Guess_Pattern[row][column] == '-':
        print(' You have already fired at this location ')
    elif Hidden_Pattern[row][column] == '*':
        print(' Battleship hit! ')
        Guess_Pattern[row][column] = '*'
        turns -= 1
    else:
        print('No hit')
        Guess_Pattern[row][column] = '-'
        turns -= 1
    if count_hit_ships(Guess_Pattern) == 5:
        print("You have sunk all the battleships ")
        break
    print(' You have ' + str(turns) + ' torpedos remaining ')
    if turns == 0:
        print('Game Over')