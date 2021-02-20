n = int(input())
c = list(map(str, input().split()))
c_bub = []
c_bub.extend(c)
c_sel = []
c_sel.extend(c)

for i in range(0, n):
    for j in reversed(range(i+1, n)):
        if int(c_bub[j][1]) < int(c_bub[j-1][1]):
            c_bub[j], c_bub[j-1] = c_bub[j-1], c_bub[j]

[print(f'{c_bub[i]} ', end = '') if n != i+1 else print(f'{c_bub[i]}') for i in range(n)]
print('Stable')

for i in range(0, n):
    minj = i
    for j in range(i, n):
        if int(c_sel[j][1]) < int(c_sel[minj][1]):
            minj = j
    c_sel[i], c_sel[minj] = c_sel[minj], c_sel[i]

[print(f'{c_sel[i]} ', end = '') if n != i+1 else print(f'{c_sel[i]}') for i in range(n)]
if c_bub == c_sel:
    print('Stable')
else:
    print('Not stable')