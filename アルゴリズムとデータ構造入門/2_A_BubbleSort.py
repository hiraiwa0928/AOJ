n = int(input())
a = list(map(int, input().split()))

flag = 1 # 逆の隣接要素が存在する
cnt = 0

while flag:
    flag = 0
    for j in reversed(range(1, n)):
        if a[j] < a[j-1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            flag = 1
            cnt += 1

[print(f'{a[i]} ', end = '') if len(a) != i+1 else print(f'{a[i]}') for i in range(len(a))]
print(cnt)