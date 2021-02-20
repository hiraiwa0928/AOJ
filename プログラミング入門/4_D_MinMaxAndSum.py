n = int(input())
a = list(map(int, input().split()))
a = sorted(a)
print(a[0], a[n-1], sum(a))