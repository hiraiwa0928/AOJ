def str_print(a, b):
    for i in range(a, b+1):
        print(str[i], end = '')
    print()

def str_reverse(a, b):
    global str
    tmp1 = str[0:a]
    tmp2 = []
    tmp3 = str[b+1:]
    for i in reversed(range(a, b+1)):
        tmp2.extend(str[i])
    str = []
    tmp1.extend(tmp2)
    tmp1.extend(tmp3)
    str.extend(tmp1)

def str_replace(a, b, s):
    s = list(s)
    for i in range(len(s)):
        str[a + i] = s[i]

if __name__ == '__main__':
    str = list(input())
    q = int(input())

    for i in range(q):
        ord = list(input().split())
        if ord[0] == 'print':
            str_print(int(ord[1]), int(ord[2]))
        elif ord[0] == 'reverse':
            str_reverse(int(ord[1]), int(ord[2]))
        else:
            str_replace(int(ord[1]), int(ord[2]), ord[3])
