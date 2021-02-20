n = int(input())
rt = [int(input())]
rt.append(int(input()))
ri = rt[0]
rj = rt[1]

ans = rj - ri

for i in range(2, n):
    rt.append(int(input()))
    if ri > rt[i-1]:
        ri = rt[i-1]
    if ans < rt[i] - ri:
        ans = rt[i] - ri

print(ans)