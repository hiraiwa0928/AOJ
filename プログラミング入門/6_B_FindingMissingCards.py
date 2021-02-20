n = int(input())
cards = [list(map(str, input().split())) for i in range(n)]
marks = ['S', 'H', 'C', 'D']

for mark in marks:
    for num in range(13):
        match = 0
        for i in range(n):
            if cards[i][0] == mark and int(cards[i][1]) == num + 1:
                match = 1
                break
        if match == 0:
            print(f'{mark} {num + 1}')