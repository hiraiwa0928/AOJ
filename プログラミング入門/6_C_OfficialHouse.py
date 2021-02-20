n = int(input())
info = [list(map(int, input().split())) for i in range(n)]
ans = [[0]*10 for i in range(3*4)]

for i in range(n):
    ans[((info[i][0] - 1)*3 - 1) + info[i][1]][info[i][2] - 1] += info[i][3]

for num1, ele1 in enumerate(ans):
    for num2, ele2 in enumerate(ele1):
        print(f' {ele2}', end = '') if num2 != 10 -1 else print(f' {ele2}')
    if (num1 + 1) % 3 == 0 and num1 != 11:
        print('####################')