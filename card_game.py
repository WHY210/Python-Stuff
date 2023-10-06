# coding=utf-8
####王DRO的選修3.14功課_無聊比大小遊戲
####by:WHY/2023.3.13


import random
from random import shuffle
ranklist = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
suitlist = ['\u2666','\u2665','\u2663','\u2660'] # 紅心/黑桃/梅花/方塊

class Card: 
    def __init__(self,rank,suit):  ## 建構子
        self.rank = rank  # 數字屬性
        self.suit = suit  # 符號屬性
    def dealCard(self):    
        self.rank = random.choice(ranklist)       # 抽數字
        self.suit = random.choice(suitlist)   # 抽符號
    def __str__(self): ## 建構子之印字串
        return (self.rank+self.suit)
    def __lt__(self,other):  ## 建構子之富比較運算的<
        if self.rank == other.rank: # 數字同的時候再比符號
            return self.suit < other.suit
        else:
            return self.rank < other.rank 

class Deck: ## 牌庫
    def __init__(self):
        self.cardlist=[]
        for i in ranklist:
            for j in suitlist:
                self.cardlist.append(Card(i,j)) 
        shuffle(self.cardlist)
    def show(self):
        i=1
        for c in self.cards:
            print("(%d)" %(i))
            i+=1
    def __len__(self):  ## 建構子之list長度
        return len(self.cardlist)
    def pop(self):  ## 移除list內最後一項
        return self.cardlist.pop()

class Hand(Deck): ## Deck的子Class-玩家手牌
    def __init__(self,player):
        self.cardlist = []      # 繼承Deck的cards屬性但直接蓋掉
        self.player = player # 玩家名稱屬性
        self.win_count = 0   # 獲勝次數屬性
    def __str__(self):     # 印：玩家：玩家手中所有牌
        return self.player + ':' + '.'.join(['' + str(card) for card in self.cardlist])
    def get_player(self):
        return self.player
    def get_win_count(self):
        return self.win_count + 1
    def round_winner(self):
        self.win_count=self.win_count + 1
    def add_card(self,card):
        self.cardlist.append(card)

# (3)創建class Game與start()
class Game:
    def __init__(self):
        self.deck=Deck() 
        self.handlist = []
    def start(self):
        ## (1)設定玩家人數與姓名
        n = int(input("請問總共有多少人玩此遊戲(可2~4人遊玩)："))
        for i in range(n): 
            self.handlist.append(Hand(str(input("請輸入使用者%d姓名：" %(i+1)))))  # Hand那邊是__init__(self,player)
        ## 抽牌直到沒牌
        while len(self.deck)> 52%n: 
            for hand in self.handlist:  # hand=玩家
                hand.add_card(self.deck.pop())
        ## 開始出牌
        for i in range(1,52//n+1):
            ## (2)當'Q'被按時程式停⽌遊戲並顯⽰從⼀開始至現在之各輪贏家資訊
            if input("按任⼀除了'Q'之外的鍵可開始⼀輪遊戲（按Q結束遊戲）") == "Q":
                break
            else:
                played_cards=[]  # 那一輪出出來的牌
                for hand in self.handlist:
                    played_cards.append(hand.pop())
                win_card=max(played_cards)
                win_hand=self.handlist[played_cards.index(win_card)]  # 看最大的那張是誰出的
                win_hand.round_winner()
                print("Rounds%d:%s,Winner:%s,%s" %(i, ' '.join([str(card) for card in played_cards]), win_hand.get_player(), str(win_card)))
        for hand in self.handlist:
                    print("score for %s：%d" %(hand.get_player(),hand.get_win_count()-1))
Game().start()