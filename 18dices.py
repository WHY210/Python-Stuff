# coding=utf-8
####朱+0的功課
####by:WHY/2022.4.17

#莊家=owner1
#閒家=player2

#擲骰子:dice()
import random
lst = []
def dice(): 
    lst = []
    for t in range(4): 
        lst.append(random.randint(1,6))
    lst.sort()
    print(lst)
    return lst

#數有幾個相同
def count(lst):
    box = []
    left = []
    for x in range(len(lst)):
        if lst[x] not in box:
            box.append(lst[x])
        else:
            if lst[x] not in left:
                left.append(lst[x])
    oldbox = box 
    for y in range(len(left)):
        if left[y] in box:
            box.remove(left[y])
    output = [len(oldbox), left, box]
    #[幾個不一樣,[一樣的],[不一樣的]]
    return(output)

#分數計算
def howmanypoint(now):
    flag = now
    go_on = 1
    while go_on == 1:
        #print("f",flag)
        if flag[0] == 0:
            if len(flag[1]) == 2: #兩個一樣兩個一樣
                #print("22")
                point = 2 * max(flag[1])
                go_on = 0
            else: #四個一樣
                #print("0")
                point = 100000
                go_on = 0
        if flag[0] == 2:
            #print("211")
            point = flag[2][0] + flag[2][1]
            go_on = 0
        if flag[0] == 1:#三個一樣
            #print("3")
            now = dice()
            flag = count(now)
            go_on = 1
        if flag[0] == 4:#四個都不同 
            #print("4")
            now = dice()
            flag = count(now)
            go_on = 1
    print(point)
    return point


money_player = 100

gogo=1
while gogo == 1:
    
    print("閒家還有", money_player)
    
    if money_player <= 0:
        gogo = 0
        break

    giveup = str(input("放棄請輸入-1，不然就隨便輸入什麼都好: "))
    if giveup == "-1":#放棄
        print("a")
        gogo = 0
        break
    else:#壓賭金
        bet_player = int(input("至少賭10塊，請下注: "))
        while bet_player < 10:
            bet_player = int(input("至少賭10塊，請下注: "))

    
    #owner starts
    print("owner= ")
    a = dice()
    owner = count(a)
    owner = howmanypoint(owner)
    #特例
    if sum(a) == 12 or owner == 100000:
        print("owner wins!!!!!!!!!")
        money_player -= bet_player
        gogo = 1
    else:
        #player starts
        print("player=")
        b = dice()
        player = count(b)
        player = howmanypoint(player)
        #特例
        if sum(b) == 12 or player == 100000:
            print("player wins, double!!!")
            money_player +=  2 * bet_player
            gogo = 1
        else:
            #宣告輸贏
            if owner > player:
                print("owner wins")
                money_player -= bet_player
                gogo = 1
            elif a == b:
                print("owner wins")
                money_player -= bet_player
                gogo = 1
            elif owner == player:
                print("tie")
                gogo = 1
            else:
                print("player wins")
                money_player += bet_player    
                gogo = 1

if gogo == 0:
    print("game over")
