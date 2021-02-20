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
    n = int(input())
    dice = [list(map(int, input().split())) for i in range(n)]

    c_dice = [RollDice(dice[i]) for i in range(n)] # RollDiceをインスタンス化

    tmp = c_dice # c_diceをコピー

    judge = 1

    for i in range(n-1):
        if judge == 0:
            break

        for j in range(i+1, n):
            if judge == 0:
                break

            for k in range(6):
                # サイコロの目に同じ数字が複数含まれていた場合は、
                # サイコロの初期位置を変えて全６パターンを検証
                c_dice[j] = tmp[j]

                if k%2 == 0:
                    tmp[j].Roll_W()
                else:
                    tmp[j].Roll_N()
                
                for num in range(3):
                    if c_dice[i].dice[0] == c_dice[j].dice[0]:
                        break
                    c_dice[j].Roll_W()
                for num in range(3):
                    if c_dice[i].dice[0] == c_dice[j].dice[0]:
                        break
                    c_dice[j].Roll_N()
                for num in range(3):
                    if c_dice[i].dice[1] == c_dice[j].dice[1]:
                        break
                    c_dice[j].Roll_Right()

                match = 1
                for num in range(6):
                    if c_dice[i].dice[num] != c_dice[j].dice[num]:
                        match = 0
                
                if match == 1: # 同じサイコロがあった場合judge=0とし、結果を出力
                    judge = 0
                    break
    
    print('Yes') if judge == 1 else print('No')