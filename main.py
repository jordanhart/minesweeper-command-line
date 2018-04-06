import random

def play_game():
    print("welcome to minesweeper")
    selected = set()
    board, length, width, num_mines = generate_board()
    game_end = False
    while(not game_end):
        print_board(board, length, width, selected)
        game_end=take_turn(board, selected, num_mines)
    print_board(board, length, width, range(len(board)))
    print("You " + game_end+ '!')
def generate_board():
    option = int(input("select board: \n 1)8x8 \n 2)16x16 \n 3)16x30\n"))
    if(option == 1):
        length = 8
        width = 8
        mines = 10
    elif(option == 2):
        length = 16
        width = 16
        mines = 40
    elif(option == 3):
        length = 16
        width = 30
        mines = 99
    else:
        return generate_board()
    board_nums = length * width
    return fill_in_board(board_nums, mines, length, width), length, width, mines

def fill_in_board(squares, mines, length, width):
    #fills in mines, and number if neighbor close to mine
    mine_locations = random.sample(range(squares), mines)
    board = [0 for i in range(squares)]
    for mine in mine_locations:
        board[mine] = 'x'
    for s in range(squares):
        if (board[s] != 'x'):
            board[s] = mines_nearby(board, s, length, width)
    return board

def mines_nearby(board, square, length, width):
    #bug numbers on edge
    if (square % length == 0):
        neighbors = [square+1, square+length, square - length, square + length + 1, square - length + 1]
    elif (square % length == length - 1):
        neighbors = [square-1, square+length, square - length, square + length - 1, square - length - 1]
    else:
        neighbors = [square+1, square-1, square+length, square - length, square + length - 1, square + length + 1, square - length - 1, square - length + 1]
    mine_count = 0
    for s in neighbors:
        if(s < len(board) and s >= 0 and board[s] == 'x'):
            mine_count += 1
    return mine_count

def print_board(board, length, width, selected=[]):
    count = 0
    for s in range(len(board)):
        if (s in selected):
            letter = board[s]
        else:
            letter = '?'
        if (count < length - 1):
            print(letter, end=', ')
            count+=1
        else:
            print(letter)
            count=0
def take_turn(board, selected, mines):
    select=int(input("select a square: ")) - 1
    selected.add(select)
    if (board[select] == 'x'):
        return 'lost'
    elif (len(selected) == len(board) - mines):
        return 'won'
    else:
        return False
            
play_game()
