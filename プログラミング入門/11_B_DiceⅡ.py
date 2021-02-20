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
    dice = list(map(int, input().split()))
    d = RollDice(dice)

    n = int(input())

    for i in range(n):
        top, front = map(int, input().split())
        if d.dice[0] != front and d.dice[5] != front:
            while(d.dice[1] != front):
                d.Roll_Right()
            while(d.dice[0] != top):
                d.Roll_W()
        else:
            while(d.dice[0] != top):
                d.Roll_W()
            while(d.dice[1] != front):
                d.Roll_Right()
        
        print(d.dice[2])