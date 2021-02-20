import math

n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

for p in range(3):
    sum = 0
    for i in range(n):
        sum += math.fabs(x[i] - y[i]) ** (p+1)
    print(f'{sum**float(1/(p+1)):.6f}')

max = -1
for i in range(n):
    if (math.fabs(x[i] - y[i]) > max):
        max = math.fabs(x[i] - y[i])
print(f'{max:.6f}')