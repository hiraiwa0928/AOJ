while(True):
    s = list(input())
    if s[0] == '-':
        break
    m = int(input())
    for i in range(m):
        n = int(input())
        tmp1 = []
        tmp2 = []
        tmp1 = s[0:n]
        tmp2 = s[n:]
        s = []
        tmp2.extend(tmp1)
        s = tmp2
    for i in s:
        print(i, end = '')
    print()