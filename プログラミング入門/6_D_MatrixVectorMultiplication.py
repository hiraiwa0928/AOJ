n, m = map(int, input().split())
A = [list(map(int, input().split())) for i in range(n)]
b = [list(map(int, input().split())) for i in range(m)]
c = [[0] for i in range(n)]

for i in range(n):
    for j in range(m):
        c[i][0] += A[i][j] * int(b[j][0])

for i in range(len(c)):
    print(c[i][0])