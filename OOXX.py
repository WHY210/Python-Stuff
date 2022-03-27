import random

#  (0,0)|(0,1)|(0,2)      1|2|3
#  (1,0)|(1,1)|(1,2)  =>  4|5|6
#  (2,0)|(2,1)|(2,2)      7|8|9
board = [[1,2,3],[4,5,6],[7,8,9]]

#print board
def display_board(board):
    for r in range(3):
        print("+-------"*3+"+")
        print("|       "*3+"|")
        for c in range(3):
            print("|  ", board[r][c],  "  ", end="")
        print("|")
        print("|       "*3+"|")
    print("+-------"*3+"+")

#winner
def victory_for(board, sign):
    flag = False
    if board[0][0] == board[1][1] == board[2][2]\
    or board[0][2] == board[1][1] == board[2][0]:
        flag = True
        if(sign):
            display_board(board)
            print("the player using 'X's has won the game")
        else:
            display_board(board)
            print("the player using 'O's has won the game")
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]\
        or board[0][i] == board[1][i] == board[2][i]:
            flag = True
            if(sign):
                print("the player using 'X's has won the game")
            else:
                print("the player using 'O's has won the game")
    return flag
              

#computer move
def draw_move(board):
    free = make_list_of_free_fields(board)
    place = free[random.randint(0, len(free)-1)]
    row = (place-1) // 3
    col = (place-1) % 3
    board[row][col] = "X"

#user move
def enter_move(board):
    Same = False
    while(Same == False):
        place = int(input("Enter your move:"))
        row = (place-1) // 3
        col = (place-1) % 3
        Same =(board[row][col] == "X" or board[row][col] == "O")
        if Same == True:
            print("Enter another one.")
            Same = not Same
        else:
            board[row][col] = "O"
            Same = not Same
            
    
#find free space
def make_list_of_free_fields(board):
    free = []
    for i in range(1, 10):
        row = (i-1) // 3
        col = (i-1) % 3
        if(board[row][col] in range(1, 10)):
            free.append(i)
    return free
   
#switch
    #if switch == True: computer move, else: user move
    #if victory_for: break
board[1][1] = "X"
sign = False
while(True):
    display_board(board)
    if sign:
        draw_move(board)
    else: 
        enter_move(board)
    
    if victory_for(board, sign):
        break
    #change side
    sign = not sign
