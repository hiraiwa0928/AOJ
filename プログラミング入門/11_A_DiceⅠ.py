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

if __name__ == '__main__':
    dice = list(map(int, input().split()))
    dirs = list(input())

    d = RollDice(dice)

    for dir in dirs:
        if dir == 'N':
            d.Roll_N()
        elif dir == 'S':
            d.Roll_S()
        elif dir == 'E':
            d.Roll_E()
        elif dir == 'W':
            d.Roll_W()
    
    print(d.spot)