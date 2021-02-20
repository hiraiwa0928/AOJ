while(1):
    s = str(input())
    if s == '0':
        exit()
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
    print(sum)