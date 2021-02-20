w = str(input())
cnt = 0

print(f'target: {w}')

while(True):
    t = list(input().split())
    if t[0] == 'END_OF_TEXT':
        break
    for word in t:
        if(word.lower() == w):
            cnt += 1

print(cnt)