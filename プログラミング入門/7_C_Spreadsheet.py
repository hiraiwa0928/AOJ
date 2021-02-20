r, c = map(int, input().split())
a = [list(map(int, input().split())) for i in range(r)]

x = [0 for i in range(c+1)]

for i in range(r):
    sum = 0
    for j in range(c):
        sum += a[i][j]
        print(f'{a[i][j]} ', end = '')
        x[j] += a[i][j]
    print(sum)
    x[j+1] += sum

for i in range(c + 1):
    print(f'{x[i]}', end = '')
    if i != c:
        print(' ', end = '')
    else:
        print()
