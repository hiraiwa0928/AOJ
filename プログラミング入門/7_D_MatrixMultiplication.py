n, m, l = map(int, input().split())

a = []
b = []

for i in range(n):
    a.append(list(input().split()))

for i in range(m):
    b.append(list(input().split()))

for i in range(n):
    for j in range(l):
        output = 0
        for k in range(m):
            output += int(a[i][k]) * int(b[k][j])
        print(f'{output}', end = '')
        if j == l - 1:
            print('\n', end = '')
        else:
            print(' ', end = '')