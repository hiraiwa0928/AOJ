class RollDice:

    def __init__(self, dice):
        self.dice = dice
        self.spot = dice[0]
    
    def Roll_N(self):
        self.dice[0], self.dice[1], self.dice[4], self.dice[5] = self.dice[1], self.dice[5], self.dice[0], self.dice[4]
        self.spot = self.dice[0]
    
    def Roll_S(self):
        self.dice[0], self.dice[1], self.dice[4], self.dice[5] = self.dice[4], self.dice[0], self.dice[5], self.dice[1]
        self.spot = self.dice[0]

    def Roll_E(self):
        self.dice[0], self.dice[2], self.dice[3], self.dice[5] = self.dice[3], self.dice[0], self.dice[5], self.dice[2]
        self.spot = self.dice[0]
    
    def Roll_W(self):
        self.dice[0], self.dice[2], self.dice[3], self.dice[5] = self.dice[2], self.dice[5], self.dice[0], self.dice[3]
        self.spot = self.dice[0]
    
    def Roll_Right(self):
        self.dice[1], self.dice[2], self.dice[3], self.dice[4] = self.dice[3], self.dice[1], self.dice[4], self.dice[2]

    def Roll_left(self):
        self.dice[1], self.dice[2], self.dice[3], self.dice[4] = self.dice[2], self.dice[4], self.dice[1], self.dice[3]

if __name__ == '__main__':
    dice1 = list(map(int, input().split()))
    dice2 = list(map(int, input().split()))

    d1 = RollDice(dice1)
    d2 = RollDice(dice2)
    tmp = d2

    judge = 0

    for i in range(6):
        d2 = tmp

        if i%2 == 0:
            tmp.Roll_W()
        else:
            tmp.Roll_N()

        for i in range(3):
            if d1.dice[0] == d2.dice[0]:
                break
            d2.Roll_W()
        for i in range(3):
            if d1.dice[0] == d2.dice[0]:
                break
            d2.Roll_N()
        for i in range(3):
            if d1.dice[1] == d2.dice[1]:
                break
            d2.Roll_Right()

        match = 1
        for i in range(6):
            if d1.dice[i] != d2.dice[i]:
                match = 0
        
        if match == 1:
            judge = 1
            break
    
    print('Yes') if judge == 1 else print('No')