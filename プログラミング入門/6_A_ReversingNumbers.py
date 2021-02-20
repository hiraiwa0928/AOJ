n = int(input())

a = list(input().split())

for i, ele in enumerate(reversed(a)):
    print(f'{ele} ', end = '') if i != n-1 else print(ele)