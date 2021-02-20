n = int(input())
a = list(map(int, input().split()))

cnt = 0

for i in range(0, n):
    minj = i
    for j in range(i, n):
        if a[j] < a[minj]:
            minj = j
    if i != minj:
        a[i], a[minj] = a[minj], a[i]
        cnt += 1

[print(f'{a[i]} ', end = '') if len(a) != i+1 else print(f'{a[i]}') for i in range(len(a))]
print(cnt)