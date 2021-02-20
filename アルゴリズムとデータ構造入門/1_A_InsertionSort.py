n = int(input())
a = list(map(int, input().split()))

[print(f'{a[num]} ', end = '') if len(a) != num+1 else print(f'{a[num]}', end = '') for num in range(len(a))]
print()

for i in range(1, n):
    
    tmp = a[i]
    j = i - 1
    while(j >= 0 and a[j] > tmp):
        a[j+1] = a[j]
        j -= 1
    a[j+1] = tmp
    [print(f'{a[num]} ', end = '') if len(a) != num+1 else print(f'{a[num]}', end = '') for num in range(len(a))]
    print()