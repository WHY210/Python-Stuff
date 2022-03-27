import random

#print board
board = [1,2,3,4,5,6,7,8,9]
def display_board(board):
    for r in range(3):
        print("+-------"*3 + "+")
        print("|       "*3 + "|")
        for c in range(3):   
            print("|  ", board[r*3+c], "  ",end = "")
        print("|")
        print("|       "*3 + "|")
    print("+-------"*3 + "+")

def enter_move(board):
    display_board(board)
    user = int(input("Enter your move"))
    if board[user-1] in range(1,10):
        board[user-1] = "O"
    else:
        print("Enter another one.")
        enter_move(board)  
        
def draw_move(board):
    free = make_list_of_free_fields(board)
    computer = free[random.randint(0, len(free)-1)]
    board[computer-1] = "X"

def make_list_of_free_fields(board):
    free = []
    for place in range(9):
        if board[place] in range(0,10):
            free.append(place)
    return free

def victory_for(board, sign):
    while(True):
        if board[0] == board[4] == board[8]\
            or board[2] == board[4] == board[6]:
            print("the player using", sign, "has won the game")
            break
        else:
            break
        for i in range(3):
            if board[i*3] == board[i*3+1] == board[i*3+2]\
                or board[i] == board[3+i] == board[6+i]:
                print("the player using", sign, "has won the game")
                break
            else:
                break

#switch
sign = "X"
while(True):
    if sign == "X":
        draw_move(board)
        victory_for(board, sign)
        sign = "O"
    if sign == "O":
        enter_move(board)
        victory_for(board, sign)
        sign = "X"
    
