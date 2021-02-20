t = 0
h = 0

n = int(input())
for i in range(n):
    s = list(input().split())
    if s[0] > s[1]:
        t += 3
    elif s[0] < s[1]:
        h += 3
    else:
        t += 1
        h += 1

print(t, h)