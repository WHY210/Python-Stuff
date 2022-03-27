def checkone(one):
    return "".join(sorted(one)) == '123456789'

s =input().split()

def is_sudoku(s):
    is_sudoku = True
    for i in range(9):
        is_sudoku = is_sudoku and checkone(list(s[i]))
        if(not is_sudoku): break
    if(is_sudoku):
        for k in range(9):
            m = [s[i][k] for i in range(9)]
            is_sudoku = is_sudoku and checkone(m)
            if(not is_sudoku): break
    if(is_sudoku):
        n=[]
        for i in range(3):
            for j in range(3):
                for h in range(3):
                    p = 3 * i + h
                    for k in range(3):
                        q = 3 * j + k
                        n.append(s[p][q])    
                is_sudoku = is_sudoku and checkone(n)          
                if(not is_sudoku): break
                n=[]
    return is_sudoku

if is_sudoku(s) == True:
    print("Yes")
else:
    print("No")