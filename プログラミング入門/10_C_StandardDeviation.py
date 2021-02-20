import math

while(True):
    n = int(input())
    if n == 0:
        break
    s = list(map(float, input().split()))
    sum = float(0)
    for i in range(n):
        sum += s[i]
    ave = sum/n
    tmp = float(0)
    for i in range(n):
        tmp += 1/n * (s[i]-ave)**2
    print(f'{math.sqrt(tmp):.8f}')